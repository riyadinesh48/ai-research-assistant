from search import search_topic
from report import generate_report

def run_research(topic):
    """Main function that runs the full research pipeline"""
    
    print(f"\n🔍 Starting research on: {topic}")
    print("=" * 50)
    
    # Step 1: Search the web
    print("\n📡 Step 1: Searching the web...")
    results = search_topic(topic)
    print(f"✅ Found {len(results)} sources!")
    
    # Step 2: Generate report
    print("\n🤖 Step 2: AI is generating your report...")
    report = generate_report(topic, results)
    print("✅ Report generated!")
    
    # Step 3: Save report to file
    filename = f"{topic.replace(' ', '_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\n💾 Report saved as: {filename}")
    
    return report

# Run it
if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    report = run_research(topic)
    print("\n" + "=" * 50)
    print(report)