from crewai import LLM

def gemini_model(temp = 0.7):
    return LLM(
        model="gemini/gemini-2.5-flash",
        temperature=temp,
    )