import uuid
from flask import Blueprint, render_template, request, redirect, url_for
from models.Project import Project
from firebase.operations import save_project

create_bp = Blueprint("create_project", __name__)

@create_bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["description"]
        project_id = str(uuid.uuid4())

        project = Project(project_id, title, desc)
        save_project(project)

        return redirect(url_for("dashboard.dashboard"))

    return render_template("create_project.html")
