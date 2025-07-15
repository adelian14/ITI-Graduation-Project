import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Configure genai with the API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def llm_model():
    # Load Gemini model
    model = genai.GenerativeModel(
        "gemini-2.5-flash", #"gemini-2.5-flash-preview-04-17"
        generation_config=genai.GenerationConfig(temperature=0.7)
    )
    return model