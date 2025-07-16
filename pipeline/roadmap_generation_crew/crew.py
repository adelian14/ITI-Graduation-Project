from crewai import Crew, Process
from pipeline.roadmap_generation_crew.agents import RoadmapGenerationAgents
from pipeline.roadmap_generation_crew.tasks import RoadmapGenerationTasks

class RoadmapGenerationCrew:
    def __init__(self):
        self.agents = RoadmapGenerationAgents()
        self.tasks = RoadmapGenerationTasks()
    
    def create_crew(self, input_data):
        # Initialize all agents
        course_planner = self.agents.course_planner
        lesson_designer = self.agents.lesson_designer
        topic_generator = self.agents.topic_generator
        formatter = self.agents.formatter

        # Create tasks with dependencies
        module_task = self.tasks.course_planner(course_planner, input_data)
        lesson_task = self.tasks.lesson_designer(lesson_designer)
        topic_task = self.tasks.topic_generator(topic_generator)
        format_task = self.tasks.json_formatter(formatter)

        # Create and return crew
        return Crew(
            agents=[course_planner, lesson_designer, topic_generator, formatter],
            tasks=[module_task, lesson_task, topic_task, format_task],
            process=Process.sequential,
            verbose=True
        )
    
    def run(self, input_data):
        crew = self.create_crew(input_data)
        result = crew.kickoff()
        return result
