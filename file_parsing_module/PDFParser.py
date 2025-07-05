from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLineHorizontal, LTChar
from typing import List
from file_parsing_module.TextElement import TextElement  # or define inline if not modularized yet

def extract_text_elements(pdf_path: str) -> List[TextElement]:
    text_elements = []

    for page_number, page_layout in enumerate(extract_pages(pdf_path), start=1):
        for element in page_layout:
            if isinstance(element, LTTextBoxHorizontal):
                for line in element:
                    if not isinstance(line, LTTextLineHorizontal):
                        continue
                    
                    text = line.get_text().strip()
                    if not text:
                        continue

                    font_sizes = []
                    font_names = []
                    is_bold = False
                    is_italic = False

                    for char in line:
                        if isinstance(char, LTChar):
                            font_sizes.append(char.size)
                            font_names.append(char.fontname)
                            if "Bold" in char.fontname:
                                is_bold = True
                            if "Italic" in char.fontname or "Oblique" in char.fontname:
                                is_italic = True

                    avg_font_size = max(font_sizes) if font_sizes else 0
                    dominant_font = font_names[0] if font_names else None

                    element_obj = TextElement(
                        text=text,
                        font_size=avg_font_size,
                        font_name=dominant_font,
                        bbox=line.bbox,
                        is_bold=is_bold,
                        is_italic=is_italic,
                        page_number=page_number
                    )

                    text_elements.append(element_obj)

    return text_elements
