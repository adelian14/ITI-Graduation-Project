from crewai import Agent, LLM
from pipeline.llm_models.config import gemini_model

llm = gemini_model()

class RoadmapGenerationAgents:
    def __init__(self):
        """Initialize with a selected LLM provider and model"""
        self.llm = llm
        
    course_planner = Agent(
        role="Course Planner",
        goal="Generate module structure and learning objectives",
        backstory="An expert in instructional design for beginners",
        llm=llm,
        verbose=True
    )

    lesson_designer = Agent(
        role="Lesson Designer",
        goal="Design lessons for each module",
        backstory="An experienced educator with a focus on modular teaching",
        llm=llm,
        verbose=True
    )

    topic_generator = Agent(
        role="Topic Generator",
        goal="Generate detailed topics for each lesson",
        backstory="A curriculum writer specializing in beginner-level courses",
        llm=llm,
        verbose=True
    )

    formatter = Agent(
        role="Structure Formatter",
        goal="Format the roadmap into a clear hierarchy",
        backstory="A document expert who formats outlines into clean structures",
        llm=llm,
        verbose=True
    )