from datetime import datetime
from models.DocumentObject import DocumentObject
from models.Course import Course
from firebase.file_operations import delete_file_from_storage, save_file
class Project:
    def __init__(self, _id, title, desc, created_at: datetime = None):
        self.id = str(_id)
        self.title = title
        self.description = desc
        self.createdAt = created_at or datetime.now()
        self.documents = []
        self.courses = []
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description, 
            "createdAt": self.createdAt.isoformat(),
            "documents": [f.to_dict() for f in self.documents],
            "courses": [c.to_dict() for c in self.courses],
        }
    
    @classmethod
    def from_dict(cls, data):

        project = cls(
            _id=data["id"],
            title=data["title"],
            desc=data["description"],
            created_at=datetime.fromisoformat(data["createdAt"])
        )

        project.documents = [DocumentObject.from_dict(f) for f in data.get("documents", [])]
        project.courses = [Course.from_dict(c) for c in data.get("courses", [])]
        project.sort_docs()
        project.sort_courses()
        return project
    
    def get_doc(self, doc_id) -> DocumentObject:
        for doc in self.documents:
            if doc.id == doc_id:
                return doc
        return None
            
    def get_course(self, course_id) -> Course:
        for course in self.courses:
            if course.id == course_id:
                return course
        return None
    
    def delete_doc(self, doc_id):
        for doc in self.documents:
            if doc.id == doc_id:
                delete_file_from_storage(doc)
        self.documents = [d for d in self.documents if d.id != doc_id]
        self.sort_docs()
    
    def delete_course(self, crs_id):
        self.courses = [c for c in self.courses if c.id != crs_id]
        self.sort_courses()
    
    def add_doc(self, doc: DocumentObject):
        self.documents.append(doc)
        self.sort_docs()
        
    def add_course(self, course: Course):
        self.courses.append(course)
        self.sort_courses()
    
    def sort_docs(self):
        self.documents = sorted(self.documents, key=lambda doc: doc.uploadedAt, reverse=True)
        
    def sort_courses(self):
        self.courses = sorted(self.courses, key=lambda c: c.generatedAt, reverse=True)
        
    

        
