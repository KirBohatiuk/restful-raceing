from flask_restful import Resource
from flask import request
from .db import create_student, get_session, StudentModel


class StudentInfo(Resource):
    def get(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            session = get_session()
            student_dict = {}
            students = session.query(StudentModel).filter(StudentModel.first_name == first_name).all()
            for i, student in enumerate(students):
                student_dict[i] = {"first_name": first_name}
                student_dict[i] = {"last_name": last_name}
            return student_dict
    def post(self):
        user_info = request.get_json()
        first_name = user_info["first_name"]
        last_name = user_info["last_name"]
        session = get_session()
        student = create_student(first_name=first_name, last_name=last_name, session=session)
        return student.last_name

    def put(self, first_name, last_name):
        new_name = request.get_json()
        student_dict = {}
        session = get_session()
        student = session.query(StudentModel).filter(StudentModel.first_name == first_name and StudentModel == last_name)
        return student

    # def delete(self, num):
    #     del student[num]
    #     return student
