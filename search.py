import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load API keys from .env file
load_dotenv()

# Connect to Tavily using your API key
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_topic(topic):
    """Search the web for a given topic and return results"""
    
    print(f"Searching for: {topic}")
    
    # Search the web
    response = client.search(
        query=topic,
        search_depth="advanced",
        max_results=8
    )
    
    # Collect the results
    results = []
    for item in response["results"]:
        results.append({
            "title": item["title"],
            "content": item["content"],
            "url": item["url"]
        })
    
    return results

# Test
if __name__ == "__main__":
    results = search_topic("Artificial Intelligence")
    for r in results:
        print(r["title"])
        print(r["url"])
        print("---")