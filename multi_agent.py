import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from ddgs import DDGS

load_dotenv()

llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")

# Agent 1 - Research Agent
def research_agent(topic):
    print("🔍 Research Agent: Searching the web...", flush=True)
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(topic, max_results=6))
            output = ""
            for r in results:
                output += f"Title: {r['title']}\nSummary: {r['body']}\n\n"
            
            # Agent summarizes research
            prompt = f"Summarize these search results about '{topic}' into key facts and insights:\n\n{output}"
            summary = llm.invoke(prompt).content
            print("✅ Research Agent: Done!", flush=True)
            return summary
    except Exception as e:
        return f"Research failed: {e}"

# Agent 2 - Writer Agent
def writer_agent(topic, research):
    print("✍️ Writer Agent: Writing content...", flush=True)
    prompt = f"""
You are a professional content writer.
Write a comprehensive, engaging article about: {topic}

Use this research:
{research}

Structure:
- Catchy headline
- Introduction
- 3 main sections with subheadings
- Conclusion
- 500-700 words
"""
    content = llm.invoke(prompt).content
    print("✅ Writer Agent: Done!", flush=True)
    return content

# Agent 3 - Reviewer Agent
def reviewer_agent(content, topic):
    print("🔎 Reviewer Agent: Reviewing and improving...", flush=True)
    prompt = f"""
You are an expert editor. Review this article about '{topic}' and improve it.

Original article:
{content}

Your tasks:
1. Fix any factual issues
2. Improve clarity and flow
3. Make the headline more catchy
4. Add a key takeaway at the end
5. Return the fully improved version
"""
    improved = llm.invoke(prompt).content
    print("✅ Reviewer Agent: Done!", flush=True)
    return improved

# Coordinator - manages all agents
def coordinator(topic):
    print(f"\n🤖 MULTI-AGENT SYSTEM ACTIVATED")
    print(f"📋 Task: Create article about '{topic}'")
    print("="*50)
    
    # Step 1: Research Agent
    research = research_agent(topic)
    
    # Step 2: Writer Agent uses research
    draft = writer_agent(topic, research)
    
    # Step 3: Reviewer Agent improves draft
    final = reviewer_agent(draft, topic)
    
    # Save final output
    with open("final_article.md", "w") as f:
        f.write(f"# Topic: {topic}\n\n")
        f.write(final)
    
    print("="*50)
    print("✅ All agents completed their tasks!")
    print("💾 Final article saved as final_article.md")
    return final

# Main
print("\n✅ Multi-Agent System Ready!")
print("3 agents will collaborate: Researcher → Writer → Reviewer\n")

topic = input("Enter a topic: ")
result = coordinator(topic)

print("\n--- FINAL ARTICLE PREVIEW ---\n")
print(result[:600])
print("\n... (full article saved in final_article.md)")