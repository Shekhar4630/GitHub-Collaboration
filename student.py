class Student:
    def welcome(self):
    print("Welcome to Student Management System!")

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)


student1 = Student("Shekhar", 101)

student1.display_details()