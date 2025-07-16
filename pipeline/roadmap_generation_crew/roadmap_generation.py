import json
from pipeline.roadmap_generation_crew.crew import RoadmapGenerationCrew

def cleaned_json_str(result):
    #  Get the raw output (remove the ```json ... ``` wrapper)
    raw_output = result.raw.strip()

    # Step 2: Clean the string (remove the markdown-like wrappers)
    if raw_output.startswith("```json"):
        cleaned_json_str = raw_output.replace("```json", "").replace("```", "").strip()
    else:
        cleaned_json_str = raw_output.strip()

    # Step 3: Convert to JSON
    try:
        structured_data = json.loads(cleaned_json_str)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        structured_data = None

    return structured_data


def generate_roadmap(input_data):
    crew = RoadmapGenerationCrew()
    result = crew.run(input_data)

    structured_data = cleaned_json_str(result)
    return structured_data


