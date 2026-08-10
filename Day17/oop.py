"""
Project : Daily Python Practice
Day     : 17
Topic   : Object-Oriented Programming
Author  : Shivam Patel
"""


# Class
class Student:

    # Constructor
    def __init__(self, name, branch, year):
        self.name = name
        self.branch = branch
        self.year = year

    # Method
    def introduce(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am studying {self.branch}.")
        print(f"I am currently in year {self.year}.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")


# Creating Objects
student1 = Student("Shivam", "AI/ML", 2)
student2 = Student("Rahul", "Computer Science", 2)


# Using Object 1
print("=== Student 1 ===")
student1.introduce()
student1.study("Python")


# Using Object 2
print("\n=== Student 2 ===")
student2.introduce()
student2.study("Data Structures")
