from flask_restful import Resource
from flask import request, abort, render_template
from .db import create_student, get_session, StudentModel, create_course, add_student_to_course, CourseModel
from . import my_utils

class StudentInfo(Resource):
    def get(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            session = get_session()
            students = session.query(StudentModel).filter(StudentModel.first_name == first_name).all()
            student_dict = my_utils.stutent_dict(students, first_name, last_name)
            if student_dict == {}:
                abort(404)
            return student_dict
        return abort(404)

    def post(self):
        try:
            user_info = request.get_json()
            first_name = user_info["first_name"]
            last_name = user_info["last_name"]
        except:
            abort(404)
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


class CourseInfo(Resource):
    def get(self):
        if request.args.get("course_name"):
            course_name = request.args.get("course_name")
            session = get_session()
            courses = session.query(CourseModel).filter(CourseModel.course_name == course_name).all()
            students_dict = my_utils.courses_dict(courses, course_name)
            if students_dict == {}:
                abort(404)
            return students_dict
        return "Invalid data"

    def post(self):
        course_info = request.get_json()
        course_name = course_info["course_name"]
        course_description = course_info["course_description"]
        print(course_name)
        session = get_session()
        course = create_course(course_name=course_name, course_description=course_description, session=session)
        return course.course_name

    def put(self):
        if request.args.get("course_name"):
            course_name = request.args.get("course_name")
            new_course_info = request.get_json()
            session = get_session()
            courses = session.query(CourseModel).filter(CourseModel.course_name == course_name).first()
            courses.course_name = new_course_info["new_course_name"]
            courses.course_description = new_course_info["new_course_description"]
            session.commit()
            return courses.course_name
        return "Invalid data"

    def delete(self):
        if request.args.get("course_name"):
            course_name = request.args.get("course_name")
            session = get_session()
            course = session.query(CourseModel).filter(CourseModel.course_name == course_name).first()
            session.delete(course)
            session.commit()
            return course.course_name
        return "Invalid data"


class StudentCourseMod(Resource):
    def post(self):
        course_info = request.get_json()
        user_info = request.get_json()
        first_name = user_info["first_name"]
        last_name = user_info["last_name"]
        course_name = course_info["course_name"]
        print(first_name, last_name, course_name)
        session = get_session()
        student = session.query(StudentModel).filter(
            StudentModel.first_name == first_name,
            StudentModel.last_name == last_name
        ).first()
        course = session.query(CourseModel).filter(CourseModel.course_name == course_name).first()
        student.courses_id.append(course)
        session.commit()
        return "hi"