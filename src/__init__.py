from flask import Flask
from flask_restful import Api
from . import view, db, my_utils


def create_app():
    app = Flask(__name__)
    api = Api(app)
    db.create_tables()
    api.add_resource(view.StudentInfo, "/api/v1/student-info/")
    api.add_resource(view.CourseInfo, "/api/v1/course-info/")
    api.add_resource(view.StudentCourseMod, "/api/v1/groups-modification/")
    app.register_blueprint(view.bp)
    # my_utils.send_student_to_api()
    return app
