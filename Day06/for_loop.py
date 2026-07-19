"""
Day 06 - For Loop
Author: Shivam Patel
Topic: Python For Loop
"""

# Print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Print even numbers
print("\nEven Numbers (1 to 20):")
for i in range(2, 21, 2):
    print(i)

# Multiplication Table
num = int(input("\nEnter a number: "))

print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
