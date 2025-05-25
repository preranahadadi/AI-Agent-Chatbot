from dotenv import load_dotenv
import os
load_dotenv()

# Load keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # Set up LLM
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, api_key=OPENAI_API_KEY)
    else:
        raise ValueError("Unsupported provider")

    tools = [TavilySearchResults(max_results=2, api_key=TAVILY_API_KEY)] if allow_search else []

    # Create agent
    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    # Build message state
    messages = [SystemMessage(content=system_prompt)]
    messages += [HumanMessage(content=q) for q in query]

    state = {"messages": messages}

    response = agent.invoke(state)
    messages = response.get("messages", [])
    ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
    return ai_messages[-1] if ai_messages else "No AI response."
