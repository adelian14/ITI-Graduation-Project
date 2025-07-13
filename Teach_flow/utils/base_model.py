from crewai import Agent, LLM
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key="AIzaSyATVonQ3KEbyC6tRt-UF1d6g18HPwcjXAk",
    temperature=0.3,
)