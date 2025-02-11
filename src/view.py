from flask_restful import Resource
from flask import request, abort, render_template, Blueprint, jsonify
from .db import (create_student, get_session, StudentModel, create_course,
                 add_student_to_course, remove_student_from_course,
                 add_student_to_course, CourseModel, get_student,
                 change_student_info, get_course, change_course_info,
                 remove_student, remove_course, get_student_by_id, get_all_courses)
from . import my_utils
import requests


class StudentInfo(Resource):
    def get(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            session = get_session()
            student = get_student(first_name, last_name, session)
            return student.first_name
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
            student = get_student(first_name, last_name, session)
            student = change_student_info(new_name, student, session)
            return student.first_name
        return abort(404)

    def delete(self):
        if request.args.get("first_name") and request.args.get("last_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            session = get_session()
            student = get_student(first_name, last_name, session)
            student = remove_student(session, student)
            return student.first_name
        elif request.args.get("student_id"):
            student_id = int(request.args.get("student_id"))
            session = get_session()
            student = get_student_by_id(student_id, session)
            student = remove_student(session, student)
            return student.first_name
        return abort(404)


class CourseInfo(Resource):
    def get(self):
        if request.args.get("course_name"):
            course_name = request.args.get("course_name")
            session = get_session()
            course = get_course(course_name, session)
            return course.name
        return abort(404)

    def post(self):
        course_info = request.get_json()
        try:
            course_name = course_info["course_name"]
            course_description = course_info["course_description"]
        except:
            abort(404)
        session = get_session()
        course = create_course(name=course_name, description=course_description, session=session)
        return course.name

    def put(self):
        if request.args.get("course_name"):
            course_name = request.args.get("course_name")
            course_info = request.get_json()
            session = get_session()
            course = get_course(course_name, session)
            course = change_course_info(course_info, course, session)
            return course.name
        return abort(404)

    def delete(self):
        if request.args.get("course_name"):
            course_name = request.args.get("course_name")
            session = get_session()
            course = get_course(course_name, session)
            course = remove_course(session, course)
            return course.name
        return abort(404)


class StudentCourseMod(Resource):
    def post(self):
        course_info = request.get_json()
        user_info = request.get_json()
        try:
            first_name = user_info["first_name"]
            last_name = user_info["last_name"]
            course_name = course_info["course_name"]
        except:
            abort(404)
        session = get_session()
        student = get_student(first_name, last_name, session)
        course = get_course(course_name, session)
        student = add_student_to_course(session, student, course)
        return student.first_name


    def delete(self):
        if request.args.get("first_name") and request.args.get("last_name") and request.args.get("course_name"):
            first_name = request.args.get("first_name")
            last_name = request.args.get("last_name")
            course_name = request.args.get("course_name")
            session = get_session()
            student = get_student(first_name, last_name, session)
            course = get_course(course_name, session)
            student = remove_student_from_course(session, student, course)
        else:
            return abort(404)
        return student.first_name


class AllStudentsInCourse(Resource):
    def get(self):
        if request.args.get("course_name"):
            students_list = []
            course_name = request.args.get("course_name")
            session = get_session()
            course = get_course(course_name, session)
            students = course.course_users_id
            for student in students:
                students_list.append(f"{student.first_name} {student.last_name}")
        else:
            return abort(404)
        return students_list


class CourseWithSomeStudents(Resource):
    def get(self):
        if request.args.get("students_amount"):
            max_students = int(request.args.get("students_amount"))
            courses_list = []
            session = get_session()
            courses = get_all_courses(session)
            for course in courses:
                if len(course.course_users_id) <= max_students:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        courses_list.append(course.name)
            return courses_list


bp = Blueprint("send", __name__, url_prefix="/send")


@bp.route("/student/")
def send_student_to_api():
    first_name = input("User`s first name: ")
    last_name = input("User`s last name: ")
    session = get_session()
    student = create_student(first_name=first_name, last_name=last_name, session=session)
    return student.first_name


@bp.route("/course/")
def send_course_to_api():
    course_name = input("course`s course name: ")
    course_description = input("course`s description: ")
    session = get_session()
    course = create_course(name=course_name, description=course_description, session=session)
    return course.name
