from models.DocumentObject import DocumentObject
from models.Content import Content
from firebase.config import TEMP_DIR
from firebase.file_operations import download_file_to_temp, clear_temp_folder
from firebase.operations import save_project, get_project_by_id
from pdf2image import convert_from_path
import os
from pipeline.parsing_crew.crew import build_pdf_parsing_crew
from utils.json_utils import id_json, str_to_json

def parse_document_content(doc: DocumentObject):
    if doc.parsedContent:
        return
    path = doc.get_full_path()
    local_path = download_file_to_temp(path, doc.extension)
    image_paths = convert_pdf_to_images(local_path, doc.id)
    crew = build_pdf_parsing_crew(image_paths)
    result = crew.kickoff()
    json_content = str_to_json(str(result))
    json_content = id_json(doc.id, json_content)
    doc.parsedContent = Content.from_dict(json_content)
    doc.error = None
    clear_temp_folder()


def convert_pdf_to_images(pdf_path, doc_id, dpi=300):
    # Create output directory if it doesn't exist
    os.makedirs(TEMP_DIR, exist_ok=True)
    # poppler_path = r"poppler-24.08.0\Library\bin"
    # images = convert_from_path(pdf_path, dpi=dpi, poppler_path=poppler_path)
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi)
    

    # Save images to the output folder
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(TEMP_DIR, f'{doc_id}_page_{i+1}.jpg')
        image.save(image_path, 'JPEG')
        image_paths.append(image_path)

    return image_paths
     