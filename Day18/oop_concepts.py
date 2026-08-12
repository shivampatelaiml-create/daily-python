"""
Project : Daily Python Practice
Day     : 18
Topic   : OOP Concepts
Author  : Shivam Patel

Concepts:
1. Inheritance
2. Encapsulation
3. Polymorphism
"""


# ==========================================================
# 1. INHERITANCE
# ==========================================================

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Student(Person):

    def study(self):
        print(f"{self.name} is studying Python.")


print("=== Inheritance ===")

student = Student("Shivam")

student.introduce()
student.study()


# ==========================================================
# 2. ENCAPSULATION
# ==========================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")

    def get_balance(self):
        return self.__balance


print("\n=== Encapsulation ===")

account = BankAccount("Shivam", 5000)

account.deposit(2000)

print("Account Owner:", account.owner)
print("Balance:", account.get_balance())


# ==========================================================
# 3. POLYMORPHISM
# ==========================================================

class Dog:

    def sound(self):
        print("Dog says: Woof!")


class Cat:

    def sound(self):
        print("Cat says: Meow!")


print("\n=== Polymorphism ===")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
