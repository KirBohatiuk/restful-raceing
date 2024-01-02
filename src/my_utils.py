



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
