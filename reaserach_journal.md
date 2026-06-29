# Research Journal — AI Research Assistant

## 1. How I Approached the Problem

When I first read the assignment, I broke it down into simple parts:
- Something needs to search the internet
- Something needs to summarize the results
- Something needs to show it to the user

I decided to build it step by step rather than all at once.

## 2. Technologies I Researched

### Tavily API
I researched Tavily as a web search tool built specifically for AI apps.
It returns clean, structured results which made it easy to pass to an AI model.

### Groq API
I initially tried Anthropic Claude API but it required paid credits.
I then researched free alternatives and found Groq, which provides
free access to LLaMA 3 — a powerful open source AI model.

### Streamlit
I researched Streamlit as a way to build web interfaces using only Python.
It was perfect since I didn't need to learn HTML or JavaScript.

## 3. Why I Chose This Approach

| Decision | Reason |
|---|---|
| Python | Most comfortable language |
| Groq over Anthropic | Free tier available |
| Tavily over Google Search API | Built for AI, easier to use |
| Streamlit over Flask | Much simpler for quick UI |

## 4. Challenges I Encountered

### Challenge 1 — Anthropic API Cost
Claude API required paid credits. I solved this by switching to
Groq which offers free access to LLaMA 3 model.

### Challenge 2 — Deprecated Model
The llama3-70b-8192 model was decommissioned. I solved this by
updating to llama-3.3-70b-versatile which is the current model.

### Challenge 3 — File Location
Initially my Python files were saved inside the venv folder instead
of the project root. I fixed this by recreating them in the correct location.

## 5. AI Tools I Used
- Claude AI (claude.ai) — for guidance, code help, and debugging
- Groq LLaMA 3 — as the AI brain inside my application

## 6. How I Verified AI Generated Code
- I ran every piece of code immediately after writing it
- I tested with real topics like "Artificial Intelligence" and "Cloud Computing"
- I fixed errors as they appeared and understood what each fix did

## 7. What I Learned

- How to use APIs to connect different services together
- How to build a web app using only Python
- How to handle API errors and find free alternatives
- How the full pipeline of an AI application works:
  Search → Process → Generate → Display
- The importance of virtual environments
- How to read and understand error messages