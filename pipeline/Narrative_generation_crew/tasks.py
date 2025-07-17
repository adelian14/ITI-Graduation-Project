from crewai import Task
from datetime import datetime

class NarrativeGenerationTasks:
    def create_analyze_and_structure_task(self, lesson_content_string, learner, agent):
        return Task(
            description=f"""
            CONTENT ANALYSIS & NARRATIVE STRUCTURING

            **Raw Content to Analyze:**
            {lesson_content_string}

            **Your Mission:**
            1. **Content Analysis**: Identify key concepts, learning objectives, and difficulty level
            2. **Narrative Architecture**: Structure into engaging story format with:
            - Hook/Opening (grab attention immediately)
            - Problem/Challenge setup
            - Progressive concept building
            - Real-world applications
            - Memorable conclusion

            **Requirements:**
            - Create logical learning progression
            - Identify 3-5 key takeaways
            - Include storytelling elements (characters, scenarios, analogies)
            - Ensure content flows naturally from simple to complex
            - Add interactive elements (questions, thought experiments)
            - Target total length: {learner.attention_span}

            **Output Format:**
            - Clear section headers
            - Learning objectives for each section
            - Suggested pacing and timing
            - Key concepts highlighted
            """,
            expected_output="""A comprehensive narrative structure document with:
            - Executive summary of content
            - Detailed section breakdown with timing
            - Key learning objectives
            - Storytelling elements and analogies
            - Interactive engagement points""",
            agent=agent,
        )


    def create_personalize_content_task(self, learner, agent, dependency_task):
        return Task(
            description=f"""
            AUDIENCE PERSONALIZATION & CUSTOMIZATION

            **Target Learner Profile:**
            - Age Range: {learner.age}
            - Experience Level: {learner.experience}
            - Preferred Style: {learner.style}
            - Language Level: {learner.language}
            - Desired Tone: {learner.tone}
            - Attention Span: {learner.attention_span}
            - Learning Preference: {learner.learning_preference}

            **Your Mission:**
            Take the structured narrative and transform it to perfectly match the learner profile:

            1. **Language Adaptation**: Adjust vocabulary, sentence structure, and complexity
            2. **Tone Calibration**: Ensure the tone matches the desired emotional engagement
            3. **Experience Matching**: Provide appropriate context and background for beginners
            4. **Age-Appropriate Examples**: Use relatable scenarios and references
            5. **Style Implementation**: Incorporate step-by-step approach with analogies
            6. **Engagement Optimization**: Add motivational elements and curiosity triggers

            **Specific Requirements:**
            - Use conversational, friendly language
            - Include relevant analogies and metaphors
            - Add encouragement and motivation
            - Break complex ideas into digestible chunks
            - Include "why this matters" explanations
            - Add personal relevance connections
            """,
            expected_output="""A fully personalized educational narrative featuring:
            - Age-appropriate language and examples
            - Motivational and curious tone throughout
            - Step-by-step explanations with analogies
            - Beginner-friendly context and background
            - Interactive elements matching learning preferences""",
            agent=agent,
            depends_on=[dependency_task],
        )


    def create_produce_video_script_task(self, learner, agent, dependency_task):
        return Task(
            description=f"""
            VIDEO SCRIPT PRODUCTION

            **Production Requirements:**
            Transform the personalized narrative into a complete, production-ready video script.

            **Script Structure:**
            1. **Opening Hook** (0-15 seconds): Grab attention immediately
            2. **Introduction** (15-30 seconds): Set context and expectations
            3. **Main Content Sections** (70% of total time): Core educational content
            4. **Practical Application** (15% of total time): How to use the knowledge
            5. **Conclusion & Next Steps** (5% of total time): Wrap up and call to action

            **For Each Scene Include:**
            - Scene number and title
            - Estimated duration
            - Narrator script (word-for-word)
            - Visual suggestions (animations, graphics, text overlays)
            - Audio cues (music, sound effects)
            - Transition instructions
            - Engagement elements (questions, pauses, emphasis)

            **Technical Specifications:**
            - Target video length: {learner.attention_span}
            - Speaking pace: 150-160 words per minute
            - Include natural pauses and emphasis
            - Add visual cue timings
            - Include subtitle-friendly formatting

            **Quality Standards:**
            - Professional, engaging narration
            - Clear visual instructions
            - Smooth transitions between scenes
            - Appropriate pacing and rhythm
            - Production notes for editor
            """,
            expected_output="""A complete video production script with:
            - Scene-by-scene breakdown with timings
            - Word-for-word narration script
            - Detailed visual and audio cues
            - Production notes and instructions
            - Ready for immediate video production""",
            agent=agent,
            depends_on=[dependency_task],
        )


    def create_format_markdown_task(self, learner, agent, dependency_task):
        return Task(
            description=f"""
            MARKDOWN FORMATTING & DOCUMENTATION

            **Your Mission:**
            Transform the final video script into a professional, well-structured markdown document 
            that is clean, readable, and follows markdown best practices.

            **Markdown Structure Requirements:**
            
            1. **Document Header:**
            - Main title using # (H1)
            - Subtitle and metadata using ## (H2)
            - Generation date and audience info
            
            2. **Script Structure:**
            - Use ## (H2) for major sections
            - Use ### (H3) for scene headers
            - Use #### (H4) for subsections within scenes
            
            3. **Content Formatting:**
            - **Bold** for emphasis and important terms
            - *Italic* for production notes and directions
            - `Code formatting` for technical terms or specific instructions
            - > Blockquotes for narrator voice or special instructions
            
            4. **Lists and Organization:**
            - Use numbered lists (1. 2. 3.) for sequential steps
            - Use bullet points (-) for feature lists and options
            - Use checkboxes (- [ ]) for production checklists
            
            5. **Special Elements:**
            - Horizontal rules (---) to separate major sections
            - Tables for timing and production schedules
            - Code blocks for long production notes

            **Quality Standards:**
            - Clean, consistent formatting throughout
            - Proper heading hierarchy
            - Clear visual separation between sections
            - Professional appearance when rendered
            - Easy to read and navigate
            - GitHub/documentation platform friendly

            **Example Structure:**
            ```markdown
            # Educational Video Script: [Topic]

            ## Project Information
            - **Target Audience:** {learner.age}
            - **Duration:** {learner.attention_span}
            - **Experience Level:** {learner.experience}

            ---

            ## Scene 1: Opening Hook
            **Duration:** 0-15 seconds

            ### Narration
            > [Enthusiastic tone] "Have you ever wondered..."

            ### Visual Cues
            - Animated introduction
            - Background transition

            ### Production Notes
            *Remember to emphasize the question*
            ```
            """,
            expected_output="""A professionally formatted markdown document with:
            - Clean, consistent markdown syntax
            - Proper heading hierarchy and structure
            - Well-organized content sections
            - Professional formatting and styling
            - Easy-to-read and navigate layout
            - Production-ready documentation format""",
            agent=agent,
            depends_on=[dependency_task],
        )

