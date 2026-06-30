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
        background: linear-gradient(135deg, #fff0f5 0%, #f3e8ff 50%, #ffe4ec 100%);
    }
    
    h1 {
        background: linear-gradient(90deg, #ff9eb5, #c9a7ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    .stTextInput input {
        border-radius: 20px;
        border: 2px solid #f8c8dc;
        padding: 12px 20px;
        background-color: #fff;
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
        color: white;
        border-radius: 30px;
        border: none;
        font-weight: 600;
    }
    
    h2 {
        color: #c084a3;
        border-bottom: 3px solid #f8c8dc;
        padding-bottom: 8px;
    }
    
    .stMarkdown {
        font-family: 'Trebuchet MS', sans-serif;
    }
    
    [data-testid="stSpinner"] {
        color: #c9a7ff;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🌸 Petal — AI Research Assistant")
st.markdown("##### ✨ Drop a topic, get the tea — instant research, zero effort")

st.write("")

# Input box
topic = st.text_input("", placeholder="✍️ e.g. AI Agents, Climate Change, K-pop industry...")

# Button
if st.button("Generate Report ✨🚀"):
    
    if topic.strip() == "":
        st.warning("babe you forgot to type a topic 👀")
    
    else:
        # Search the web
        with st.spinner("🔍 stalking the internet for you..."):
            results = search_topic(topic)
        
        st.success(f"💅 found {len(results)} solid sources!")
        
        # Generate report
        with st.spinner("🧠 AI is cooking your report..."):
            report = generate_report(topic, results)
        
        # Show the report
        st.markdown("---")
        st.markdown(report)
        
        # Download button
        st.download_button(
            label="📥 save this report bestie",
            data=report,
            file_name=f"{topic}_report.txt",
            mime="text/plain"
        )