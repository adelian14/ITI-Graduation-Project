from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()
# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

def gemini_model(temp = 0.7):
    return LLM(
        model="gemini/gemini-2.5-flash",
        temperature=temp,
    )