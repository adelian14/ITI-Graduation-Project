from crewai import Agent, LLM
import os
from dotenv import load_dotenv
load_dotenv()

# Instantiate the LLM
os.environ["GEMINI_API_KEY"] = "AIzaSyAiGYmZq67r8iL8B7aE1J67eMbGjRd2Yng"
llm = LLM(
    model="gemini/gemini-2.0-flash" ,
    temperature=0.3, 
)