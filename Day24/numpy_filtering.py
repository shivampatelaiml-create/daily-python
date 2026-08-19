"""
Project : Daily Python Practice
Day     : 24
Topic   : NumPy Random, Boolean Masking and Data Filtering
Author  : Shivam Patel
"""

import numpy as np


# ==========================================================
# 1. RANDOM NUMBERS
# ==========================================================

print("=== Random Numbers ===")

random_numbers = np.random.randint(1, 101, 10)

print("Random Numbers:")
print(random_numbers)


# ==========================================================
# 2. RANDOM DECIMAL VALUES
# ==========================================================

print("\n=== Random Decimal Values ===")

random_values = np.random.rand(5)

print(random_values)


# ==========================================================
# 3. BOOLEAN MASKING
# ==========================================================

numbers = np.array([10, 25, 40, 55, 70, 85, 90])

print("\n=== Boolean Masking ===")

mask = numbers > 50

print("Numbers:", numbers)
print("Mask:", mask)


# ==========================================================
# 4. FILTERING DATA
# ==========================================================

print("\n=== Data Filtering ===")

greater_than_50 = numbers[numbers > 50]

print("Numbers greater than 50:")
print(greater_than_50)


# ==========================================================
# 5. MULTIPLE CONDITIONS
# ==========================================================

print("\n=== Multiple Conditions ===")

between_30_and_80 = numbers[
    (numbers >= 30) & (numbers <= 80)
]

print("Numbers between 30 and 80:")
print(between_30_and_80)


# ==========================================================
# 6. EVEN NUMBER FILTER
# ==========================================================

print("\n=== Even Numbers ===")

even_numbers = numbers[numbers % 2 == 0]

print("Even Numbers:")
print(even_numbers)


# ==========================================================
# 7. ML-STYLE STUDENT DATASET
# ==========================================================

marks = np.array([
    [85, 90, 88],
    [72, 80, 75],
    [95, 92, 96],
    [60, 70, 65],
    [45, 55, 50],
    [88, 85, 90]
])

print("\n=== Student Marks Dataset ===")

print("Dataset:")
print(marks)


# ==========================================================
# 8. STUDENTS WITH HIGH ML MARKS
# ==========================================================

ml_marks = marks[:, 2]

high_ml_students = marks[ml_marks >= 80]

print("\nStudents with ML marks >= 80:")
print(high_ml_students)


# ==========================================================
# 9. STUDENTS WITH AVERAGE >= 80
# ==========================================================

student_average = np.mean(marks, axis=1)

top_students = marks[student_average >= 80]

print("\nStudent Averages:")
print(student_average)

print("\nStudents with Average >= 80:")
print(top_students)


# ==========================================================
# 10. RANDOM DATASET
# ==========================================================

print("\n=== Random ML-Style Dataset ===")

dataset = np.random.randint(1, 101, (5, 3))

print("Dataset:")
print(dataset)

print("\nValues greater than 70:")
print(dataset[dataset > 70])
