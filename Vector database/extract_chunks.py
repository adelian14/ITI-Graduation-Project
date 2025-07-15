def add_full_content_fields(data):
    for module in data['document_structure']['Module']:
        module_full_content = []

        for lesson in module['Lesson']:
            lesson_full_content = []

            for topic in lesson['Topic']:
                topic_content = topic.get('Full_content', '')
                lesson_full_content.append(topic_content)

            # Add Full_content to the lesson
            lesson['Full_content'] = '\n\n'.join(lesson_full_content)
            module_full_content.append(lesson['Full_content'])

        # Add Full_content to the module
        module['Full_content'] = '\n\n'.join(module_full_content)

    return data

def extract_chunks_by_module(data):
    chunks = []
    document_meta = data.get("document_metadata", {})
    modules = data.get("document_structure", {}).get("Module", [])

    for module in modules:
        text = module.get("Full_content", "")
        if text:
            chunks.append({
                "id": f"module-{module.get('Module_number', 'X')}",
                "metadata": {
                    "module_number": module.get("Module_number"),
                    "module_title": module.get("Module_title"),
                    "document_title": document_meta.get("document_title"),
                    "document_type": document_meta.get("document_type"),
                    "language": document_meta.get("language")
                },
                    "text": f"{module.get('Module_title')}\n\n{text.strip()}"
            })

    return chunks

def extract_chunks_by_lesson(data):
    chunks = []
    document_meta = data.get("document_metadata", {})
    modules = data.get("document_structure", {}).get("Module", [])

    for module in modules:
        lessons = module.get("Lesson", [])
        for lesson in lessons:
            text = lesson.get("Full_content", "")
            if text:
                chunks.append({
                    "id": f"lesson-{lesson.get('Lesson_number', 'X')}",
                    "metadata": {
                        "module_number": lesson.get("Module_number"),
                        "module_title": lesson.get("Module_title"),
                        "lesson_number": lesson.get("Lesson_number"),
                        "lesson_title": lesson.get("Lesson_title"),
                        "document_title": document_meta.get("document_title"),
                        "document_type": document_meta.get("document_type"),
                        "language": document_meta.get("language")
                    },
                    "text": f"{lesson.get('Module_title')}\n\n{lesson.get('Lesson_title')}\n\n{text.strip()}"
                })

    return chunks

def extract_chunks_by_topic(data):
    chunks = []
    document_meta = data.get("document_metadata", {})
    modules = data.get("document_structure", {}).get("Module", [])

    def extract_topic_chunks(topics):
        for topic in topics:
            text = topic.get("Full_content", "")
            if text:
                chunks.append({
                    "id": f"topic-{topic.get('Topic_number', 'X')}",
                    "metadata": {
                        "module_number": topic.get("Module_number"),
                        "module_title": topic.get("Module_title"),
                        "lesson_number": topic.get("Lesson_number"),
                        "lesson_title": topic.get("Lesson_title"),
                        "topic_number": topic.get("Topic_number"),
                        "topic_title": topic.get("Topic_title"),
                        "document_title": document_meta.get("document_title"),
                        "document_type": document_meta.get("document_type"),
                        "language": document_meta.get("language")
                    },
                    "text": f"{topic.get('Module_title')}\n\n{topic.get('Lesson_title')}\n\n{topic.get('Topic_title')}\n\n{text.strip()}"
                })

            if "Topic" in topic:
                extract_topic_chunks(topic["Topic"])

    for module in modules:
        lessons = module.get("Lesson", [])
        for lesson in lessons:
            topics = lesson.get("Topic", [])
            extract_topic_chunks(topics)

    return chunks

def extract_chunks(data, chunk_type):
    data = add_full_content_fields(data)
    
    if chunk_type == "module":
        return extract_chunks_by_module(data)
    elif chunk_type == "lesson":
        return extract_chunks_by_lesson(data)
    elif chunk_type == "topic":
        return extract_chunks_by_topic(data)
    else:
        raise ValueError("Invalid chunk type specified. Use 'module', 'lesson', or 'topic'.")