from pydantic import BaseModel
from typing import List

class Lesson(BaseModel):
    title: str

class Module(BaseModel):
    title: str
    lessons: List[str]

class Roadmap(BaseModel):
    course_title: str
    description: str
    modules: List[Module]
