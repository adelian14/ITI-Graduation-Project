from models.Topic import Topic
from models.TopicItem import TopicItem
from models.Lesson import Lesson
from models. LessonVersion import LessonVersion
from models.LessonSetting import LessonSetting
from models.Course import Course
from models.Content import Content
from utils.json_utils import id_json
from uuid import uuid4
from pipeline.generation_crew.crew import build_lesson_generation_crew
from pipeline.roadmap_generation_crew.roadmap_generation import generate_roadmap

def lesson_generation(lesson: Lesson, setting: LessonSetting) -> LessonVersion:
    version = LessonVersion(
        _id=str(uuid4()),
        title=f"{lesson.title}",
        lesson_setting=setting,
        parent_id=lesson.id
    )
    
    context_dict = {"data": lesson.get_raw_lesson(), "setting": version.lessonSetting.to_dict()}
    crew = build_lesson_generation_crew(context_dict)
    try:
        result = crew.kickoff()
        version.rawLesson = str(result)
        print(version.rawLesson)
        return version
    
    except Exception as e:
        return None

def topic_generation(topic: TopicItem, setting: LessonSetting) -> Topic:
    version = Topic(
        _id=str(uuid4()),
        title=f"{topic.title}",
        lesson_setting=setting,
        parent_id=topic.id
    )
    
    context_dict = {"data": topic.get_summary(), "setting": version.lessonSetting.to_dict()}
    crew = build_lesson_generation_crew(context_dict)
    try:
        result = crew.kickoff()
        version.rawTopic = str(result)
        print(version.rawTopic)
        return version
    
    except Exception as e:
        return None
    
def generate_course(course: Course):
    context = course.get_context()
    try:
        content = generate_roadmap(context)
        content = id_json(course.id, content)
        course.content = Content.from_dict(content)
    except Exception as e:
        print(f"Couldn't parse file, Try again with another file. {e}")
    