from crewai import Task

class RoadmapGenerationTasks:
    # Task 1: Create modules
    def course_planner(self, agent, input_data):
        return Task(
        description=f"""Given the following inputs:
        - Course Title: {input_data['course_title']}
        - Course Level: {input_data['course_level']}
        - Number of Modules: {input_data['number_of_modules']}
        - Course Description: {input_data['course_description']}

        Create a JSON array of modules. Each module must include:
        - module_title
        - module_goal
        """,
            expected_output="A JSON list of modules with module_title and module_goal.",
            agent=agent
        )

    # Task 2: Create lessons per module
    def lesson_designer(self, agent):
        return Task(
            description="""Using the modules provided, create 2–3 lessons per module.
            Each lesson must include:
            - lesson_title
            - parent_module
            """,
                expected_output="A JSON list of lessons, each with lesson_title and parent_module.",
                agent=agent
            )

    # Task 3: Generate topics for each lesson
    def topic_generator(self, agent):
        return Task(
        description="""For each lesson, generate 3–5 topic titles.
        Each topic must include:
        - topic_title
        - parent_lesson
        - parent_module
        """,
            expected_output="A JSON list of topics with their parent lesson and module.",
            agent=agent
        )

    # Task 4: Format everything into a nested JSON: Module -> Lessons -> Topics
    def json_formatter(self, agent):
        return Task(
        description="""
        Convert the following structured educational content into a deeply nested JSON object. 
        Combine the modules, lessons, and topics into a nested JSON structure like this:
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
                "}\n\n"
                "Return valid JSON only. No extra text or commentary."
    """,
        expected_output="A single JSON array of modules, each with lessons and nested topics.",
        agent=agent
    )
