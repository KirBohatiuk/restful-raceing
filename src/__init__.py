from flask import Flask
from flask_restful import Api
from . import view


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(view.ReadStudent, "/api/v1/get/")
    api.add_resource(view.CreateStudent, "/api/v1/post/")
    api.add_resource(view.UpdateStudent, "/api/v1/put/<string:name>")
    api.add_resource(view.DeleteStudent, "/api/v1/delete/<int:num>")

    return app
