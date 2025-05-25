from dotenv import load_dotenv
import os

# Print current working directory
print("Working directory:", os.getcwd())

# Load environment variables from .env
load_dotenv()

# Print whether .env exists
print(".env found:", os.path.exists(".env"))

# Print loaded API keys
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
print("TAVILY_API_KEY:", os.getenv("TAVILY_API_KEY"))
