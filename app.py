import streamlit as st
from cnn_page import cnn_classifier_page
from mobilenetv2_page import mobilenetv2_classifier_page

# Set page configuration with new theme and layout
st.set_page_config(
    page_title="Fashion Trend Classifier",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for style improvements
st.markdown("""
    <style>
        .stApp {
            background-color: #f9f9f9;
            color: #333333;
        }
        header, footer {visibility: hidden;}
        .css-1avcm0n, .css-1ekf893 {color: #ff7f50; font-weight: bold;}
        .css-1kyxreq {background: #fffcf7; border: 1px solid #ff7f50; padding: 1.5rem;}
        .stSelectbox, .stFileUploader, .stButton > button {
            border-radius: 0.5rem;
            background: #fffcf7;
        }
    </style>
""", unsafe_allow_html=True)

# App header
st.title("🛍️ Fashion Trend Image Classifier")

# Sidebar model selection
st.sidebar.title("Select Model Version")
page = st.sidebar.radio(
    "Choose a model",
    ["CNN Classifier", "MobileNetV2 Classifier"],
    index=0
)

# Conditional model page loading
if page == "CNN Classifier":
    cnn_classifier_page()  # CNN version function
else:
    mobilenetv2_classifier_page()  # MobileNetV2 version function
