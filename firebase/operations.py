from firebase.config import db
from models.Project import Project
from models.LessonVersion import LessonVersion
from models.Topic import Topic

PROJECTS_COLLECTION = 'projects'

def save_project(project: Project):
    data = project.to_dict()
    db.collection(PROJECTS_COLLECTION).document(project.id).set(data)

def get_all_projects() -> list:
    docs = db.collection(PROJECTS_COLLECTION).stream()
    return [Project.from_dict(doc.to_dict()) for doc in docs]

def delete_project(project_id: str):
    db.collection(PROJECTS_COLLECTION).document(project_id).delete()

def get_project_metadata() -> list:
    docs = (
            db.collection(PROJECTS_COLLECTION)
            .order_by("createdAt", direction="DESCENDING")
            .select(["id", "title", "description"])
            .stream()
        )
    return [{"id": doc.get("id"), "title": doc.get("title"), "description": doc.get("description")} for doc in docs]

def get_project_metadata_by_id(project_id: str):
    doc = db.collection(PROJECTS_COLLECTION).document(project_id).get()
    if doc.exists:
        return {
            "id": doc.get("id"),
            "title": doc.get("title"),
            "description": doc.get("description")
        }
    return None

def get_project_by_id(project_id: str):
    doc = db.collection(PROJECTS_COLLECTION).document(project_id).get()
    if doc.exists:     
        return Project.from_dict(doc.to_dict())
    return None

def get_document_by_id(project_id: str, doc_id: str):
    prj = get_project_by_id(project_id)
    if not prj: return None
    for doc in prj.documents:
        if doc.id == doc_id:
            return doc
    return None

def get_topic_by_id(project_id: str, topic_id: str):
    prj = get_project_by_id(project_id)
    for doc in prj.documents:
        if not doc.parsedContent: continue
        for mod in doc.parsedContent.children:
            for lesson in mod.children:
                for topic in lesson.children:
                    if topic.id == topic_id:
                        return topic
    for course in prj.courses:
        if not course.content: continue
        for mod in course.content.children:
            for lesson in mod.children:
                for topic in lesson.children:
                    if topic.id == topic_id:
                        return topic
    return None

def get_lesson_by_id(project_id: str, lesson_id: str):
    prj = get_project_by_id(project_id)
    for doc in prj.documents:
        if not doc.parsedContent: continue
        for mod in doc.parsedContent.children:
            for lesson in mod.children:
                if lesson.id == lesson_id:
                    return lesson
    for course in prj.courses:
        if not course.content: continue
        for mod in course.content.children:
            for lesson in mod.children:
                if lesson.id == lesson_id:
                    return lesson
    return None

def save_lesson_version(project_id, lesson_id, new_version: LessonVersion):
    project = get_project_by_id(project_id)
    for doc in project.documents:
        if not doc.parsedContent: continue
        for mod in doc.parsedContent.children:
            for lesson in mod.children:
                if lesson.id == lesson_id:
                    lesson.versions.append(new_version)
                    save_project(project)
                    return
    for course in project.courses:
        if not course.content: continue
        for mod in course.content.children:
            for lesson in mod.children:
                if lesson.id == lesson_id:
                    lesson.versions.append(new_version)
                    save_project(project)
                    return

def save_topic_version(project_id, topic_id, new_version: Topic):
    project = get_project_by_id(project_id)
    for doc in project.documents:
        if not doc.parsedContent: continue
        for mod in doc.parsedContent.children:
            for lesson in mod.children:
                for topic in lesson.children:
                    if topic.id == topic_id:
                        topic.versions.append(new_version)
                        save_project(project)
                        return
    for course in project.courses:
        if not course.content: continue
        for mod in course.content.children:
            for lesson in mod.children:
                for topic in lesson.children:
                    if topic.id == topic_id:
                        topic.versions.append(new_version)
                        save_project(project)
                        return

def get_all_lessons(project_id):
    project = get_project_by_id(project_id)
    all_lessons = []

    def collect_lessons_from_content(content):
        if not content:
            return
        for module in content.children:
            for lesson in module.children:
                all_lessons.append(lesson)

    for doc in project.documents:
        collect_lessons_from_content(doc.parsedContent)

    for course in project.courses:
        collect_lessons_from_content(course.content)

    return all_lessons

def get_all_topics(project_id):
    project = get_project_by_id(project_id)
    all_topics = []

    def collect_topics_from_content(content):
        if not content:
            return
        for module in content.children:
            for lesson in module.children:
                for topic in lesson.children:
                    all_topics.append(topic)

    for doc in project.documents:
        collect_topics_from_content(doc.parsedContent)
        
        
    for course in project.courses:
        collect_topics_from_content(course.content)

    return all_topics


def get_generated_version(project_id,version_id):
    lessons = get_all_lessons(project_id)
    topics = get_all_topics(project_id)
    for lesson in lessons:
        for version in lesson.versions:
            if version.id == version_id:
                return version
    for topic in topics:
        for version in topic.versions:
            if version.id == version_id:
                return version