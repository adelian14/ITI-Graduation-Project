from models.LessonSetting import LessonSetting
from datetime import datetime

class LessonVersion:
    def __init__(self, _id, title: str = '', lesson_setting: LessonSetting = None, generated_at: datetime = None, parent_id = None, narrative = None, slides = None, summary = None, raw_lesson = None, video_script = None):
        self.id = str(_id)
        self.title = title
        self.lessonSetting = lesson_setting or LessonSetting()
        self.narrative = narrative
        self.slides = slides
        self.summary = summary
        self.rawLesson = raw_lesson
        self.videoScript = video_script
        self.generatedAt = generated_at or datetime.now()
        self.parentId = parent_id
        
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "lessonSetting": self.lessonSetting.to_dict(),
            "narrative": self.narrative,
            "slides": self.slides,
            "rawLesson": self.rawLesson,
            "summary": self.summary,
            "videoScript": self.videoScript,
            "generatedAt": self.generatedAt.isoformat(),
            "parentId": self.parentId
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data["id"],
            title=data.get("title", ""),
            lesson_setting=LessonSetting.from_dict(data["lessonSetting"]),
            generated_at=datetime.fromisoformat(data["generatedAt"]),
            parent_id=data.get("parentId"),
            narrative=data.get("narrative",None),
            slides=data.get("slides",None),
            raw_lesson=data.get("rawLesson",None),
            summary=data.get("summary",None),
            video_script=data.get("videoScript",None)
        )

