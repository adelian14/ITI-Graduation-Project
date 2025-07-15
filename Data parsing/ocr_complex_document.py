from utils.models import llm_model
from PIL import Image

model = llm_model()

def ocr_with_llm(image_paths, instruction):
    images = [Image.open(path) for path in image_paths]

    prompt = f"""

    You are an expert document analysis AI with exceptional OCR capabilities.
    Your task is to extract ALL textual content from the provided document images with perfect accuracy.

    CRITICAL REQUIREMENTS:
    1. ACCURACY: Every word, number, symbol, and punctuation mark must be captured exactly as shown
    2. STRUCTURE: Maintain the original document structure, hierarchy, and formatting
    3. COMPLETENESS: Do not skip any content, including headers, footers, page numbers, footnotes, watermarks, or marginalia
    4. CONTEXT: Understand the document context to resolve ambiguous characters

    {instruction}

    """

    response = model.generate_content([prompt, *images])
    return response.text

def ocr_complex_document(image_paths):
    instruction = """
    Extract ALL text content from these document pages.
    For Tables:
    - Use markdown table format with proper alignment
    - Include all headers, subheaders, and merged cells
    - Preserve numerical precision and units
    - Note any table notes or footnotes

    For Multi-column Text:
    - Process columns in natural reading order (left to right, top to bottom)
    - Clearly separate column content with appropriate breaks
    - Maintain column-specific formatting

    For Charts/Graphs:
    - Describe chart type and purpose
    - Extract all axis labels, legends, and data points
    - Capture titles, captions, and source information
    - Note any trends or key insights visible in the visual

    For Special Elements:
    - Preserve bullet points, numbered lists, and indentation
    - Maintain emphasis (bold, italic, underline) using markdown
    - Capture all hyperlinks and cross-references
    - Include page numbers and section breaks

    QUALITY ASSURANCE:
    - Double-check all numerical data for accuracy
    - Verify proper names, technical terms, and specialized vocabulary
    - Ensure logical flow and coherence in extracted text
    - Flag any unclear or potentially misread content with [UNCERTAIN: text]
    Preserve all headers, footers, page numbers, and footnotes.
    """

    return ocr_with_llm(image_paths, instruction)