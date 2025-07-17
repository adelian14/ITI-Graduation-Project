from flask import request, redirect, url_for, render_template, Blueprint
from models.teaching_config import experience_levels, explanatory_styles, age_groups, teaching_tones, languages
from models.teaching_config import DEFAULT_AGE_GROUP, DEFAULT_EXPERIENCE_LEVEL, DEFAULT_EXPLANATORY_STYLE, DEFAULT_LANGUAGE, DEFAULT_TEACHING_TONE
from models.LessonSetting import LessonSetting
from models.Topic import Topic
from models.LessonVersion import LessonVersion
from uuid import uuid4
from firebase.operations import (
    get_document_by_id,
    get_lesson_by_id,
    get_topic_by_id,
    save_lesson_version,
    save_topic_version
)
from pipeline.generation import lesson_generation, topic_generation, full_generation


generateRoute_bp = Blueprint("generate_route",__name__,url_prefix="/projects/<project_id>")

@generateRoute_bp.route("lessons/<lesson_id>/generate", methods=["GET"])
def generate_lesson_form(project_id, lesson_id):
    return render_template("generate_form.html",
        form_action=f"/projects/{project_id}/lessons/{lesson_id}/generate",
        age_groups=age_groups,
        experience_levels=experience_levels,
        explanatory_styles=explanatory_styles,
        languages=languages,
        teaching_tones=teaching_tones,
        default_age=DEFAULT_AGE_GROUP,
        default_experience=DEFAULT_EXPERIENCE_LEVEL,
        default_explanatory_style=DEFAULT_EXPLANATORY_STYLE,
        default_language=DEFAULT_LANGUAGE,
        default_tone=DEFAULT_TEACHING_TONE
    )

@generateRoute_bp.route("topics/<topic_id>/generate", methods=["GET"])
def generate_topic_form(project_id, topic_id):
    return render_template("generate_form.html",
        form_action=f"/projects/{project_id}/topics/{topic_id}/generate",
        age_groups=age_groups,
        experience_levels=experience_levels,
        explanatory_styles=explanatory_styles,
        languages=languages,
        teaching_tones=teaching_tones,
        default_age=DEFAULT_AGE_GROUP,
        default_experience=DEFAULT_EXPERIENCE_LEVEL,
        default_explanatory_style=DEFAULT_EXPLANATORY_STYLE,
        default_language=DEFAULT_LANGUAGE,
        default_tone=DEFAULT_TEACHING_TONE
    )

@generateRoute_bp.route("lessons/<lesson_id>/generate", methods=["POST"])
def generate_lesson_material(project_id, lesson_id):
    setting = LessonSetting(
        narrative_language=languages[request.form["language"]],
        explanatory_style=explanatory_styles[request.form["explanatory_style"]],
        teaching_tone=teaching_tones[request.form["teaching_tone"]],
        age_group=age_groups[request.form["age_group"]],
        experience_level=experience_levels[request.form["experience_level"]]
    )

    lesson = get_lesson_by_id(project_id, lesson_id)

    version = lesson_generation(lesson, setting)
    
    if version:
        full_generation(version)
        save_lesson_version(project_id, lesson_id, version)

    return redirect(f"/projects/{project_id}/lessons/{lesson_id}")


@generateRoute_bp.route("topics/<topic_id>/generate", methods=["POST"])
def generate_topic_material(project_id, topic_id):
    setting = LessonSetting(
        narrative_language=languages[request.form["language"]],
        explanatory_style=explanatory_styles[request.form["explanatory_style"]],
        teaching_tone=teaching_tones[request.form["teaching_tone"]],
        age_group=age_groups[request.form["age_group"]],
        experience_level=experience_levels[request.form["experience_level"]]
    )

    topic = get_topic_by_id(project_id, topic_id)

    version = topic_generation(topic, setting)
    
    if version:
        full_generation(version)
        save_topic_version(project_id, topic_id, version)

    return redirect(f"/projects/{project_id}/topics/{topic_id}")