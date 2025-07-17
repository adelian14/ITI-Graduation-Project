# tools/gemini_vision_tool.py
from crewai.tools import BaseTool
import google.generativeai as genai
from PIL import Image
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

class OCRTool(BaseTool):
    name: str = "gemini_vision_tool"
    description: str = "Extracts text and structure from an image using Gemini 2.5 Flash multimodal."

    def _run(self, image_path: str, prompt: str = "Extract all readable content from this image") -> str:
        try:
            img = Image.open(image_path)
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content([prompt, img])
            return response.text
        except Exception as e:
            return f"Failed to process image: {e}"
