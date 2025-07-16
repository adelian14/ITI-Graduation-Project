import uuid
from flask import Blueprint, render_template, request, redirect, url_for
from models.Course import Course
from models.teaching_config import experience_levels
from firebase.operations import get_project_by_id, save_project

createCourse_bp = Blueprint("courseCreate_course", __name__)

@createCourse_bp.route("/projects/<project_id>/courses/create", methods=["GET", "POST"])
def create_course(project_id):
    
    project = get_project_by_id(project_id)
    print('here')
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        num_modules = int(request.form["num_modules"])
        experience_level = request.form["experience_level"]

        course = Course(
            _id=str(uuid.uuid4()),
            title=title,
            desc=description,
            num_modules=num_modules,
            experience_level=experience_levels[experience_level]
        )

        project.add_course(course)
        save_project(project)

        return redirect(url_for("project_view.project_dashboard", project_id=project_id))

    return render_template("create_course.html", project=project, experience_levels=experience_levels)
