from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    """
    Returns a Groq LLM client configured with environment variables.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing in environment variables.")
    
    return ChatGroq(
        temperature=0.1,
        model="mixtral-8x7b-32768",  # You can replace this with another Groq model
        groq_api_key=api_key
    )
