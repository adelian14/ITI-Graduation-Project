from flask import Flask
from app.routes.homepage import homepage_bp
from app.routes.projects import dashboard_bp
from app.routes.project import project_bp
from app.routes.create_project import create_bp
from app.routes.upload_file import upload_bp
from app.routes.delete_document import deleteDocument_bp
from app.routes.create_course import createCourse_bp
from app.routes.document_dashboard import documentDashboard_bp
from app.routes.lesson_dashboard import lessonDashboard_bp
from app.routes.topic_dashboard import topicDashboard_bp
from app.routes.generate_route import generateRoute_bp
from app.routes.course_dashboard import courseDashboard_bp
from app.routes.gen_material import genMaterial_bp
from app.routes.delete_project import deleteProject_bp
from dotenv import load_dotenv
from markdown import markdown


load_dotenv()

app = Flask(__name__, template_folder='app/templates')
app.jinja_env.filters['markdown'] = lambda text: markdown(text or "")

app.secret_key = "SECRET_KEY"
app.register_blueprint(homepage_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(create_bp)
app.register_blueprint(project_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(deleteDocument_bp)
app.register_blueprint(deleteProject_bp)
app.register_blueprint(createCourse_bp)
app.register_blueprint(documentDashboard_bp)
app.register_blueprint(courseDashboard_bp)
app.register_blueprint(lessonDashboard_bp)
app.register_blueprint(topicDashboard_bp)
app.register_blueprint(generateRoute_bp)
app.register_blueprint(genMaterial_bp)

if __name__ == "__main__":
    app.run(debug=True)
