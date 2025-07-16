from flask import Blueprint, render_template
from firebase.operations import get_generated_version
from models.LessonVersion import LessonVersion
from models.Topic import Topic as TopicVersion

genMaterial_bp = Blueprint("genMaterial", __name__, url_prefix="/projects/<project_id>")

@genMaterial_bp.route("/gen_material/<version_id>", methods=["GET"])
def generate_material(project_id, version_id):
    version = get_generated_version(project_id, version_id)

    if not version:
        return "Material version not found", 404

    is_lesson = isinstance(version, LessonVersion)
    
    return render_template(
        "generated_version.html",
        version=version,
        is_lesson=is_lesson,
        project_id=project_id
    )
