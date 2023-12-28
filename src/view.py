from flask_restful import Resource
from flask import request
from .db import create_student, get_session


class StudentInfo(Resource):
    def get(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            session = get_session()
            student = create_student(first_name=first_name, last_name=last_name, session=session)
            return student.first_name
    def post(self):
        user_info = request.get_json()
        first_name = user_info["first_name"]
        last_name = user_info["last_name"]

        # session = get_session()
        # student = create_student(first_name=first_name, last_name=last_name, session=session)
        return last_name
    #
    # def put(self, name):
    #     new_name = request.get_json()
    #     for num, name_dct in student.items():
    #         if name_dct == name:
    #             student[num] = new_name
    #     return student
    #
    # def delete(self, num):
    #     del student[num]
    #     return student
