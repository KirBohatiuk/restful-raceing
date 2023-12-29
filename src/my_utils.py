



def stutent_dict(students_list, first_name, last_name):
    student_dict = {}
    for i, student in enumerate(students_list):
        student_dict[i] = {"first_name": first_name, "last_name": last_name}
    return student_dict