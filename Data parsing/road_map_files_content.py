def print_topics(topics, indent=3):
    if not isinstance(topics, list):
        return

    for topic in topics:
        topic_number = topic.get("Topic_number", "")
        topic_title = topic.get("Topic_title", "")
        print("  " * indent + f"Topic {topic_number}: {topic_title}")

        # Recursively print nested topics
        nested_topics = topic.get("Topic")
        if isinstance(nested_topics, list):
            print_topics(nested_topics, indent + 1)


def print_lessons(lessons, indent=2):
    if not isinstance(lessons, list):
        return

    for lesson in lessons:
        lesson_number = lesson.get("Lesson_number", "")
        lesson_title = lesson.get("Lesson_title", "")
        print("  " * indent + f"Lesson {lesson_number}: {lesson_title}")

        # Print lesson-level topics
        topics = lesson.get("Topic")
        if isinstance(topics, list):
            print_topics(topics, indent + 1)


def print_modules(data):
    modules = data.get("document_structure", {}).get("Module", [])
    for module in modules:
        module_number = module.get("Module_number", "")
        module_title = module.get("Module_title", "")
        print(f"Module {module_number}: {module_title}")

        lessons = module.get("Lesson")
        if isinstance(lessons, list):
            print_lessons(lessons)