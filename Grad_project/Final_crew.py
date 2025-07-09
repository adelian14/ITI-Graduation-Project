from crewai import Crew, Process
from agents import Project_agents
from tasks import ProjectTasks
from utils.Vector_store import create_vector_store
from utils.load_document import load_documents
from utils.Split_data import split_by_chunk_size


num_weeks=4
sessions_per_week=2
topic="classical machine learning"
folder_path = "data"
documents, candidate_names = load_documents(folder_path)
chunks=split_by_chunk_size(documents)
vector_store = create_vector_store(chunks)

class Project_crew:
    def __init__(self):
        self.agents = Project_agents()
        self.tasks = ProjectTasks()
    def create_crew(self):
        Topic_creator = self.agents.topics_agents(topic)
        retriever_agent=self.agents.context_retriever_agent()
        course_agent=self.agents.course_content_builder_agent()
        
        topics_task=self.tasks.extract_main_topics(Topic_creator)
        context_retriever_task=self.tasks.retrieve_combined_context_task(
            retriever_agent,vector_store,[topics_task])
        
        course_ppt_task=self.tasks.build_full_course_ppt_task(
          course_agent,dict(context_retriever_task),num_weeks,sessions_per_week)
        
        return Crew(
                agents=[Topic_creator,retriever_agent,course_agent],
                tasks=[topics_task,context_retriever_task,course_ppt_task],
                process=Process.sequential,
                verbose=False
            )
    
    def run(self):
        crew = self.create_crew()
        result = crew.kickoff()
        return result


