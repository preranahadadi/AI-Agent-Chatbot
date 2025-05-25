# AI Agent Chatbot

A smart, customizable AI chatbot built using FastAPI, LangChain, LangGraph, and Streamlit. Supports models from OpenAI and Groq, with optional web search using Tavily.

---

## Features

- Choose between OpenAI (gpt-4o-mini) and Groq (llama3-70b, mixtral-8x7b)
- Customize the system prompt to define your AI agent's behavior
- Optional real-time web search using Tavily
- Clean Streamlit UI frontend
- FastAPI backend using LangGraph ReAct agent logic

---

## Tech Stack

- Frontend: Streamlit
- Backend: FastAPI
- LLM Providers: OpenAI, Groq
- Search Tool: Tavily
- Agent Framework: LangGraph + LangChain
- Language: Python

---

## Getting Started

### 1. Clone the repo

git clone https://github.com/preranahadadi/AI-Agent-Chatbot.git
cd AI-Agent-Chatbot

---

### 2. Install dependencies

If using Pipenv:

pipenv install
pipenv shell

Or with pip:

pip install -r requirements.txt

---

### 3. Setup environment variables

Create a .env file in the root directory and paste your keys:

OPENAI_API_KEY=your-openai-key  
GROQ_API_KEY=your-groq-key  
TAVILY_API_KEY=your-tavily-key

Ensure `.env` is included in your `.gitignore`.

---

### 4. Run the backend

uvicorn backend:app --reload --port 9999

---

### 5. Run the frontend

streamlit run frontend.py

Then open your browser to:

http://localhost:8501

---

## UI Preview

Here’s what the chatbot UI looks like:

![UI Preview](ui-preview.png)

---

## Example Payload Sent to Backend

{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as a helpful AI assistant.",
  "messages": ["What are the latest trends in AI?"],
  "allow_search": true
}

---

## Project Structure

├── ai_agent.py         # Agent logic using LangGraph  
├── backend.py          # FastAPI backend  
├── frontend.py         # Streamlit UI  
├── ui-preview.png      # Screenshot of the app  
├── .env                # API keys (not committed)  
├── .gitignore  
└── README.md

