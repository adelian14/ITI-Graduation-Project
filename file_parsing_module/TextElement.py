from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class TextElement:
    text: str
    font_size: float
    font_name: Optional[str]
    bbox: Tuple[float, float, float, float]
    is_bold: bool = False
    is_italic: bool = False
    page_number: int = 0

    def __post_init__(self):
        self.text = self.text.strip()
        
    def __repr__(self):
        return f"{self.text} | font: {self.font_size} | {'bold' if self.is_bold else 'regular'}"
