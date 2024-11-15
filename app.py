import streamlit as st 
from cnn_page import cnn_classifier_page
from mobilenetv2_page import mobilenetv2_classifier_page

# Set page configuration
st.set_page_config(
    page_title="Fashion Trend Classifier",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for vibrant design
st.markdown("""
    <style>
        /* App background and font style */
        .stApp {
            background: linear-gradient(to bottom, #fff5f5, #ffe6e6);
            color: #333333;
            font-family: 'Helvetica Neue', sans-serif;
        }

        /* Header customization */
        header, footer {visibility: hidden;}
        .main-header {
            text-align: center;
            font-size: 3rem;
            font-weight: bold;
            color: #ff6f61;
            margin: 1rem 0;
            text-shadow: 2px 2px 2px #ffcccc;
        }

        /* Sidebar styling */
        .css-1lcbmhc {
            background: linear-gradient(to bottom, #ffebeb, #ffe6e6);
            color: #333333;
            font-weight: bold;
        }

        /* Customizing the radio button */
        .stRadio > label {
            font-size: 1.1rem;
            color: #ff6f61;
        }
        .stRadio div {
            gap: 10px;
        }

        /* Styling buttons */
        .stButton > button {
            background: linear-gradient(to right, #ff6f61, #ff847c);
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 16px;
            font-size: 1rem;
            box-shadow: 2px 2px 5px #ff9999;
        }
        .stButton > button:hover {
            background: linear-gradient(to right, #ff847c, #ff6f61);
        }

        /* Styling the title */
        .css-10trblm {
            color: #ff6f61 !important;
        }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown("<div class='main-header'>🛍️ Fashion Trend Image Classifier</div>", unsafe_allow_html=True)

# Sidebar for model selection
st.sidebar.title("Model Selection")
st.sidebar.markdown("Choose a model to classify your fashion images:")
page = st.sidebar.radio(
    "Model Versions",
    ["CNN Classifier", "MobileNetV2 Classifier"],
    index=0
)

# Load the selected model page
if page == "CNN Classifier":
    cnn_classifier_page()  # CNN version function
else:
    mobilenetv2_classifier_page()  # MobileNetV2 version function
