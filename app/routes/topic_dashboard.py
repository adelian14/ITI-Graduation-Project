from flask import Blueprint, render_template
from models.Project import Project
from firebase.operations import get_project_by_id, get_document_by_id, get_topic_by_id

topicDashboard_bp = Blueprint("topic_dashboard", __name__, url_prefix="/projects/<project_id>")

@topicDashboard_bp.route("/topics/<topic_id>")
def topic_dashboard(project_id, topic_id):
    # Retrieve everything we need
    project = get_project_by_id(project_id)
    topic = get_topic_by_id(project_id, topic_id)

    if not topic:
        return "Topic not found", 404

    return render_template(
        "topic_dashboard.html",
        project=project,
        topic=topic
    )
