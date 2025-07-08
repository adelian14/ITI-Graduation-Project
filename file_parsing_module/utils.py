from collections import Counter
from typing import List
from file_parsing_module.TextElement import TextElement
import math
from collections import defaultdict

def count_font_sizes(elements: List[TextElement]) -> dict:
    sizes = [math.floor(el.font_size) for el in elements if el.font_size > 0]
    return dict(Counter(sizes))


def compute_weighted_font_distribution(elements: List[TextElement]):
    font_char_count = defaultdict(int)

    for el in elements:
        font_size = math.floor(el.font_size)
        font_char_count[font_size] += len(el.text)

    return dict(sorted(font_char_count.items(), key=lambda x: -x[1]))

