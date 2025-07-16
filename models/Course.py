from datetime import datetime
from models.teaching_config import experience_levels, DEFAULT_EXPERIENCE_LEVEL
from models.Content import Content

class Course:
    def __init__(self, _id, title, desc, num_modules, experience_level = experience_levels[DEFAULT_EXPERIENCE_LEVEL], parent_project_id = None, generated_at: datetime = None, content: Content = None):
        self.id = str(_id)
        self.title = title
        self.description = desc
        self.numModules = num_modules
        self.experienceLevel = experience_level
        self.parentProjectId = parent_project_id
        self.generatedAt = generated_at or datetime.now()
        self.content = content
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "numModules": self.numModules,
            "parentProjectId":self.parentProjectId,
            "experienceLevel": self.experienceLevel,
            "generatedAt": self.generatedAt.isoformat(),
            "content": self.content.to_dict() if self.content else None
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data["id"],
            title=data["title"],
            desc=data["description"],
            num_modules=data["numModules"],
            experience_level=data["experienceLevel"],
            parent_project_id=data["parentProjectId"],
            generated_at=datetime.fromisoformat(data["generatedAt"]),
            content=Content.from_dict(data["content"]) if data.get("content") else None
        )

    def get_context(self):
        return { 
            "course_title" : self.title,
            "course_level" : self.experienceLevel,
            "number_of_modules" : self.numModules,
            "course_description" : self.description
        }