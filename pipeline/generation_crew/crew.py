from crewai import Agent
from crewai import Crew
from crewai import Task
from pipeline.llm_models.config import gemini_model

lesson_writer_agent = Agent(
    role="Expert Educational Content Developer & Instructional Designer",
    goal=(
        "Create comprehensive, engaging, and pedagogically sound educational lessons "
        "that maximize learning outcomes through evidence-based instructional design, "
        "adaptive content delivery, and learner-centered approaches."
    ),
    backstory=(
        "You are a seasoned educational content developer with a Ph.D. in Educational Psychology "
        "and 15+ years of experience in curriculum design, instructional methodology, and adult learning. "
        "You specialize in creating content that accommodates different learning styles, incorporates "
        "cognitive load theory, and follows proven pedagogical frameworks like Bloom's Taxonomy and "
        "Gagne's Nine Events of Instruction. You understand how to scaffold learning, create meaningful "
        "assessments, and design content that promotes deep understanding rather than surface learning."
    ),
    verbose=True,
    llm = gemini_model()
)

def create_lesson_generation_task(full_context: dict) -> Task:
    lesson_data = full_context["data"]
    setting = full_context["setting"]
    
    title = lesson_data["title"]
    summary = f"Lesson Brief Summary (description): {lesson_data['summary']}\n\n"
    topics = lesson_data.get("covered_topics",None)

    setting_str = (
        f"Audience: {setting['ageGroup']}, "
        f"Experience Level: {setting['experienceLevel']}, "
        f"Language: {setting['narrativeLanguage']}"
    )
    if topics:
        topics_str = "\n\n".join(
            f"{i+1}. {topic['title']}\n{topic['content']}" for i, topic in enumerate(topics)
        )
        topics_str = f"Topics:\n{topics_str}\n\n"
    else:
        topics_str = ""

    full_prompt = (
        f"You are generating a structured, objective lesson based on the following inputs.\n\n"
        f"Lesson Title: {title}\n"
        f"{summary}"
        f"{setting_str}\n\n"
        f"{topics_str}"
        f"Write a complete lesson that:\n"
        f"- Starts with an introduction.\n"
        f"- Has a separate section for each topic.\n"
        f"- Uses clear, informative, and objective language.\n"
        f"- Ends with a summary or conclusion.\n"
        f"Return only the final lesson text."
    )

    # Return the task
    return Task(
        description=full_prompt,
        expected_output="A complete lesson text written in raw, structured, objective form.",
        agent=lesson_writer_agent
    )


def build_lesson_generation_crew(lesson_object: dict) -> Crew:
    lesson_task = create_lesson_generation_task(lesson_object)

    crew = Crew(
        agents=[lesson_writer_agent],
        tasks=[lesson_task],
        verbose=True
    )

    return crew


