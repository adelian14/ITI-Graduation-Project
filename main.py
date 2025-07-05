from file_parsing_module.PDFParser import extract_text_elements
from file_parsing_module.utils import count_font_sizes

file_path = 'test_files/book-test.pdf'

text_elements = extract_text_elements(file_path)

font_size_counts = count_font_sizes(text_elements)

for size, count in sorted(font_size_counts.items(), key=lambda x: -x[0]):
    print(f"Font size {size}: {count} occurrences")