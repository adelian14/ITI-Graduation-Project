from models.teaching_config import languages, explanatory_styles, teaching_tones, age_groups, experience_levels
from models.teaching_config import DEFAULT_LANGUAGE, DEFAULT_EXPLANATORY_STYLE, DEFAULT_TEACHING_TONE, DEFAULT_AGE_GROUP, DEFAULT_EXPERIENCE_LEVEL

class LessonSetting:
    
    def __init__(self,
                 narrative_language = languages[DEFAULT_LANGUAGE],
                 explanatory_style = explanatory_styles[DEFAULT_EXPLANATORY_STYLE],
                 teaching_tone = teaching_tones[DEFAULT_TEACHING_TONE], 
                 age_group = age_groups[DEFAULT_AGE_GROUP],
                 experience_level = experience_levels[DEFAULT_EXPERIENCE_LEVEL]):
        
        self.narrativeLanguage = narrative_language
        self.explanatoryStyle = explanatory_style
        self.teachingTone = teaching_tone
        self.ageGroup = age_group
        self.experienceLevel = experience_level
    
    def to_dict(self):
        return {
            "narrativeLanguage": self.narrativeLanguage,
            "explanatoryStyle": self.explanatoryStyle,
            "teachingTone": self.teachingTone,
            "ageGroup": self.ageGroup,
            "experienceLevel": self.experienceLevel
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            narrative_language=data.get("narrativeLanguage"),
            explanatory_style=data.get("explanatoryStyle"),
            teaching_tone=data.get("teachingTone"),
            age_group=data.get("ageGroup"),
            experience_level=data.get("experienceLevel")
        )

