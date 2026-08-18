"""
Project : Daily Python Practice
Day     : 23
Topic   : NumPy Mathematical and Statistical Operations
Author  : Shivam Patel
"""

import numpy as np


# ==========================================================
# 1. BASIC MATHEMATICAL OPERATIONS
# ==========================================================

numbers = np.array([10, 20, 30, 40, 50])

print("=== Basic Mathematical Operations ===")

print("Original:", numbers)
print("Add 5:", numbers + 5)
print("Subtract 5:", numbers - 5)
print("Multiply by 2:", numbers * 2)
print("Divide by 10:", numbers / 10)


# ==========================================================
# 2. STATISTICAL OPERATIONS
# ==========================================================

print("\n=== Statistical Operations ===")

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Median:", np.median(numbers))
print("Minimum:", np.min(numbers))
print("Maximum:", np.max(numbers))
print("Standard Deviation:", np.std(numbers))
print("Variance:", np.var(numbers))


# ==========================================================
# 3. MATRIX ADDITION
# ==========================================================

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("\n=== Matrix Addition ===")

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

print("\nA + B:")
print(matrix_a + matrix_b)


# ==========================================================
# 4. MATRIX MULTIPLICATION
# ==========================================================

print("\n=== Matrix Multiplication ===")

print("A × B:")
print(np.matmul(matrix_a, matrix_b))


# ==========================================================
# 5. DOT PRODUCT
# ==========================================================

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print("\n=== Dot Product ===")

dot_product = np.dot(vector_a, vector_b)

print("Vector A:", vector_a)
print("Vector B:", vector_b)
print("Dot Product:", dot_product)


# ==========================================================
# 6. POWER AND SQUARE ROOT
# ==========================================================

values = np.array([4, 9, 16, 25])

print("\n=== Power and Square Root ===")

print("Values:", values)
print("Square:", np.power(values, 2))
print("Square Root:", np.sqrt(values))


# ==========================================================
# 7. ROUNDING
# ==========================================================

decimal_values = np.array([
    2.3456,
    5.7891,
    9.1234
])

print("\n=== Rounding ===")

print("Original:", decimal_values)
print("Rounded:", np.round(decimal_values, 2))


# ==========================================================
# 8. ML-STYLE DATASET ANALYSIS
# ==========================================================

marks = np.array([
    [85, 90, 88],
    [72, 80, 75],
    [95, 92, 96],
    [60, 70, 65]
])

print("\n=== ML-Style Dataset ===")

print("Dataset:")
print(marks)

print("\nOverall Mean:", np.mean(marks))

print("Subject-wise Mean:")
print(np.mean(marks, axis=0))

print("Student-wise Mean:")
print(np.mean(marks, axis=1))

print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
