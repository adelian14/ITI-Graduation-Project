from flask import Blueprint, redirect, url_for, request
from firebase.operations import get_project_by_id, save_project

deleteDocument_bp = Blueprint("deleteDocument", __name__)

@deleteDocument_bp.route("/projects/<project_id>/documents/<doc_id>/delete", methods=["POST"])
def delete_document(project_id, doc_id):
    project = get_project_by_id(project_id)
    project.delete_doc(doc_id)
    save_project(project)
    return redirect(url_for("project_view.project_dashboard", project_id=project_id))
