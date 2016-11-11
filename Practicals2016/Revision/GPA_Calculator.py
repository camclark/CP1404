"""
<50 = N, 50-64 = P, 65-74 = C, 75-84 = D, >= 85 = HD.
(Floats should be handled, e.g. 74.95 is a C.)
"""

__author__ = "Cameron Clark"


def find_grade_and_point(score):
    if score < 50:
        grade = "F"
        point = 0
    elif score <= 64:
        grade = "P"
        point = 4
    elif score <= 74:
        grade = "C"
        point = 5
    elif score <= 84:
        grade = "D"
        point = 6
    else:
        grade = "HD"
        point = 7

    return grade, point

with open("gpa.txt", "r") as in_file:
    all_marks = []
    all_subjects = []
    for line in in_file:
        subject, mark = line.strip().split(",")
        all_marks.append(float(mark))
        all_subjects.append(subject)

    grade_total = 0
    for i, mark in enumerate(all_marks):
        grade, point = find_grade_and_point(mark)
        grade_total += point
        print("For {} you achieved a {} with {}%".format(all_subjects[i-1], grade, all_marks[i-1]))

    print("\nYour gpa is {:.2f}".format(grade_total/i))
