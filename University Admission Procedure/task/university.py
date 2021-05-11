places = int(input())
students = []
departments_name = ["Biotech", "Chemistry", "Engineering", "Mathematics", "Physics"]
departments_name_with_number = {"Biotech": 0, "Chemistry": 1, "Engineering": 2, "Mathematics": 3, "Physics": 4}
position_of_points = {"Physics": [0, 2], "Chemistry": [1], "Mathematics": [2], "Engineering": [2, 3],
                      "Biotech": [0, 1]}  # Position in the file
places_in_each_departments = [places] * 5
with open("applicant_list.txt") as file:
    for line in file:
        students.append(line.split() + [""])

departments = []
answer = [[] for _ in range(5)]

for priority in range(7, 10):
    for department in departments_name:
        departments.append([student for student in students if student[priority] == department])
    students = []
    for name, department in zip(departments_name, departments):
        for student in department:
            student[10] = 0
            for point in position_of_points[name]:
                student[10] += int(student[2 + point])
            student[10] = max(round(student[10] / len(position_of_points[name]), 1), float(student[6]))
    for name, department in zip(departments_name, departments):
        department.sort(key=lambda x: (-x[10], x[0], x[1]))
    for number_of_department, department in enumerate(departments_name):
        for _ in range(len(departments[number_of_department])):
            if places_in_each_departments[number_of_department] > 0:
                student = departments[number_of_department].pop(0)
                answer[number_of_department].append(student[0:2] + [student[10]])
                places_in_each_departments[number_of_department] -= 1
            else:
                break
        students += departments[number_of_department]
    departments = []

for name, department in zip(departments_name, answer):
    department.sort(key=lambda x: (-x[2], x[0], x[1]))

for name, department in zip(departments_name, answer):
    with open("{}.txt".format(name).lower(), "w") as file:
        for student in department:
            file.write("{} {} {}\n".format(student[0], student[1], student[2]))
