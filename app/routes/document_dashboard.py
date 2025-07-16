from flask import Blueprint, render_template, abort
from firebase.operations import get_project_by_id, save_project
from pipeline.parse_pdf import parse_document_content

documentDashboard_bp = Blueprint("documentDashboard", __name__)

@documentDashboard_bp.route("/projects/<project_id>/documents/<doc_id>")
def document_dashboard(project_id, doc_id):
    project = get_project_by_id(project_id)
    doc = project.get_doc(doc_id)

    if not doc:
        abort(404, "Document not found")

    if doc.parsedContent is None:
        print("Sending file to agent parser...")
        parse_document_content(doc)
        save_project(project)

    return render_template("document_dashboard.html", project=project, doc=doc)
