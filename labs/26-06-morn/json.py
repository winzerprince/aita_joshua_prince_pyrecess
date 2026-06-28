import json

with open("students.json", "r") as file:
    students_dict = json.load(file)

    print(students_dict)
