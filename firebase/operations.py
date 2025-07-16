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
    
