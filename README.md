# Multi-Agent System

3 AI agents collaborating to research, write and review content automatically.

## Agents
- **Research Agent** — searches web and summarizes findings
- **Writer Agent** — writes article using research
- **Reviewer Agent** — reviews and improves the draft

## How it works
1. You give a topic
2. Research Agent searches web for latest info
3. Writer Agent creates a full article
4. Reviewer Agent improves and polishes it
5. Final article saved as markdown

## Tech Stack
- Python
- LangChain
- Groq API (Llama 3)
- DuckDuckGo Search

## Setup
1. Clone the repo
2. Install: `pip install langchain langchain-groq ddgs python-dotenv`
3. Add Groq API key in `.env`
4. Run: `python multi_agent.py`
