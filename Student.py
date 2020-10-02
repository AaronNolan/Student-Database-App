#!/usr/bin/env python

import random


class Student:

    def __init__(self):
        self.costofcourse = 600
        self.id = 1000
        self.courses = ""
        self.firstname = ""
        self.lastname = ""
        self.gradeyear = 0
        self.tuitionbalance = 0
        self.studentid = Student._setstudentid(self)

    def _setstudentid(self):
        self.id += 1
        return str(str(self.gradeyear) + "" + str(self.id))

    def student(self):
        self.firstname = input("Student's First Name: ")
        self.lastname = input("Student's Last Name: ")
        self.gradeyear = input("Student's Course Year: ")

    def enroll(self):
        while True:
            course = input("Enter course to enroll (Q to quit): ")
            if course != "Q":
                self.courses += "\n" + course
                self.tuitionbalance += self.costofcourse
            else:
                break

    def viewbalance(self):
        print("Your balance is €" + str(self.tuitionbalance))

    def paytuition(self):
        self.viewbalance()
        payment = int(input("Enter the payment amount: "))
        self.tuitionbalance -= payment
        print("Thank you for your payment of €" + str(self.tuitionbalance))

    def showinfo(self):
        return "Student Name: " + self.firstname + " " + self.lastname + \
               "\nStudent ID: " + self.studentid + \
               "\nCourses Enrolled:" + self.courses + \
               "\nBalance: €" + str(self.tuitionbalance)
