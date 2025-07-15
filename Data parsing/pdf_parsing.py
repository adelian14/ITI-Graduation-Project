import os
import re
import json
import shutil
from ocr_complex_document import ocr_with_llm
from pdf_to_images import convert_pdf_to_images, batch_images
from text_to_json import text_to_json_with_llm

def process_large_pdf_with_cleanup(
    pdf_path: str,
    output_folder: str = './images',
    batch_size: int = 10,
    cleanup_images: bool = True
) -> str:
    """
    Processes a large PDF by converting it to images, performing OCR, and optionally cleaning up.

    Args:
        pdf_path (str): Path to the input PDF.
        output_folder (str): Directory to store image outputs.
        batch_size (int): Number of images to process in a batch.
        cleanup_images (bool): If True, deletes the image folder after processing.

    Returns:
        str: The full OCR-extracted text from the PDF.
    """

    # Cleanup any existing output folder before starting
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)

    try:
        # Convert PDF to images
        image_paths = convert_pdf_to_images(pdf_path, output_folder)

        # Split into batches
        batches = batch_images(image_paths, batch_size)

        # Run OCR and combine results
        full_text = ""
        for i, batch in enumerate(batches):
            print(f"Processing batch {i+1}...")
            batch_text = ocr_with_llm(batch, "Extract all text, maintaining document structure")
            full_text += f"\n\n--- BATCH {i+1} ---\n\n{batch_text}"

        return full_text

    finally:
        # Cleanup images if requested
        if cleanup_images and os.path.exists(output_folder):
            shutil.rmtree(output_folder)
            print(f"Cleaned up images folder: {output_folder}")


def pdf_parse_and_convert_to_json(pdf_path, output_folder = './images'):  
    batch_size = 10
    cleanup_images = True
    extracted_text = process_large_pdf_with_cleanup(pdf_path, output_folder, batch_size, cleanup_images)
    structure_json_content = text_to_json_with_llm(extracted_text)
    cleaned_structure_json_content = re.sub(r'(?<!\\)\\(?!["\\/bfnrtu])', r'\\\\', structure_json_content)
    cleaned_structure_json_content = cleaned_structure_json_content.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()

    return cleaned_structure_json_content
