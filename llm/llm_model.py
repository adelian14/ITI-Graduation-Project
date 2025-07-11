from crewai import LLM

gemini_model = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.7,
)

ollama_model = LLM(
    model = "ollama/llama3.1",
    base_url = "http://localhost:11434/api/generate",
    temperature=0.7,
)
