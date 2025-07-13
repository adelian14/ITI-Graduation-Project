from crewai import Agent, LLM
from pptx import Presentation
from pptx.util import Inches, Pt
from utils.base_model import llm
from tools import generate_pptx_from_json
class Project_agents:
    def __init__(self):
        """Initialize with a selected LLM provider and model"""
        self.llm = llm

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
    def lesson_agent(self):

      return Agent(
        role="Lesson Structuring Expert",
        goal="Convert unstructured context into a well-organized lesson format with headers and supporting mini-paragraphs.",
        backstory=(
            "You are an educational content designer with expertise in organizing textual content into digestible, structured lesson formats. "
            "You specialize in taking raw or unorganized information and turning it into easy-to-follow lessons, suitable for learners of all ages."
        ),
        verbose=True,
        allow_delegation=False,
        llm=self.llm,
        instructions=(
            "You will be given a large amount of context, usually in the form of raw or messy paragraphs. "
            "Your task is to break down the content into a clean, structured lesson format. "
            "Use headers to separate sections or main ideas. Under each header, write short, clear, and focused paragraphs (2–4 sentences each) "
            "that explain the concept or topic. Use bullet points or numbered lists when necessary. Ensure a logical flow between sections. "
            "Do not invent new information. Do not summarize. Simply restructure the original content for clarity and learning purposes. "
            "Use markdown-style formatting with `##` for main headers and `###` for subheaders if needed."
        )
    )

    def summary_agent(self):
      return Agent(
        role="Expert Summarizer and Context Preserver",
        goal="Summarize long content into a concise version without losing key information or meaning.",
        backstory=(
            "You are an expert in summarization with a deep understanding of language and context. "
            "You excel at analyzing long-form content and distilling it into shorter versions that keep all essential points, insights, and terminology intact. "
            "Your summaries never skip critical technical, conceptual, or contextual details."
        ),
        verbose=True,
        allow_delegation=False,
        llm=self.llm,
        instructions=(
            "You will receive long-form content. Your task is to summarize it into a shorter version while preserving all core ideas, essential information, "
            "and original intent. Avoid vague generalizations or oversimplifying. Ensure all technical or domain-specific terminology is retained and accurately represented. "
            "Use clear and precise language. Break the summary into short paragraphs if needed for readability. Do not omit anything critical. "
            "If something is repeated or redundant in the source, you may remove that repetition, but never remove unique or insightful points."
        )
    )

      
    def json_agent(self):

      return Agent(
        role="Course Structuring and Summarization Agent",
        goal=(
            "Analyze the course content, summarize it accurately without missing key information, "
            "organize it into well-defined topics and subtopics, and output it in a structured JSON format "
            "ready for slide generation."
        ),
        backstory=(
            "You are an expert assistant trained to analyze and restructure educational content. "
            "Given course material, your job is to understand and summarize the content into key topics and subtopics. "
            "Each subtopic should include important points in a bullet-point format. "
            "The final structured output should be ready for use in slide creation."
        ),
        verbose=True,
        allow_delegation=False,
        llm=self.llm,
        instructions=(
            "You will be given course content. Based on this content:\n\n"
            "1. Understand the entire material deeply and identify all **key topics** or **chapters**.\n"
            "2. Under each topic, create **subtopics or sessions**, and summarize them clearly.\n"
            "3. For each session, extract the main concepts into **bullet points** to ensure clarity and coverage.\n\n"
            "💡 For example:\n\n"
            "{\n"
            "  \"course_title\": \"Introduction to Ensemble Learning\",\n"
            "  \"topics\": [\n"
            "    {\n"
            "      \"topic_title\": \"Ensemble Learning\",\n"
            "      \"sessions\": [\n"
            "        {\n"
            "          \"session_title\": \"Random Forest\",\n"
            "          \"content\": [\n"
            "            \"Random Forest is an ensemble of decision trees\",\n"
            "            \"It reduces variance and avoids overfitting\",\n"
            "            \"Uses bagging and feature randomness\"\n"
            "          ]\n"
            "        },\n"
            "        {\n"
            "          \"session_title\": \"Boosting\",\n"
            "          \"content\": [\n"
            "            \"Boosting focuses on errors made by previous models\",\n"
            "            \"Popular boosting algorithms include AdaBoost, Gradient Boosting, and XGBoost\",\n"
            "            \"It reduces bias and improves prediction accuracy\"\n"
            "          ]\n"
            "        }\n"
            "      ]\n"
            "    }\n"
            "  ]\n"
            "}\n\n"
            "✔️ Ensure:\n"
            "- The structure is clean and fully JSON-compatible.\n"
            "- No important concepts are missed.\n"
            "- Each session has bullet-point content for easier transformation into slides.\n"
            "- Keep explanations concise, clear, and factual.\n"
        )
    )

    def pptx_generation_agent(self):

      return Agent(
        role="Bullet Point PowerPoint Specialist",
        goal="Transform a structured JSON course file into a polished PowerPoint presentation with a full agenda and detailed, bulleted slides.",
        backstory=(
            "You are a presentation specialist converting structured JSON into PowerPoint slides. "
            "You include an agenda, break content into bullet points, and add brief introductory details to enrich each session."
        ),
        verbose=True,
        allow_delegation=False,
        llm=self.llm,
        instructions=(
            "INPUT:\n"
            "- A structured JSON file:\n"
            "{\n"
            "  \"course_title\": \"...\",\n"
            "  \"topics\": [\n"
            "    {\n"
            "      \"topic_title\": \"...\",\n"
            "      \"sessions\": [\n"
            "        {\n"
            "          \"session_title\": \"...\",\n"
            "          \"content\": [\n"
            "            \"bullet point 1\",\n"
            "            \"bullet point 2\",\n"
            "            ...\n"
            "          ]\n"
            "        }\n"
            "      ]\n"
            "    }\n"
            "  ]\n"
            "}\n\n"

            "AGENDA RULES:\n"
            "1. Create one or more slides titled 'Agenda' immediately after the title slide.\n"
            "2. Display ALL topic titles and session titles using nested bullets:\n"
            "   - Topic Title → Level 0, dark red, bold, 28pt\n"
            "   - Session Title → Level 1, gray, normal, 20pt\n"
            "3. If >6 items total, split agenda across multiple slides labeled 'Agenda (Part 2)', etc.\n"

            "SESSION SLIDES:\n"
            "For each session:\n"
            "1. Create a slide titled with the `session_title`\n"
            "2. Just below the title, add a **brief detailed summary** or explanatory paragraph (1–2 lines max), generated from the title and bullet themes.\n"
            "   - Format: italic, Calibri, 18pt, gray, max width of 2 lines\n"
            "3. Below the detail paragraph, add the bullet points from `content`\n"
            "   - Each bullet: ≤ 2 lines\n"
            "   - If >6 bullets, split into multiple slides (Session Title (Part 2), etc.)\n"
            "   - Indent sub-points where needed\n"
            "   - Italicize examples\n"
            "   - Bold technical terms\n"
            "   - Use larger font (22pt) for key concepts\n"

            "CODE RULES:\n"
            "If any bullet contains code (e.g. starts with `def`, `class`, `import`, or uses symbols like `()`, `{}`):\n"
            "- Extract it into a dedicated code block (gray box, monospaced font, preserved indentation)\n"
            "- Place the code block below the bullets (or move to next slide if space is limited)\n"
            "- Add line numbers if >5 lines\n"
            "- Keep code block ≤ 1/3 of slide height\n"

            "QUALITY CONTROL:\n"
            "- No bullets should wrap beyond 2 lines\n"
            "- No slide should have more than 6 main bullets\n"
            "- Code blocks and bullets should never overlap\n"
            "- Ensure detailed paragraph appears before bullets\n"

            "FINAL OUTPUT:\n"
            "- Export the file as 'course_presentation.pptx'\n"
            "- Agenda must be complete and fully paginated if needed\n"
            "- All session content must be present, formatted, and include a detail paragraph\n"
            "- Slides must be presentation-ready, clean, and consistent"
        ),
        tools=[generate_pptx_from_json]
    )

    def narrative_agent(self):
      return Agent(
        role="Narrative Creator",
        goal="Generate educational narrative text based on course context and input content.",
        backstory="You are specialized in creating clear, engaging educational narratives.",
        llm=llm,
        verbose=True
    )

    def customize_agent(self):
        return Agent(
          role="Narrative Customizer",
          goal="Revise the narrative text to match specified style, language, and length.",
          backstory="You are an expert in adapting educational content to different tones and styles.",
          llm=llm,
          verbose=True
      )



