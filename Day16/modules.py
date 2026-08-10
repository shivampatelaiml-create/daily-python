"""
Project : Daily Python Practice
Day     : 16
Topic   : Modules
Author  : Shivam Patel
"""

import calculator
import math
import random


# Custom Module
a = 20
b = 5

print("=== Custom Calculator Module ===")

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiply(a, b))
print("Division:", calculator.divide(a, b))


# Math Module
print("\n=== Math Module ===")

number = 25

print("Square Root:", math.sqrt(number))
print("Power:", math.pow(2, 3))
print("Value of Pi:", math.pi)


# Random Module
print("\n=== Random Module ===")

random_number = random.randint(1, 100)

print("Random Number:", random_number)
