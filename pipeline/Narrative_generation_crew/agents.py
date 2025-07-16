from crewai import Agent, LLM
from pipeline.llm_models.config import gemini_model

llm = gemini_model()

class NarrativeGenerationAgents:
    def __init__(self):
        """Initialize with a selected LLM provider and model"""
        self.llm = llm
        
    # Agent 1: Content Analyzer & Narrative Structurer
    content_analyzer_agent = Agent(
        role="Educational Content Analyzer & Narrative Architect",
        goal="""Analyze raw educational content and transform it into a compelling, 
        pedagogically sound narrative structure that maximizes learning retention 
        and engagement.""",
        backstory="""You are a seasoned educational content strategist with 15+ years 
        of experience in curriculum design and storytelling. You specialize in breaking 
        down complex topics into digestible, memorable narratives. You understand 
        cognitive load theory, learning progressions, and how to create emotional 
        connections with educational content.""",
        verbose=False,
        allow_delegation=False,
        llm=llm
    )

    # Agent 2: Audience Personalization Specialist
    personalization_agent = Agent(
        role="Audience Personalization & Learning Experience Designer",
        goal="""Transform generic educational content into highly personalized learning 
        experiences that resonate with specific audience demographics, learning styles, 
        and experience levels.""",
        backstory="""You are an expert in educational psychology and personalized learning 
        design. You have deep knowledge of how different age groups, experience levels, 
        and learning preferences affect content consumption. You excel at adjusting 
        complexity, tone, examples, and delivery methods to match learner needs perfectly.""",
        verbose=False,
        allow_delegation=False,
        llm=llm
    )

    # Agent 3: Multi-Media Script Producer
    script_producer_agent = Agent(
        role="Multi-Media Educational Script Producer",
        goal="""Create production-ready video scripts with detailed scene breakdowns, 
        narration, visual cues, and engagement elements that translate educational 
        content into captivating video experiences.""",
        backstory="""You are a professional educational video producer with expertise 
        in creating explainer videos, educational content, and instructional media. 
        You understand pacing, visual storytelling, engagement techniques, and how to 
        maintain viewer attention throughout educational videos.""",
        verbose=False,
        allow_delegation=False,
        llm=llm
    )

    # Agent 4: Markdown Formatting Specialist
    markdown_formatter_agent = Agent(
        role="Markdown Documentation Specialist",
        goal="""Transform video script content into clean, professional markdown format 
        with proper structure, headers, emphasis, and documentation standards.""",
        backstory="""You are a technical documentation expert specializing in markdown 
        formatting and content structuring. You excel at creating clean, readable, 
        and well-organized markdown documents that are perfect for documentation, 
        sharing, and version control. You understand markdown syntax, best practices, 
        and how to create professional-looking structured documents.""",
        verbose=False,
        allow_delegation=False,
        llm=llm
    )