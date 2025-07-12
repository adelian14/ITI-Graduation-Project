from crews.roadmap_crew import RoadmapCrew
from utils.json_utils import dump_clean_json

course_title = "Intro to Machine Learning with Python"
course_description = "Foundations of machine learning including concepts, techniques, and Python implementation."
topics = [
    "Supervised Learning", "Unsupervised Learning", "Model Evaluation",
    "Linear Regression", "Overfitting", "Decision Trees", "Scikit-learn"
]

crew = RoadmapCrew(course_title, course_description, topics).get()
crew.kickoff()


# Read and clean the raw output
with open("app/agent_pipeline/data/outputs/roadmap_json_output.txt", "r", encoding="utf-8") as f:
    raw_output = f.read()

try:
    cleaned_path = dump_clean_json(raw_output, "app/agent_pipeline/data/outputs/roadmap_json_output_cleaned.json")
    print(f"✅ Cleaned JSON saved to: {cleaned_path}")
except ValueError as e:
    print("❌ Failed to extract valid JSON:", e)

