import requests


def stutent_dict(students_list, first_name, last_name):
    students_dict = {}
    for i, student in enumerate(students_list):
        students_dict[i] = {"first_name": first_name, "last_name": last_name}
    return students_dict


def courses_dict(courses_list, course_name):
    courses_dict = {}
    for i, student in enumerate(courses_list):
        courses_dict[i] = {"course_name": course_name}
    return courses_dict






# def get_user_from_api():
#     first_name = input("User`s first name: ")
#     last_name = input("User`s last name: ")
#     url = f"http://127.0.0.1:5000/api/v1/student info/?first_name={first_name}&last_name={last_name}"