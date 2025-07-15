import os
from pdf2image import convert_from_path


def convert_pdf_to_images(pdf_path, output_folder, dpi=300):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi)

    # Save images to the output folder
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.jpg')
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)

    return image_paths

def batch_images(image_paths, batch_size=10):
    """Group images into batches for processing"""
    for i in range(0, len(image_paths), batch_size):
        yield image_paths[i:i + batch_size]