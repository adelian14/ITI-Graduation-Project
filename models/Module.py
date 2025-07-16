from models.CurriculumNode import CurriculumNode
from models.Lesson import Lesson

class Module(CurriculumNode):
    def get_all_topics(self):
        topics = []
        for lesson in self.children:
            topics.extend(lesson.get_all_topics())
        sorted(topics, key = lambda t : t.generatedAt, reverse= True)
        return topics
    
    def get_all_lessons(self):
        lessons = []
        for lesson in self.children:
            lessons.extend(lesson.get_all_lessons())
        sorted(lessons, key = lambda l : l.generatedAt, reverse= True)
        return lessons
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data["id"],
            title=data.get("title", ""),
            desc=data.get("description", ""),
            children=[Lesson.from_dict(c) for c in data.get("children", [])],
            parent_id=data.get("parentId")
        )
