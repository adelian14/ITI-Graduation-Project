from crewai import Task
from tqdm import tqdm
#from reportlab.lib.pagesizes import A4
#from reportlab.pdfgen import canvas
from Prompts import narrative_prompt,customize_prompt
from utils.Save_vector import get_vector_store

class ProjectTasks:

  def retrieve_combined_context_task(self, agent, course_name, course_description, found, folder_path,topic,saved_name,k=30):
    """
    Retrieves context from the vector store relevant to a specific topic/lesson/chapter.

    Args:
        agent: The LLM agent to handle the task.
        course_name: The overall name of the course.
        course_description: A general description of the course.
        found: Data required to build the vector store.
        folder_path: Path to the vector store or documents.
        query: Specific topic, lesson, or chapter to retrieve context for.
        k: Number of most similar documents to retrieve.

    Returns:
        A Task object with context relevant to the specific query.
    """
    # Build the vector store
    vector_store = get_vector_store(folder_path, found, course_name,saved_name)

    # Search based on specific topic/chapter/lesson
    relevant_docs = vector_store.similarity_search(topic, k=k)

    # Combine document content
    combined_context = "\n\n".join([doc.page_content for doc in relevant_docs])

    # Return a task with detailed instructions and context
    return Task(
        description=(
            f"You are given content from the course '{course_name}'.\n\n"
            f"Course Description: {course_description}\n\n"
            f"Your task is to focus specifically on the topic: '{topic}' and extract or summarize relevant information.\n\n"
            f"Context:\n{combined_context}"
        ),
        agent=agent,
        expected_output=f"A summary, explanation, or response focused on: '{topic}'."
    )

  def lesson_task(self, agent, context):
    return Task(
        agent=agent,
        description=(
            "You will receive unstructured context consisting of multiple paragraphs. "
            "Your job is to convert this content into a clear, structured lesson using headers and mini-paragraphs. "
            "Ensure the final output is easy to follow, educational, and formatted with headers (`##`) and subheaders (`###`) where appropriate."
        ),
        expected_output=(
            "A structured lesson in markdown format with clearly defined headers and short, informative paragraphs. "
            "The content should retain the original meaning but be organized for clarity and better understanding."
        ),
        input=context
    )

  def summary_task(self, agent, context):
    return Task(
        agent=agent,
        description=(
            "You will be given detailed content that may span multiple paragraphs. "
            "Your task is to create a well-written, concise summary that accurately reflects all key ideas, arguments, and important information "
            "present in the original content without losing meaning or depth."
        ),
        expected_output=(
            "A concise, clear summary that retains all essential information, key points, and terminology from the original context. "
            "Avoid omitting important details. Use short paragraphs or bullet points if needed for readability."
        ),
        input=context
    )

  
  def json_task(self, agent, age, experience_level,context):

    return Task(
        description=(
            f"You are tasked with converting the provided course context into a structured JSON format, ready for presentation slides.\n\n"
            f"🎯 Target Audience:\n"
            f"- Age Group: {age}\n"
            f"- Experience Level: {experience_level}\n\n"
            f"📋 Instructions:\n"
            f"1. Analyze and understand the provided course material thoroughly.\n"
            f"2. Identify major **topics or chapters** based on the flow of the content.\n"
            f"3. Break down each topic into **sessions** (or subtopics).\n"
            f"4. Summarize the content of each session using **bullet points**.\n"
            f"5. Adapt the tone and depth of content to match the **target audience**:\n"
            f"   - Use engaging, simple, and example-rich language for younger or beginner users.\n"
            f"   - Use technical and detailed language for experienced or advanced learners.\n\n"
            f"6. Return the output in the following **strict JSON format**:\n\n"
            "{\n"
            "  \"course_title\": \"...\",\n"
            "  \"topics\": [\n"
            "    {\n"
            "      \"topic_title\": \"...\",\n"
            "      \"sessions\": [\n"
            "        {\n"
            "          \"session_title\": \"...\",\n"
            "          \"content\": [\n"
            "            \"Bullet point 1\",\n"
            "            \"Bullet point 2\",\n"
            "            \"...\"\n"
            "          ]\n"
            "        }\n"
            "      ]\n"
            "    }\n"
            "  ]\n"
            "}\n\n"
            f"⚠️ Ensure the JSON is clean, coherent, and free of missing or redundant information."
        ),
        agent=agent,
        expected_output=(
            "A JSON file that clearly organizes the course into topics and bullet-point sessions, "
            "tailored to the specified age and experience level. Ready to be used in slide generation."
        ),
        input=context
    )

  def pptx_task(self, agent, context):
    return Task(
        description=(
            "Take the JSON output from the previous step and generate a PowerPoint presentation. "
            "Include a title slide with the course name and audience info, then one slide per session with session titles and content."
        ),
        agent=agent,
        expected_output="A PowerPoint file named 'course_presentation.pptx'.",
        input=context  # or explicitly input_from if your system requires
    )

  def narrative_task(self,content_task, course_name, course_description, presentation_task, age, teaching_style, language, narrative_agent, narrative_prompt):
    return Task(
        agent=narrative_agent,
        description=narrative_prompt.format(
            content=content_task.output,
            course_title=course_name,
            course_desc=course_description,
            presentation=presentation_task.output,
            audience_age=age,
            teaching_style=teaching_style,
            language=language
        ),
        expected_output="Narrative text explaining the topic clearly in English."
    )

  def customize_task(self,narrative_task, customize_agent, customize_prompt,teaching_style,language,length):
    return Task(
        agent=customize_agent,
        description=customize_prompt.format(
            narrative=narrative_task.output,
            style=teaching_style,
            language=language,
            length=length
        ),
        expected_output="Customized narrative text matching style and length and saved to 'narrative.html' ",
        output_file="narrative.html"
    )

