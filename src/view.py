from flask_restful import Resource
from flask import request

student = {
    1: "Dah",
    2: "Nah",
}


class ReadStudent(Resource):
    def get(self):
        if request.args.get("user_id"):
            user_id = int(request.args.get("user_id"))
            return student[user_id]
        return student

class CreateStudent(Resource):
    def post(self):
       username = request.get_json()
       student[max(student.keys()) + 1] = username
       return student

class UpdateStudent(Resource):
    def put(self, name):
        new_name = request.get_json()
        for num, name_dct in student.items():
            if name_dct == name:
                student[num] = new_name
        return student


class DeleteStudent(Resource):
    def delete(self, num):
        del student[num]
        return student
