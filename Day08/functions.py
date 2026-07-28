"""
Project : Daily Python Practice
Day     : 08
Topic   : Functions
Author  : Shivam Patel
"""

# Function without parameters
def welcome():
    print("Welcome to Python Functions!")


# Function with parameters
def greet(name):
    print(f"Hello, {name}! 👋")


# Function with return value
def add(a, b):
    return a + b


# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


# Calling Functions
welcome()

name = input("\nEnter your name: ")
greet(name)

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print("Sum =", result)

number = int(input("\nEnter a number: "))
print(check_even_odd(number))
