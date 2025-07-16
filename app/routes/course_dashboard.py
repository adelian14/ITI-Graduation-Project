from flask import Blueprint, render_template, abort
from firebase.operations import get_project_by_id, save_project
from pipeline.generation import generate_course

courseDashboard_bp = Blueprint("courseDashboard", __name__)

@courseDashboard_bp.route("/projects/<project_id>/courses/<course_id>")
def course_dashboard(project_id, course_id):
    project = get_project_by_id(project_id)
    course = project.get_course(course_id)

    if not course:
        abort(404, "Course not found")

    if course.content is None:
        print("Sending file to course generator...")
        generate_course(course)
        save_project(project)

    return render_template("course_dashboard.html", project=project, course=course)
