#!/usr/bin/env python

from Student import *

students = []
n = int(input("Emter number of students to be enrolled: "))
for i in range(n):
    students.append(Student())

for i in range(len(students)):
    students[i].student()
    students[i].enroll()
    students[i].paytuition()

for i in range(len(students)):
    print(students[i].showinfo())
