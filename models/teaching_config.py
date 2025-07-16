DEFAULT_EXPLANATORY_STYLE = 'concept'
DEFAULT_TEACHING_TONE = 'neutral'
DEFAULT_EXPERIENCE_LEVEL = 'beginner'
DEFAULT_AGE_GROUP = 'adult'
DEFAULT_LANGUAGE = 'en'

languages = {
    'en': 'English',
    'ar': 'Arabic',
    'mixed': 'Mixed (Arabic with original English technical terms)'
}


explanatory_styles = {
    'concept': 'Conceptual (focus on understanding underlying ideas)',
    'example': 'Example-driven (learning by concrete use cases)',
    'visual': 'Visual (uses diagrams, flowcharts, illustrations)',
    'step_by_step': 'Step-by-step (progressive logical breakdown)',
    'analogy': 'Analogy-based (relating to real-world situations)',
    'compare': 'Comparative (contrasting related ideas)',
    'hands_on': 'Hands-on (interactive or code-first approach)',
    'theoretical': 'Theoretical (focus on formal definitions and theory)',
    'practical': 'Practical (real-world applications and tips)',
    'story': 'Story-based (explaining through narrative or scenario)',
    'intuitive': 'Intuitive (building gut-level understanding first)',
    'minimal': 'Minimal (as few words as possible, direct core insight)',
    'faq': 'FAQ-style (common questions with sharp answers)'
}


teaching_tones = {
    'neutral': 'Neutral (balanced, informative, and objective)',
    'formal': 'Formal (academic, structured, and professional)',
    'conversational': 'Conversational (casual, friendly tone)',
    'humorous': 'Humorous (light-hearted and witty)',
    'motivational': 'Motivational (inspiring and confidence-boosting)',
    'provocative': 'Provocative (challenges assumptions and encourages debate)',
    'empathetic': 'Empathetic (emotionally supportive and understanding)',
    'authoritative': 'Authoritative (confident, expert-led tone)',
    'skeptical': 'Skeptical (questioning, critical-thinking focused)',
    'enthusiastic': 'Enthusiastic (energetic and passionate delivery)',
    'serious': 'Serious (no-nonsense, focused delivery)',
    'calm': 'Calm (soothing and patient, great for anxious learners)',
    'playful': 'Playful (gamified, curious tone to keep it fun)'
}


experience_levels = {
    'beginner': 'Beginner (no prior knowledge or just starting out)',
    'intermediate': 'Intermediate (some experience, understands basics)',
    'advanced': 'Advanced (solid experience, familiar with key concepts)',
    'expert': 'Expert (deep understanding, may challenge assumptions)',
    'mixed': 'Mixed (covers multiple levels in one audience)'
}


age_groups = {
    'child': 'Child (under 13)',
    'teen': 'Teen (ages 13-17)',
    'young_adult': 'Young Adult (ages 18-25)',
    'adult': 'Adult (ages 26-50)',
    'senior': 'Senior (50+)',
    'mixed': 'Mixed (age-diverse audience)'
}
