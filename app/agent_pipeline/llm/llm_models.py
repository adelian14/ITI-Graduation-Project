from crewai import LLM

gemini_model = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.7,
)

