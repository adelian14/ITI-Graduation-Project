from file_parsing_module.PDFParser import extract_text_elements
from file_parsing_module.utils import count_font_sizes, compute_weighted_font_distribution
import math

file_path = 'test_files/test-paper.pdf'

text_elements = extract_text_elements(file_path)

font_size_counts = compute_weighted_font_distribution(text_elements)

for ele in text_elements[1000:1010]:
    print(ele)

for size, count in sorted(font_size_counts.items(), key=lambda x: -x[0]):
    print(f"Font size {size}: {count} occurrences")

font_20 = [ele for ele in text_elements if math.floor(ele.font_size)==9]

print('='*50)
for txt in font_20:
    print(txt.text)
    print('-'*10)