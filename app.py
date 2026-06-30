import streamlit as st
from search import search_topic
from report import generate_report

# Page settings
st.set_page_config(
    page_title="Petal — AI Research Assistant",
    page_icon="🌸",
    layout="wide"
)

# Custom CSS for pastel peachy/lavender theme
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1625 0%, #211a2e 50%, #251a28 100%);
    }
    
    h1 {
        background: linear-gradient(90deg, #ff9eb5, #c9a7ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    .stMarkdown, p, label, span {
        color: #e8d9f0 !important;
    }
    
    .stTextInput input {
        border-radius: 20px;
        border: 2px solid #c9a7ff;
        padding: 12px 20px;
        background-color: #2a2238;
        color: #ffffff;
    }
    
    .stTextInput input::placeholder {
        color: #b39ddb;
        opacity: 0.7;
    }
    
    .stButton button {
        background: linear-gradient(90deg, #ff9eb5, #c9a7ff);
        color: white;
        border-radius: 30px;
        border: none;
        padding: 12px 30px;
        font-weight: 700;
        font-size: 16px;
        box-shadow: 0 4px 15px rgba(201, 167, 255, 0.4);
        transition: 0.3s;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(201, 167, 255, 0.6);
    }
    
    .stDownloadButton button {
        background: linear-gradient(90deg, #ffb6c1, #d8b4fe);
        color: #1a1625;
        border-radius: 30px;
        border: none;
        font-weight: 600;
    }
    
    h2, h3 {
        color: #ffb6c1 !important;
        border-bottom: 2px solid #c9a7ff;
        padding-bottom: 8px;
    }
    
    .stAlert {
        background-color: #2a2238;
        border-radius: 15px;
    }
    
    [data-testid="stSpinner"] {
        color: #c9a7ff;
    }
    
    code {
        background-color: #3a2e4f !important;
        color: #ffb6c1 !important;
    }
</style>
""", unsafe_allow_html=True)