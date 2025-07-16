from flask import Blueprint, render_template, session
from models.Project import Project
from firebase.operations import get_lesson_by_id, get_document_by_id, get_project_by_id

lessonDashboard_bp = Blueprint("lesson_dashboard", __name__, url_prefix="/projects/<project_id>")

@lessonDashboard_bp.route("/lessons/<lesson_id>")
def lesson_dashboard(project_id, lesson_id):
    # Fetch project from DB (session or Firestore)
    project = get_project_by_id(project_id)
    target_lesson = get_lesson_by_id(project_id, lesson_id)

    if not target_lesson:
        return "Lesson not found", 404

    return render_template(
        "lesson_dashboard.html",
        project=project,
        lesson=target_lesson
    )
