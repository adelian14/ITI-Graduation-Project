from flask import Blueprint, render_template, abort, session
from firebase.operations import get_project_by_id, delete_project
from models.Project import Project

project_bp = Blueprint("project_view", __name__)

@project_bp.route("/projects/<project_id>")
def project_dashboard(project_id):
    project = get_project_by_id(project_id)
    if not project:
        abort(404, description="Project not found.")

    session["active_project_id"] = project_id

    return render_template("project_dashboard.html", project = project)