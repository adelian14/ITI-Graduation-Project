from firebase.config import bucket
import os
from werkzeug.utils import secure_filename
import uuid
from models.DocumentObject import DocumentObject
from firebase.config import TEMP_DIR
import shutil

def save_file(file, project_id):
    print(TEMP_DIR)
    filename = secure_filename(file.filename)
    name, ext = os.path.splitext(filename)
    ext = ext.replace(".", "")

    file_id = str(uuid.uuid4())
    storage_path = f"projects/{project_id}/{name}_{file_id}.{ext}"

    # Upload to Firebase Storage
    blob = bucket.blob(storage_path)
    blob.upload_from_file(file, content_type=file.content_type)
    
    return name, ext, file_id


def download_file_to_temp(storage_path: str, extension="pdf") -> str:
    """
    Downloads a file from Firebase Storage into the local 'temp/' folder.
    Returns the local file path.
    """

    blob = bucket.blob(storage_path)

    if not blob.exists():
        raise FileNotFoundError(f"File not found in Firebase Storage: {storage_path}")

    filename = f"{uuid.uuid4()}.{extension}"
    local_path = os.path.join(TEMP_DIR, filename)

    blob.download_to_filename(local_path)
    return local_path


def delete_file_from_storage(file: DocumentObject):
    """
    Deletes a file from Firebase Storage given its path (e.g., 'projects/<project_id>/<file_id>.pdf').
    """
    storage_path = file.get_full_path()
    blob = bucket.blob(storage_path)

    if blob.exists():
        blob.delete()
        print(f"Deleted: {storage_path}")
    else:
        print(f"File not found in storage: {storage_path}")


def clear_temp_folder():
    for filename in os.listdir(TEMP_DIR):
        file_path = os.path.join(TEMP_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # remove file or symlink
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # remove directory and its contents
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


