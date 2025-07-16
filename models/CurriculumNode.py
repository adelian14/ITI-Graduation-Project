from typing import List, Optional
from abc import ABC

class CurriculumNode(ABC):
    def __init__(self, _id, title: str = '', desc: str = '', children: Optional[List] = None, parent_id = None):
        self.id = str(_id)
        self.title = title
        self.description = desc
        self.children = children or []
        self.parentId = parent_id

    def get_all_topics(self) -> List:
        raise NotImplementedError("Override in subclass is needed.")
    
    def get_all_lessons(self) -> List:
        raise NotImplementedError("Override in subclass is needed.")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "children": [c.to_dict() for c in self.children],
            "parentId": self.parentId
        }

