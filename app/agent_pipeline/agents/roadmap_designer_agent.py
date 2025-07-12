from crewai import Agent
from crewai import Task
from llm.llm_models import gemini_model

class RoadmapDesignerAgent:
    def get(self):
        return Agent(
            role="Course Roadmap Designer",
            goal=(
                "Design a logically structured and pedagogically sound course roadmap "
                "from a list of topics, a course title, and description."
            ),
            backstory=(
                "You are an expert instructional designer. "
                "You specialize in creating educational roadmaps that are progressive, comprehensive, "
                "and aligned with learning goals. You critically evaluate given topics, identify gaps, "
                "remove irrelevant ones, and add necessary missing topics based on your knowledge and the context."
            ),
            verbose=True,
            reasoning=True,
            use_system_prompt=True,
            llm=gemini_model
        )


def build_roadmap_task(course_title, course_description, topic_list):
    task_description = f"""
        You are given a course titled: "{course_title}"

        Description:
        "{course_description}"

        Preliminary list of topics:
        {topic_list}

        Your job is to:
        - Design a structured, logical course roadmap based on the title and description.
        - Determine which topics are useful and relevant.
        - Add any missing key topics.
        - Remove irrelevant or redundant ones.
        - Group and order them into a hierarchy (units, modules, lessons if appropriate).
    """

    return Task(
        description=task_description,
        expected_output="A structured, hierarchical roadmap in plain text or markdown.",
        agent=RoadmapDesignerAgent().get(),
        output_file="app/agent_pipeline/data/outputs/roadmap_output.txt"
    )
