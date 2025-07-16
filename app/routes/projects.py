from flask import Blueprint, render_template
from firebase.operations import get_project_metadata
from models.Project import Project

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/projects")
def dashboard():
    projects = get_project_metadata()
    return render_template("dashboard.html", projects=projects)


