import os
import matplotlib.pyplot as plt
import math

def find_student_id(name):
    with open("data/students.txt", "r") as file:
        output = ""
        for line in file:
            if name == line[3:-1]:
                for char in line:
                    if char in "1234567890":
                        output += char
                return output

def get_assignment_id(name):
    line_num = 0
    with open("data/assignments.txt", "r") as file:
        for line in file:
            if name == line[0:-1]:
                return file.readline()
            line_num += 1

def get_assignment_value(id):
    line_num = 0
    with open("data/assignments.txt", "r") as file:
        for line in file:
            if id in line:
                return int(file.readline())
            line_num += 1

def get_grade_student(id):
    output = 0
    for filename in os.listdir("data/submissions"):
        with open(f"data/submissions/{filename}", "r") as file:
            grade = file.read().split("|")
            if grade[0] == id:
                output += int(grade[2])/100*get_assignment_value(grade[1])/1000*100
    return round(output)

def get_grade_assignment(id):
    maximum = 0
    minimum = 100
    total = 0
    count = 0
    for filename in os.listdir("data/submissions"):
        with open(f"data/submissions/{filename}", "r") as file:
            grade = file.read().split("|")
            if grade[1] in id:
                total += int(grade[2])
                count += 1
                if int(grade[2]) <= minimum:
                    minimum = int(grade[2])
                if int(grade[2]) >= maximum:
                    maximum = int(grade[2])
    return math.trunc(total/count), maximum, minimum

def create_histogram(id):
    score_list = []
    for filename in os.listdir("data/submissions"):
        with open(f"data/submissions/{filename}", "r") as file:
            grade = file.read().split("|")
            if grade[1] in id:
                score_list.append(grade[2])
    score_list.sort()
    print(score_list)
    plt.hist(score_list, bins=10)
    plt.show()

def main():
    while True:
        print("1. Student grade")
        print("2. Assignment statistics")
        print("3. Assignment graph\n")
        choice = input("Enter your selection: ")
        if choice == "1":
            name = input("What is the student's name: ")
            grade = get_grade_student(find_student_id(name))
            if grade:
                print(f"{grade} %")
            else:
                print("Student not found")
        if choice == "2":
            name = input("What is the assignment name: ")
            assignment_id = get_assignment_id(name)
            if assignment_id:
                values = get_grade_assignment(assignment_id)
                print(f"Min: {values[2]}%")
                print(f"Avg: {values[0]}%")
                print(f"Max: {values[1]}%")
            else:
                print("Assignment not found")
        if choice == "3":
            name = input("What is the assignment name: ")
            assignment_id = get_assignment_id(name)
            if assignment_id:
                create_histogram(assignment_id)
            else:
                print("Assignment not found")
        print()


if __name__ == "__main__":
    main()