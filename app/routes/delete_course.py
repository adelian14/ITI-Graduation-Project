from flask import Blueprint, redirect, url_for, request
from firebase.operations import get_project_by_id, save_project

deleteCourse_bp = Blueprint("deleteCourse", __name__)

@deleteCourse_bp.route("/projects/<project_id>/courses/<course_id>/delete", methods=["POST"])
def delete_course(project_id, course_id):
    project = get_project_by_id(project_id)
    project.delete_course(course_id)
    save_project(project)
    return redirect(url_for("project_view.project_dashboard", project_id=project_id))
