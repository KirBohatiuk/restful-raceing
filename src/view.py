from flask_restful import Resource
from flask import request
from .db import create_student, get_session, StudentModel


class StudentInfo(Resource):
    def get(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            student_dict = {}

            session = get_session()
            students = session.query(StudentModel).filter(StudentModel.first_name == first_name).all()
            for i, student in enumerate(students):
                student_dict[i] = {"first_name": first_name, "last_name": last_name}
            return student_dict
        return "Invalid data"

    def post(self):
        user_info = request.get_json()
        first_name = user_info["first_name"]
        last_name = user_info["last_name"]
        session = get_session()
        student = create_student(first_name=first_name, last_name=last_name, session=session)
        return student.last_name

    def put(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            new_name = request.get_json()
            session = get_session()
            student = session.query(StudentModel).filter(StudentModel.first_name == first_name).first()
            student.first_name = new_name["first_name"]
            student.last_name = new_name["last_name"]
            session.commit()
            return student.first_name
        return "Invalid data"

    def delete(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            session = get_session()
            student = session.query(StudentModel).filter(StudentModel.first_name == first_name).first()
            session.delete(student)
            session.commit()
            return student.first_name
        return "Invalid data"
