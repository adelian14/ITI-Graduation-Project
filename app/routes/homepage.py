from flask import Blueprint, render_template
from firebase.operations import get_project_metadata

homepage_bp = Blueprint("homepage", __name__)

@homepage_bp.route("/")
def dashboard():
    projects = get_project_metadata()
    return render_template("index.html", projects=projects)
