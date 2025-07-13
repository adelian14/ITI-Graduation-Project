from crewai import Crew, Process
import json
from agents import Project_agents
from tasks import ProjectTasks
from Prompts import narrative_prompt, customize_prompt  # Make sure these are imported

class Project_crew:
    def __init__(self, folder_path, course_name, course_description, topic, age,
                 experience_level, language, teaching_style, length, found,saved_name):
        self.agents = Project_agents()
        self.tasks = ProjectTasks()
        
        # Assign parameters
        self.folder_path = folder_path
        self.course_name = course_name
        self.course_description = course_description
        self.topic = topic
        self.age = age
        self.experience_level = experience_level
        self.language = language
        self.teaching_style = teaching_style
        self.length = length
        self.found = found
        self.saved_name=saved_name

    def create_crew(self):
        # Define agents
        content_creator = self.agents.context_retriever_agent()
        lesson_creator = self.agents.lesson_agent()
        summary_creator=self.agents.summary_agent()
        json_creator = self.agents.json_agent()
        pptx_creator = self.agents.pptx_generation_agent()
        narrative_creator = self.agents.narrative_agent()
        customize_creator = self.agents.customize_agent()

        # Define tasks
        content_retriever_task = self.tasks.retrieve_combined_context_task(
            agent=content_creator,
            course_name=self.course_name,
            course_description=self.course_description,
            found=self.found,
            folder_path=self.folder_path,
            topic=self.topic,
            saved_name=self.saved_name
        )

        lesson_task = self.tasks.lesson_task(
            agent=lesson_creator,
            context=content_retriever_task.output
        )

        summary_task = self.tasks.summary_task(
            agent=summary_creator,
            context=lesson_task.output
        )

        json_task = self.tasks.json_task(
            agent=json_creator,
            age=self.age,
            experience_level=self.experience_level,
            context=summary_task.output
        )

        pptx_task = self.tasks.pptx_task(
            agent=pptx_creator,
            context=json_task.output
        )

        narrative_task = self.tasks.narrative_task(lesson_task,self.course_name, self.course_description,
                                pptx_task, self.age, self.teaching_style, self.language, narrative_creator, narrative_prompt)

        customize_task = self.tasks.customize_task(
            narrative_task, customize_creator, customize_prompt,self.teaching_style,self.language,self.length)




        # Create crew
        return Crew(
            agents=[content_creator,lesson_creator,summary_creator,json_creator, pptx_creator,
                narrative_creator, customize_creator],
          tasks=[content_retriever_task,lesson_task,summary_task,json_task,pptx_task,
               narrative_task, customize_task],
          process=Process.sequential,
          verbose=False
        )

    def run(self):
        crew = self.create_crew()
        result = crew.kickoff()
        return result
