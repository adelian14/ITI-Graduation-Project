import os
import uuid
from flask import Blueprint, request, redirect, url_for
from firebase.config import bucket
from firebase.operations import get_project_by_id, save_project
from models.DocumentObject import DocumentObject
from firebase.file_operations import save_file

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/projects/<project_id>/upload", methods=["POST"])
def upload_file(project_id):
    
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400

    name, ext, file_id = save_file(file, project_id)

    document = DocumentObject(
        _id=file_id,
        name=name,
        extension=ext,
        parent_project_id=project_id
    )
    
    project = get_project_by_id(project_id)
    project.add_doc(document)
    
    save_project(project)
    
    return redirect(url_for("project_view.project_dashboard", project_id=project_id))
