from crewai import Agent, LLM
from utils.base_model import llm

class Project_agents:
    def __init__(self):
        """Initialize with a selected LLM provider and model"""
        self.llm = llm
    
    def topics_agents(self, topic: str):
        return Agent(
            role="Curriculum Designer",
            goal=f"Generate a list of essential subtopics someone must learn to master the topic: '{topic}'.",
            backstory=(
                f"You are a senior curriculum designer with 15+ years of experience in structuring learning paths. "
                f"Your current assignment is to break down the topic '{topic}' into logical and essential subtopics. "
                f"You focus on clarity, completeness, and educational progression to help learners master the subject."
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
    )


    def context_retriever_agent(self):
        return Agent(
            role="Document Search Assistant",
            goal="Find and return relevant text chunks for each topic from a document store.",
            backstory=(
                "You specialize in retrieving relevant information for educational purposes. "
                "When given a topic, you search a document database and return the most relevant text chunks "
                "to support curriculum generation and slide creation."
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
    )

    def course_content_builder_agent(self):
        return Agent(
            role="Course Content Architect",
            goal="Generate a professional course slide deck organized into sessions using combined topic text.",
            backstory=(
                "You are an advanced AI course designer. Your job is to turn combined topic content into structured, well-organized, "
                "session-based presentations. You understand pacing, flow, and instructional slide design."
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
    )




    



