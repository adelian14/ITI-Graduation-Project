from crewai import Agent
from llm.llm_models import gemini_model
from crewai import Task

class RoadmapToJsonAgent:
    def get(self):
        return Agent(
            role="Roadmap JSON Converter",
            goal="Convert a raw course roadmap into a clean, structured JSON object with a logical hierarchy",
            backstory=(
                "You are an experienced data formatter and curriculum analyst. "
                "You understand how educational roadmaps are organized and can convert text into structured JSON. "
                "You're capable of inferring structure even when the original roadmap is loosely or inconsistently formatted."
            ),
            use_system_prompt=True,
            verbose=True, 
            llm=gemini_model
        )


def roadmap_to_json_task(raw_roadmap_text):
    return Task(
        description=f"""
            You are given a structured course roadmap as plain text:

            ---
            {raw_roadmap_text}
            ---

            Convert this roadmap into a **valid JSON object**.

            Instructions:
            - Only output the JSON object.
            - Do NOT include any extra text, comments, explanations, or markdown code blocks (e.g., no ```json).
            - The JSON must be clean, properly formatted, and directly usable by a parser.
            - Structure the roadmap using a hierarchy like:
              {{
                  "course_title": "...",
                  "description": "...",
                  "modules": [
                      {{
                          "title": "...",
                          "lessons": ["...", "..."]
                      }}
                  ]
              }}
        """,
        expected_output="Only a clean JSON object representing the course roadmap.",
        agent=RoadmapToJsonAgent().get(),
        output_file="app/agent_pipeline/data/outputs/roadmap_json_output.json"
    )

