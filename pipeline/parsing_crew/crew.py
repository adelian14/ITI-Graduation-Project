# crew_pdf_parser.py

from crewai import Agent, Task, Crew
from pipeline.parsing_crew.tools.ocr_tool import OCRTool
from pipeline.parsing_crew.tools.patch_merger_tool import PatchMergerTool
from pipeline.parsing_crew.tools.markdown_normalizer_tool import MarkdownNormalizerTool
from pipeline.llm_models.config import gemini_model

# === Tool instances ===
ocr_tool = OCRTool()
patch_tool = PatchMergerTool()
md_tool = MarkdownNormalizerTool()

# === Agent 1: OCR Agent ===
ocr_agent = Agent(
    role="OCR Processor",
    goal="Extract readable text from image patches using OCR",
    backstory="You're skilled in recognizing text from scanned documents and returning clean results.",
    tools=[ocr_tool],
    verbose=True,
    llm = gemini_model()
)

# === Agent 2: Text Unifier Agent ===
unifier_agent = Agent(
    role="Text Merger",
    goal="Merge and reorder multiple OCR outputs into a single coherent document",
    backstory="You take fragmented outputs and arrange them logically, fixing overlaps or order issues.",
    verbose=True, 
    llm=gemini_model(0.4)
)

# === Agent 3: Markdown Formatter Agent ===
formatter_agent = Agent(
    role="Markdown Formatter",
    goal="Format raw text into structured, readable Markdown",
    backstory="You're a document formatter who turns messy text into clean, readable Markdown with clear sections.",
    tools=[md_tool],
    verbose=True,
    llm = gemini_model(0.4)
)

course_agent = Agent(
    role="Course Structuring Agent",
    goal="Break down educational content into Modules → Lessons → Topics with raw-text descriptions.",
    backstory=(
        "You're a curriculum designer. Your job is to structure content logically, "
        "outputting plain raw text in a clean, indented, and hierarchical format. "
        "Do NOT return JSON or markdown, just indented headings and descriptions."
    ),
    verbose=True,
    llm = gemini_model()
)


json_agent = Agent(
    role="JSON Structuring Agent",
    goal="Parse raw hierarchical text and convert it into a strictly formatted JSON document.",
    backstory=(
        "You're a highly accurate information architect. You receive indented text representing a document's structure "
        "and output deeply nested JSON objects following a strict schema of document > modules > lessons > topics. "
        "Each node has a title, a description, and children (if applicable). Topics include their rawContent."
    ),
    verbose=True,
    llm = gemini_model(.3)
)



# === Crew Factory Function ===
def build_pdf_parsing_crew(image_paths: list[str], patch_size: int = 5) -> Crew:
    # Step 1: Split into chunks
    patches = patch_tool._run(image_paths, patch_size)

    # Step 2: Create OCR tasks for each patch
    ocr_tasks = []
    ocr_outputs = []
    for i, patch in enumerate(patches):
        task = Task(
            description=f"Extract text from images: {patch}",
            expected_output="Cleaned text extracted from these image pages.",
            agent=ocr_agent,
            tools=[ocr_tool]
        )
        ocr_tasks.append(task)

    # Step 3: Merging Task
    merge_task = Task(
        description="Merge and reorder all extracted text chunks into a single clean document.",
        expected_output="A single continuous block of text, logically ordered.",
        agent=unifier_agent,
        context=ocr_tasks
    )

    # Step 4: Markdown Formatting Task
    format_task = Task(
        description="Format the merged document into clean Markdown using headings, lists, and paragraphs.",
        expected_output="A Markdown-formatted version of the full content.",
        agent=formatter_agent,
        context=[merge_task]
    )

    course_task = Task(
        description=(
            "Given the Markdown-formatted content, analyze and organize it into Modules, Lessons, and Topics. "
            "Each module should start with 'Module X [title]', followed by a description. "
            "Each lesson should be inside a module and start with 'Lesson X.Y [title]', followed by a description. "
            "Each topic should be nested inside a lesson and start with 'Topic X.Y.Z [title]', with its description and raw content. "
            "The entire output should be raw text, structured using indentation, NOT JSON or markdown."
        ),
        expected_output="A clean, indented, raw text hierarchy of modules → lessons → topics, no JSON.",
        agent=course_agent,
        context=[merge_task]
    )
    

    json_task = Task(
        description=(
            "Convert the following structured educational content into a deeply nested JSON object. "
            "Use this schema strictly:\n\n"
            "document = {\n"
            '  "title": "Document Title",\n'
            '  "description": "High-level overview of the document",\n'
            '  "children": [ modules ]\n'
            "}\n\n"
            "module = {\n"
            '  "title": "Module Title",\n'
            '  "description": "What this module teaches",\n'
            '  "children": [ lessons ]\n'
            "}\n\n"
            "lesson = {\n"
            '  "title": "Lesson Title",\n'
            '  "description": "What this lesson covers",\n'
            '  "children": [ topics ]\n'
            "}\n\n"
            "topic = {\n"
            '  "title": "Topic Title",\n'
            '  "description": "What this topic explains",\n'
            '  "rawTopic": "Raw content as extracted — can be markdown or plain text"\n'
            "}\n\n"
            "Return valid JSON only. No extra text or commentary."
        ),
        expected_output="A single valid JSON object following the schema above.",
        agent=json_agent,
        context=[course_task]
    )

    
    # Step 5: Build and return Crew
    return Crew(
        agents=[ocr_agent, unifier_agent, course_agent, json_agent],
        tasks=ocr_tasks + [merge_task, course_task, json_task],
        verbose=True
    )
