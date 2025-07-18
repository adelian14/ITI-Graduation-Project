from flask import Blueprint, redirect, url_for, request
from firebase.operations import delete_project_by_id, save_project

deleteProject_bp = Blueprint("deletePeoject", __name__)

@deleteProject_bp.route("/projects/<project_id>/delete", methods=["POST"])
def delete_project(project_id):
    delete_project_by_id(project_id)
    return redirect(url_for("dashboard.dashboard", project_id=project_id))
