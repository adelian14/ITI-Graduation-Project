from crew import Project_crew
import os
# Input parameters
folder_path = "/content/drive/MyDrive/Matrials"
course_name = "classical machine learning"
course_description = (
    "An introduction to core machine learning algorithms like regression, classification, "
    "and clustering, focusing on their concepts and practical applications."
)
topic = "linear regression"
age = "20-22" 
experience_level = "beginner"
language = "English"
teaching_style = "Motivational storytelling"
length = "Detailed explanation with example"
found = False

# Optional vector DB logic
saved_name = course_name + "vector"
found = os.path.exists(saved_name)

# Create and run the crew
crew = Project_crew(
    folder_path=folder_path,
    course_name=course_name,
    course_description=course_description,
    topic=topic,
    age=age,
    experience_level=experience_level,
    language=language,
    teaching_style=teaching_style,
    length=length,
    found=found,
    saved_name=saved_name
)

result = crew.run()

print(result)
