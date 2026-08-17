"""
Project : Daily Python Practice
Day     : 22
Topic   : NumPy Indexing, Slicing and Reshaping
Author  : Shivam Patel
"""

import numpy as np


# ==========================================================
# 1. 1D ARRAY INDEXING
# ==========================================================

numbers = np.array([10, 20, 30, 40, 50, 60])

print("=== 1D Array ===")
print("Array:", numbers)

print("\nFirst Element:", numbers[0])
print("Third Element:", numbers[2])
print("Last Element:", numbers[-1])


# ==========================================================
# 2. 1D ARRAY SLICING
# ==========================================================

print("\n=== 1D Slicing ===")

print("First Three:", numbers[:3])
print("Elements 2 to 5:", numbers[1:5])
print("Last Three:", numbers[-3:])
print("Every Second Element:", numbers[::2])


# ==========================================================
# 3. 2D ARRAY
# ==========================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n=== 2D Array ===")
print(matrix)


# ==========================================================
# 4. 2D ARRAY INDEXING
# ==========================================================

print("\n=== 2D Indexing ===")

print("First Row:", matrix[0])
print("Second Row:", matrix[1])

print("First Column:", matrix[:, 0])

print("Element at Row 2, Column 3:", matrix[1, 2])
print("Element at Row 3, Column 1:", matrix[2, 0])


# ==========================================================
# 5. 2D ARRAY SLICING
# ==========================================================

print("\n=== 2D Slicing ===")

print("First Two Rows:")
print(matrix[:2])

print("\nFirst Two Columns:")
print(matrix[:, :2])

print("\nTop-Left 2x2 Matrix:")
print(matrix[:2, :2])


# ==========================================================
# 6. RESHAPE
# ==========================================================

numbers = np.arange(1, 13)

print("\n=== Reshape ===")

print("Original Array:")
print(numbers)

matrix_3x4 = numbers.reshape(3, 4)

print("\n3 x 4 Matrix:")
print(matrix_3x4)

matrix_4x3 = numbers.reshape(4, 3)

print("\n4 x 3 Matrix:")
print(matrix_4x3)


# ==========================================================
# 7. FLATTEN
# ==========================================================

print("\n=== Flatten ===")

flattened = matrix.flatten()

print("Original Matrix:")
print(matrix)

print("\nFlattened Array:")
print(flattened)


# ==========================================================
# 8. TRANSPOSE
# ==========================================================

print("\n=== Transpose ===")

print("Original Matrix:")
print(matrix)

print("\nTransposed Matrix:")
print(matrix.T)


# ==========================================================
# 9. PRACTICAL ML-STYLE EXAMPLE
# ==========================================================

# Rows = Students
# Columns = [Maths, Python, ML]

marks = np.array([
    [85, 90, 88],
    [72, 80, 75],
    [95, 92, 96],
    [60, 70, 65]
])

print("\n=== Student Marks Dataset ===")
print(marks)

print("\nPython Marks:")
print(marks[:, 1])

print("\nML Marks:")
print(marks[:, 2])

print("\nAverage Marks of Each Student:")
print(np.mean(marks, axis=1))

print("\nAverage Marks of Each Subject:")
print(np.mean(marks, axis=0))
