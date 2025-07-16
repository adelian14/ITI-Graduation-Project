from models.Topic import Topic
from typing import List

class TopicItem:
    def __init__(self, _id, title: str = '', generated_versions: List[Topic] = [], parent_id = None):
        self.id = str(_id)
        self.title = title
        self.versions = generated_versions
        self.rawTopic = None
        self.parentId = parent_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "versions": [v.to_dict() for v in self.versions],
            "parentId": self.parentId,
            "rawTopic": self.rawTopic
        }
    
    @classmethod
    def from_dict(cls, data):
        topic_item = cls(
            _id=data["id"],
            title=data.get("title", ""),
            generated_versions=[Topic.from_dict(v) for v in data.get("versions", [])],
            parent_id=data.get("parentId")
        )
        topic_item.rawTopic=data.get("rawTopic", None)
        return topic_item

    def get_raw_topic(self):
        if not self.rawTopic: return None
        raw_topic = {"title":self.title, "content": self.rawTopic}
        return raw_topic
    
    def get_all_topics(self):
        sorted(self.versions, key = lambda t : t.generatedAt, reverse= True)
        return self.versions  