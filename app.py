import streamlit as st
from search import search_topic
from report import generate_report

# Page settings
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔬",
    layout="wide"
)

# Title
st.title("🔬 AI Research Assistant")
st.subheader("Enter any topic and get a comprehensive research report!")

# Input box
topic = st.text_input("Enter a research topic:", placeholder="e.g. Artificial Intelligence, Climate Change, Quantum Computing")

# Button
if st.button("Generate Report 🚀"):
    
    if topic.strip() == "":
        st.warning("Please enter a topic first!")
    
    else:
        # Search the web
        with st.spinner("🔍 Searching the web..."):
            results = search_topic(topic)
        
        st.success(f"Found {len(results)} sources!")
        
        # Generate report
        with st.spinner("🤖 AI is writing your report..."):
            report = generate_report(topic, results)
        
        # Show the report
        st.markdown("---")
        st.markdown(report)
        
        # Download button
        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name=f"{topic}_report.txt",
            mime="text/plain"
        )