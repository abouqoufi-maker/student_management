students_num = int(input("enter the number of students: "))
students = {}

for x in range(students_num):
    name = input("enter the name of the student: ")
    math_note = float(input("enter the math note of the student: "))
    python_note = float(input("enter the python note of the student: "))
    physics_note = float(input("enter the physics note of the student: "))

    admission_point =  (math_note * 2 + python_note * 3 + physics_note * 1) / 6

    if admission_point < 10:
        status = "Not admitted"
    else:
        status = "Admitted"

    students[name] = {
                "math": math_note,
                "python": python_note,
                "physics": physics_note,
                "status": status,
                "score": admission_point
                }

    #for keys, values in students.items():
    #    print(f"{keys} : {values}", end=", ")

    if admission_point < 10:
        print(f"{name} is {status}")
        print(f"{name} result is {admission_point:.3f}")
    else:
        print(f"{name} is {status}")
        print(f"{name} result is {admission_point:.3f}")
    

print("---------STUDENT REPORT---------")

for key, value in students.items():
    print(f"\n{key} : \n{value}")


total_average = 0
admitted = 0
not_admitted = 0

best_student = ""
best_average = 0

for name, student in students.items():
    average = student["score"]
    total_average += average

    if student["status"] == "Admitted":
        admitted += 1
    else:
        not_admitted += 1

    if average > best_average:
        best_average = average
        best_student = name

class_average = total_average / students_num

print("\n========== CLASS STATISTICS ==========")

print(f"Number of students: {students_num}")
print(f"Class average: {class_average:.3f}")
print(f"Best student: {best_student}")
print(f"Best average: {best_average:.3f}")
print(f"Admitted: {admitted}")
print(f"Not admitted: {not_admitted}")
