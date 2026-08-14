"""
Project : Daily Python Practice
Day     : 20
Topic   : List Comprehension, Lambda, Map, Filter & Reduce
Author  : Shivam Patel
"""


# ==========================================================
# 1. LIST COMPREHENSION
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

print("=== List Comprehension ===")
print("Numbers:", numbers)
print("Squares:", squares)


# Filter even numbers
even_numbers = [number for number in numbers if number % 2 == 0]

print("Even Numbers:", even_numbers)


# ==========================================================
# 2. LAMBDA FUNCTION
# ==========================================================

square = lambda x: x ** 2
multiply = lambda x, y: x * y

print("\n=== Lambda Functions ===")

print("Square of 7:", square(7))
print("5 × 6:", multiply(5, 6))


# ==========================================================
# 3. MAP FUNCTION
# ==========================================================

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print("\n=== Map Function ===")

print("Original:", numbers)
print("Squared:", squared_numbers)


# ==========================================================
# 4. FILTER FUNCTION
# ==========================================================

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("\n=== Filter Function ===")

print("Original:", numbers)
print("Even Numbers:", even_numbers)


# ==========================================================
# 5. REDUCE FUNCTION
# ==========================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda x, y: x + y,
    numbers
)

print("\n=== Reduce Function ===")

print("Numbers:", numbers)
print("Sum:", total)


# ==========================================================
# 6. PRACTICAL EXAMPLE
# ==========================================================

marks = [45, 78, 92, 56, 88, 34, 95]

passed_students = list(
    filter(lambda marks: marks >= 50, marks)
)

updated_marks = list(
    map(lambda marks: marks + 5, marks)
)

print("\n=== Practical Example ===")

print("Original Marks:", marks)
print("Passed Marks:", passed_students)
print("Marks After Bonus:", updated_marks)
