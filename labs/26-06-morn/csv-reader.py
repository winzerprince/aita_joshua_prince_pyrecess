import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# add to to csv you details

with open("students.csv", "a") as file:
    writer = csv.writer(file)

    details = {
        "RegistrationNo": "24/U/0128",
        "Name": "Aita Joshua Prince",
        "Gender": "Male",
        "Age": 22,
        "Course": "BSSE",
        "Score": 100000,
    }
