from crewai import Crew, Process
from pipeline.slides_generation_crew.agents import SlidesGenerationAgents
from pipeline.slides_generation_crew.tasks import SlidesGenerationTasks
from pipeline.llm_models.config import gemini_model

llm = gemini_model()

class NarrativeGenerationCrew:
    def __init__(self):
        self.agents = SlidesGenerationAgents()
        self.tasks = SlidesGenerationTasks()

    
    def create_crew(self, data):
        # Initialize all agents
        summarizer_agent = self.agents.summarizer_agent(llm)
        slide_designer_agent = self.agents.slide_designer_agent(llm)
        json_creator_agent = self.agents.json_creator_agent(llm)

        # Create tasks with dependencies
        summarize_task = self.tasks.summarize_task(summarizer_agent, data)
        design_task = self.tasks.design_task(slide_designer_agent)
        json_task = self.tasks.json_task(json_creator_agent)


        # Create and return crew
        return Crew(
            agents=[summarizer_agent, slide_designer_agent, json_creator_agent],
            tasks=[summarize_task, design_task, json_task],
            process=Process.sequential,
            verbose=True,
        )
    
    def run(self, data):
        crew = self.create_crew(llm, data)
        result_json = crew.kickoff()




