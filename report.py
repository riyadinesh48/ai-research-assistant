import os
from groq import Groq
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Connect to Groq (Free AI)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_report(topic, search_results):
    """Send search results to Groq AI and get a research report"""
    
    # Prepare the search results as text
    sources_text = ""
    for i, result in enumerate(search_results, 1):
        sources_text += f"""
Source {i}: {result['title']}
URL: {result['url']}
Content: {result['content']}
---
"""

    # Ask AI to write the report
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=4000,
        messages=[
            {
                "role": "user",
                "content": f"""You are a research assistant. Based on the sources below, 
write a comprehensive research report on: {topic}

{sources_text}

Your report MUST include these sections:

# Research Report: {topic}

## Executive Summary
(2-3 paragraph overview)

## Key Findings
(Most important discoveries - use bullet points)

## Important Trends
(What patterns are emerging)

## Interesting Insights
(Surprising or notable information)

## Recommended Resources
(Best sources to learn more)

## References
(List all URLs used)

Write in a clear, professional style."""
            }
        ]
    )
    
    return response.choices[0].message.content

# Test
if __name__ == "__main__":
    from search import search_topic
    
    print("Searching the web...")
    results = search_topic("Artificial Intelligence")
    
    print("Generating report with AI...")
    report = generate_report("Artificial Intelligence", results)
    
    print(report)