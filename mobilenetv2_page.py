import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import pandas as pd
import os
import zipfile

def mobilenetv2_classifier_page():
    st.header("👜 MobileNetV2 Fashion Image Classifier")

    # Load MobileNetV2 model and class indices
    mobilenetv2_model = tf.keras.models.load_model('mobilenetv2_model.keras')
    with open('class_indices_mobilenetv2.json', 'r') as f:
        mobilenetv2_class_indices = json.load(f)

    # Preprocess an image to the correct format
    def preprocess_image(uploaded_file):
        img = Image.open(uploaded_file).convert('RGB')
        img = img.resize((128, 128))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        return img_array

    # Predict class for a single image
    def predict_image(model, uploaded_file, class_indices):
        processed_image = preprocess_image(uploaded_file)
        predictions = model.predict(processed_image)
        predicted_class = class_indices[str(np.argmax(predictions))]
        return predicted_class
    
    # Single Image Upload
    st.write("#### Upload a Single Image")
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Classify Single Image"):
            prediction = predict_image(mobilenetv2_model, uploaded_image, mobilenetv2_class_indices)
            st.success(f"Prediction: **{prediction}**")

    # Multiple Image Upload
    st.write("#### Upload Multiple Images")
    multiple_images = st.file_uploader("Upload multiple images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    def predict_multiple_images(images):
        predictions = []
        for uploaded_image in images:
            prediction = predict_image(mobilenetv2_model, uploaded_image, mobilenetv2_class_indices)
            predictions.append({'Image': uploaded_image.name, 'Prediction': prediction})
        return pd.DataFrame(predictions)

    if multiple_images and st.button("Classify Multiple Images"):
        predictions_df = predict_multiple_images(multiple_images)
        st.write("## Results")
        
        # Display results in a grid-like layout
        for idx, row in predictions_df.iterrows():
            st.write(f"**{row['Image']}**")
            st.image(multiple_images[idx], caption=f"Prediction: {row['Prediction']}", width=150)
            st.write("---")

    # Batch Image Upload (Zip File)
    st.write("#### Upload a Zip File of Images")
    uploaded_zip = st.file_uploader("Upload a zip file containing images...", type="zip")

    def predict_zip_images(zip_file):
        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall("temp_images")
            image_files = [f for f in os.listdir("temp_images") if f.endswith(("jpg", "jpeg", "png"))]
            predictions = []
            for image_file in image_files:
                image_path = os.path.join("temp_images", image_file)
                img = Image.open(image_path)
                prediction = predict_image(mobilenetv2_model, img, mobilenetv2_class_indices)
                predictions.append({'Image': image_file, 'Prediction': prediction})
            return pd.DataFrame(predictions)

    if uploaded_zip and st.button("Classify Batch Images"):
        with st.spinner("Classifying batch images..."):
            predictions_df = predict_zip_images(uploaded_zip)
        
        st.write("## Batch Results")
        for idx, row in predictions_df.iterrows():
            st.image(f"temp_images/{row['Image']}", caption=f"{row['Image']} - {row['Prediction']}", width=150)
            st.write("---")

        # Clean up extracted files
        for f in os.listdir("temp_images"):
            os.remove(os.path.join("temp_images", f))
