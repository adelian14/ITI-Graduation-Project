from collections import Counter
from typing import List
from file_parsing_module.TextElement import TextElement  # or use inline class
import math

def count_font_sizes(elements: List[TextElement]) -> dict:
    sizes = [math.floor(el.font_size) for el in elements if el.font_size > 0]
    return dict(Counter(sizes))
