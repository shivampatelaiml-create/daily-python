"""
Project : Daily Python Practice
Day     : 21
Topic   : NumPy Basics
Author  : Shivam Patel
"""

import numpy as np


# ==========================================================
# 1. CREATE NUMPY ARRAY
# ==========================================================

numbers = np.array([10, 20, 30, 40, 50])

print("=== NumPy Array ===")
print("Array:", numbers)
print("Type:", type(numbers))


# ==========================================================
# 2. ARRAY PROPERTIES
# ==========================================================

print("\n=== Array Properties ===")

print("Dimensions:", numbers.ndim)
print("Shape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)


# ==========================================================
# 3. ARRAY OPERATIONS
# ==========================================================

print("\n=== Array Operations ===")

print("Addition:", numbers + 10)
print("Subtraction:", numbers - 5)
print("Multiplication:", numbers * 2)
print("Division:", numbers / 10)


# ==========================================================
# 4. STATISTICAL OPERATIONS
# ==========================================================

print("\n=== Statistical Operations ===")

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
print("Standard Deviation:", np.std(numbers))


# ==========================================================
# 5. 2D ARRAY
# ==========================================================

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n=== 2D Array ===")
print(matrix)

print("Dimensions:", matrix.ndim)
print("Shape:", matrix.shape)


# ==========================================================
# 6. INDEXING
# ==========================================================

print("\n=== Indexing ===")

print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

print("First Row:", matrix[0])
print("Element at Row 2, Column 3:", matrix[1, 2])


# ==========================================================
# 7. SLICING
# ==========================================================

print("\n=== Slicing ===")

print("First Three Elements:", numbers[:3])
print("Last Two Elements:", numbers[-2:])


# ==========================================================
# 8. SPECIAL ARRAYS
# ==========================================================

print("\n=== Special Arrays ===")

zeros = np.zeros(5)
ones = np.ones(5)

print("Zeros:", zeros)
print("Ones:", ones)

sequence = np.arange(1, 11)

print("Sequence:", sequence)
