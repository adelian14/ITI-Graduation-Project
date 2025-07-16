from models.CurriculumNode import CurriculumNode
from models.teaching_config import DEFAULT_EXPERIENCE_LEVEL, experience_levels
from models.Module import Module

class Content(CurriculumNode):    
    def get_all_topics(self):
        topics = []
        for module in self.children:
            topics.extend(module.get_all_topics())
        sorted(topics, key = lambda t : t.generatedAt, reverse= True)
        return topics
    
    def get_all_lessons(self):
        lessons = []
        for module in self.children:
            lessons.extend(module.get_all_lessons())
        sorted(lessons, key = lambda l : l.generatedAt, reverse= True)
        return lessons
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data["id"],
            title=data.get("title", ""),
            desc=data.get("description", ""),
            children=[Module.from_dict(c) for c in data.get("children", [])],
            parent_id=data.get("parentId")
        )
