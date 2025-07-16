from models.CurriculumNode import CurriculumNode
from models.TopicItem import TopicItem
from models.LessonVersion import LessonVersion
from typing import Optional, List

class Lesson(CurriculumNode):
    def __init__(self, _id, title: str = '', desc: str = '', children: Optional[List] = None, parent_id = None, generated_versions: Optional[List] = None):
        super().__init__(_id = _id, title = title, desc = desc, children = children, parent_id = parent_id)
        self.versions = generated_versions or []
        
    def get_all_topics(self):
        topics = []
        for topic_item in self.children:
            topics.extend(topic_item.versions)
        sorted(topics, key = lambda t : t.generatedAt, reverse= True)
        return topics
    
    def get_all_lessons(self):
        sorted(self.versions, key = lambda l : l.generatedAt, reverse= True)
        return self.versions
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "children": [c.to_dict() for c in self.children],
            "parentId": self.parentId,
            "versions": [v.to_dict() for v in self.versions]
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data["id"],
            title=data.get("title", ""),
            desc=data.get("description", ""),
            children=[TopicItem.from_dict(c) for c in data.get("children", [])],
            parent_id=data.get("parentId"),
            generated_versions=[LessonVersion.from_dict(v) for v in data.get("versions", [])]
        )

    def get_raw_lesson(self):
        raw_lesson = {"lesson_title": self.title, "lesson_description": self.description, "covered_topics": []}
        for topic in self.children:
            raw_lesson["covered_topics"].append({"title": topic.title, "content": topic.rawTopic if topic.rawTopic else ""})
        return raw_lesson