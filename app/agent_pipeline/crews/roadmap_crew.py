from crewai import Crew, Process
from agents.roadmap_designer_agent import build_roadmap_task, RoadmapDesignerAgent
from agents.roadmap_json_agent import roadmap_to_json_task, RoadmapToJsonAgent

class RoadmapCrew:
    def __init__(self, course_title, course_description, topic_list):
        self.course_title = course_title
        self.course_description = course_description
        self.topic_list = topic_list

    def get(self):
        # First task: generate roadmap
        roadmap_task = build_roadmap_task(
            self.course_title,
            self.course_description,
            self.topic_list
        )

        json_task = roadmap_to_json_task("{{ roadmap_task.output.raw }}")  # placeholder for auto-injection

        return Crew(
            agents=[
                roadmap_task.agent,
                json_task.agent
            ],
            tasks=[
                roadmap_task,
                json_task
            ],
            process=Process.sequential,
            verbose=True
        )
