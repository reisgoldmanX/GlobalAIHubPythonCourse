"""
Homework 3

Create 5 students. Ask these students from the user.
Each of these students should have midterm grade, project grade, and final grade.
Each student will have a course passing grade.
passingGrade = midterm * (0.3) + project * (0.3) + final * (0.4) passing grade should be determined like this.
Create a dictionary that keeps these students information.
Calculate the students grades and transfer them to the list with the help of indexing.
Finally, set the students with the Highest grade to be in the first index and student with the lowest grade to be in the last index of the list.
"""


def student_grade():  # Asking student information from user.
    name = str(input("Enter student name:\t"))
    midterm = float(input("Enter midterm grade:\t"))
    project = float(input("Enter project grade:\t"))
    final = float(input("Enter final grade:\t"))
    passing_grade = midterm * 0.3 + project * 0.3 + final * 0.4  # Calculating passing grade
    return name, midterm, project, final, passing_grade


def student_info(student_tuple):  # Creating a dictionary that keeps students information
    info = {"Name": student_tuple[0],
            "Midterm": student_tuple[1],
            "Project": student_tuple[2],
            "Final": student_tuple[3],
            "Passing Grade": student_tuple[4]}
    return info


stud_l = []


def student_list(student_dict):  # Passing student dictionaries to the list
    stud_l.append(student_dict)
    new = sorted(stud_l, key=lambda k: k["Passing Grade"], reverse=True)  # Sorting the list
    return new


for i in range(0, 6):
    student_list(student_info(student_grade()))
