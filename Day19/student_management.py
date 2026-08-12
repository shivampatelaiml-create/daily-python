"""
Project : Daily Python Practice
Day     : 19
Topic   : OOP Practical Project
Author  : Shivam Patel

Project:
Student Management System
"""


# Parent Class
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child Class
class Student(Person):

    def __init__(self, name, age, branch, roll_number):
        super().__init__(name, age)

        self.branch = branch
        self.roll_number = roll_number
        self.__marks = []

    # Add marks
    def add_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks.append(marks)
        else:
            print("Invalid marks. Enter marks between 0 and 100.")

    # Calculate average
    def calculate_average(self):
        if not self.__marks:
            return 0

        return sum(self.__marks) / len(self.__marks)

    # Display student details
    def show_details(self):
        print("\n========== STUDENT DETAILS ==========")

        self.show_person_details()

        print(f"Branch: {self.branch}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.__marks}")
        print(f"Average: {self.calculate_average():.2f}")


# Creating Student Objects

student1 = Student(
    "Shivam Patel",
    20,
    "AI/ML",
    "AIML001"
)

student2 = Student(
    "Rahul Sharma",
    20,
    "Computer Science",
    "CS002"
)


# Adding Marks

student1.add_marks(85)
student1.add_marks(90)
student1.add_marks(78)

student2.add_marks(72)
student2.add_marks(88)
student2.add_marks(80)


# Display Details

student1.show_details()
student2.show_details()
