from utils.models import llm_model
model = llm_model()

def text_to_json_with_llm(text_content):
    """Converts text content to JSON format using the Gemini model."""

    prompt = """
    You are a document structuring expert. You MUST convert the provided text into a JSON structure following the EXACT format specified below.

    CRITICAL REQUIREMENTS - NO EXCEPTIONS:
    1. Use ONLY the exact key names specified in the template
    2. Follow the EXACT structure hierarchy: document_metadata -> document_structure -> Module -> Lesson -> Topic
    3. Include ALL content from the source text - do not summarize or omit any information
    4. Key names are CASE-SENSITIVE and must match exactly: "Module", "Lesson", "Topic", "Full_content"
    5. Do not add new keys or modify existing key names
    6. Preserve all original text content in the "Full_content" fields
    7. If headers/titles are missing, create appropriate ones but still follow the structure

    MANDATORY OUTPUT FORMAT:
    {{
        "document_metadata": {{
            "document_title": "Document title if available, otherwise create appropriate title",
            "document_type": "academic|technical|report|manual|other",
            "total_pages": "number of pages processed",
            "language": "primary language detected",
            "has_tables": true/false,
            "has_charts": true/false,
            "has_images": true/false
        }},
        "document_structure": {{
            "Module": [
                {{
                    "Module_title": "Module title if available, otherwise create appropriate title",
                    "Module_number": "1 if available else null",
                    "Lesson": [
                        {{
                            "Lesson_number": "1.1",
                            "Lesson_title": "Lesson Title",
                            "Module_title": "Module title this lesson belongs to",
                            "Module_number": "Module number this lesson belongs to",
                            "page_number": "Page number if available",
                            "Topic": [
                                {{
                                    "Topic_number": "1.1.1",
                                    "Topic_title": "Topic Title",
                                    "Lesson_number": "Lesson number this topic belongs to",
                                    "Lesson_title": "Lesson title this topic belongs to",
                                    "Module_title": "Module title this topic belongs to",
                                    "Module_number": "Module number this topic belongs to",
                                    "page_number": "Page number if available",
                                    "Full_content": "COMPLETE text content from this topic - NO SUMMARIZATION",
                                    "lists": ["list items if any"],
                                    "tables": [
                                        {{
                                            "table_number": "Table 1",
                                            "caption": "Table caption",
                                            "headers": ["Column 1", "Column 2"],
                                            "rows": [["Data 1", "Data 2"]]
                                        }}
                                    ],
                                    "figures": [
                                        {{
                                            "figure_number": "Figure 1",
                                            "caption": "Figure caption",
                                            "description": "Description of visual content"
                                        }}
                                    ]
                                }}
                            ]
                        }}
                    ]
                }}
            ]
        }}
    }}

    STRICT PROCESSING RULES:
    - NEVER change the key names: "document_metadata", "document_structure", "Module", "Module_title", "Lesson", "Lesson_title", "Topic" , "Topic_title", "Full_content"
    - NEVER summarize content - include ALL original text in "Full_content" fields
    - NEVER be creative - strictly follow the template structure
    - If document lacks clear sections, organize by logical breaks but maintain the Module->Lesson->Topic hierarchy
    - For unclear structures, preserve as formatted text within the required structure
    - ALL content must be preserved - no information should be lost
    - If a section is missing, create a placeholder but maintain the structure

    TEXT TO CONVERT:
    {}

    OUTPUT REQUIREMENTS:
    - Return ONLY valid JSON
    - NO additional text, explanations, or markdown formatting
    - NO ```json``` code blocks
    - Ensure all text content is fully preserved in the appropriate "Full_content" fields
    """.format(text_content)

    response = model.generate_content([prompt])
    return response.text