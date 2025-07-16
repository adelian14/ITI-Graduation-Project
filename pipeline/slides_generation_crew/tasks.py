from crewai import Task
from datetime import datetime

class SlidesGenerationTasks:
    def summarize_task(agent, data) -> Task:
        """Create an enhanced content summarization task"""
        return Task(
            description=f"""
            Conduct a comprehensive educational analysis of the following lesson content using advanced pedagogical frameworks:

            CONTENT TO ANALYZE:
            {data}

            ANALYSIS REQUIREMENTS:

            1. **Learning Objectives Analysis:**
            - Identify explicit and implicit learning objectives
            - Classify objectives using Bloom's Taxonomy (Remember, Understand, Apply, Analyze, Evaluate, Create)
            - Assess alignment between objectives and content

            2. **Content Structure Analysis:**
            - Map the logical flow and information hierarchy
            - Identify key concepts, supporting details, and examples
            - Analyze concept dependencies and prerequisites
            - Detect potential cognitive load issues

            3. **Educational Metadata:**
            - Determine appropriate difficulty level and target audience
            - Estimate learning time and cognitive effort required
            - Identify prerequisite knowledge and skills
            - Assess accessibility and inclusivity considerations

            4. **Concept Mapping:**
            - Create a hierarchical breakdown of main topics and subtopics
            - Identify relationships between concepts
            - Highlight critical path concepts vs. supporting material

            5. **Learning Challenges Assessment:**
            - Identify potential misconceptions or difficult concepts
            - Suggest scaffolding strategies for complex topics
            - Recommend reinforcement and practice opportunities

            6. **Practical Applications:**
            - Extract real-world applications and use cases
            - Identify hands-on activities and examples
            - Suggest additional practical exercises

            7. **Assessment Opportunities:**
            - Identify natural checkpoints for formative assessment
            - Suggest knowledge check questions and activities
            - Recommend summative assessment strategies

            Provide a structured, comprehensive analysis that will inform effective presentation design.
            """,
            agent=agent,
            expected_output=(
                "A comprehensive educational analysis including learning objectives classification, "
                "content structure mapping, difficulty assessment, concept relationships, learning "
                "challenges identification, practical applications, and assessment recommendations. "
                "The analysis should be structured and actionable for presentation design."
            )
        )

    def design_task(agent) -> Task:
        """Create an enhanced slide structure design task"""
        return Task(
            description="""
            Design a comprehensive slide structure for an educational presentation using advanced instructional design principles:

            DESIGN REQUIREMENTS:

            1. **Presentation Architecture:**
            - Design optimal slide sequence and flow
            - Determine total slide count with rationale
            - Create logical information progression
            - Plan cognitive load distribution across slides

            2. **Slide Type Specifications:**
            - Title slides with impact and clarity
            - Content slides with optimal information density
            - Concept illustration slides with visual learning support
            - Activity/interaction slides for engagement
            - Summary and reinforcement slides for retention
            - Assessment/checkpoint slides for formative evaluation

            3. **Information Architecture:**
            - Apply progressive disclosure principles
            - Design visual hierarchy for each slide type
            - Plan content chunking for optimal processing
            - Ensure logical concept building and scaffolding

            4. **Engagement Strategy:**
            - Plan interaction points and active learning moments
            - Design attention management techniques
            - Include variety in presentation methods
            - Plan for different learning preferences

            5. **Time and Pacing:**
            - Allocate appropriate time per slide
            - Plan for questions and discussion
            - Include buffer time for complex concepts
            - Design natural break points

            6. **Visual Design Guidelines:**
            - Specify layout requirements for different slide types
            - Plan for visual elements (diagrams, charts, images)
            - Ensure accessibility and readability standards
            - Design consistent visual themes

            7. **Technical Specifications:**
            - Define slide dimensions and formatting requirements
            - Specify font, color, and styling guidelines
            - Plan for multimedia integration
            - Consider export and sharing requirements

            Create a detailed slide-by-slide blueprint that maximizes learning effectiveness.
            """,
            agent=agent,
            expected_output=(
                "A comprehensive slide structure design including slide-by-slide breakdown, "
                "content distribution strategy, engagement planning, time allocation, visual "
                "design guidelines, and technical specifications. The design should be "
                "pedagogically sound and ready for implementation."
            )
        )

    def json_task(agent) -> Task:
        """Create an enhanced JSON structure creation task with static template"""
        return Task(
            description="""
            Create a comprehensive, production-ready JSON structure for PowerPoint presentation generation using the following STATIC TEMPLATE structure:

            REQUIRED JSON STRUCTURE (DO NOT MODIFY THESE KEYS):

            ```json
            {
                "presentation_metadata": {
                    "title": "",
                    "author": "",
                    "date": "",
                    "duration_estimate": "",
                    "difficulty_level": "",
                    "prerequisites": [],
                    "summary": "",
                    "version": "1.0"
                },
                "learning_objectives": [
                    {
                        "id": "",
                        "description": "",
                        "bloom_level": "",
                        "assessment_method": ""
                    }
                ],
                "slides": [
                    {
                        "slide_id": "",
                        "slide_number": 1,
                        "slide_type": "",
                        "title": "",
                        "content": {
                            "header": "",
                            "subheader": "",
                            "bullet_points": [],
                            "text_blocks": [],
                            "tables": [
                                {
                                    "headers": [],
                                    "rows": []
                                }
                            ],
                            "plots": [
                                {
                                    "type": "",
                                    "title": "",
                                    "description": "",
                                    "data_source": ""
                                }
                            ],

                        },
                        "presenter_notes": "",
                        "time_allocation": 0,
                        "visual_elements": {
                            "layout": "",
                            "background": "",
                            "color_scheme": ""
                        }
                    }
                ],
                "styling": {
                    "theme": "",
                    "font_primary": "",
                    "font_secondary": "",
                    "color_palette": {
                        "primary": "",
                        "secondary": "",
                        "accent": "",
                        "background": "",
                        "text": ""
                    }
                },
                "export_config": {
                    "output_format": "pptx",
                    "resolution": "1920x1080",
                    "compression_quality": "high",
                    "speaker_view": true,
                    "handout_mode": false
                },
                "extensibility": {
                    "custom_fields": {},
                    "ai_agent_hooks": [],
                    "integration_points": []
                }
            }
            ```

            REQUIREMENTS:
            1. **Maintain Static Keys:** Do NOT modify the structure or key names above
            2. **Populate with Content:** Fill all fields with appropriate content based on the lesson analysis
            3. **Ensure Completeness:** Every slide must have complete content structure
            4. **Validate Data Types:** Use correct data types (strings, arrays, objects, numbers, booleans)
            5. **Cover All Use Cases:** Include examples of:
            - Header and subheader usage
            - Bullet point lists
            - Text blocks for detailed content
            - Tables with proper headers and rows
            - Plot/chart specifications

            SPECIFIC CONTENT REQUIREMENTS:
            - Create at least 8-12 slides covering the lesson content
            - Include variety in slide types (title, content, diagram, summary, etc.)
            - Ensure proper content distribution across slides
            - Add comprehensive presenter notes for each slide
            - Include realistic time allocations
            - Specify appropriate visual elements and styling

            Generate a complete, valid JSON structure that can be directly used by PowerPoint generation tools.
            """,
            agent=agent,
            expected_output=(
                "A complete, valid JSON structure following the exact static template provided. "
                "The JSON must be production-ready for PowerPoint generation with all required "
                "fields populated, proper data types, and comprehensive content covering all "
                "use cases including headers, subheaders, bullet points, tables, and plots. "
                "The structure should be directly consumable by python-pptx or similar tools."
            )
        )

