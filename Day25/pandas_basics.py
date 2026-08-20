"""
Project : Daily Python Practice
Day     : 25
Topic   : Pandas Basics
Author  : Shivam Patel
"""

import pandas as pd


# ==========================================================
# 1. CREATE A PANDAS SERIES
# ==========================================================

marks = pd.Series([85, 90, 78, 92, 88])

print("=== Pandas Series ===")
print(marks)


# ==========================================================
# 2. CREATE A DATAFRAME
# ==========================================================

data = {
    "Name": ["Shivam", "Rahul", "Priya", "Aman", "Neha"],
    "Age": [20, 21, 20, 22, 21],
    "Branch": ["AI/ML", "CSE", "AI/ML", "CSE", "AI/ML"],
    "Marks": [85, 78, 92, 65, 88]
}

df = pd.DataFrame(data)

print("\n=== Student DataFrame ===")
print(df)


# ==========================================================
# 3. VIEW COLUMNS
# ==========================================================

print("\n=== Columns ===")
print(df.columns)


# ==========================================================
# 4. VIEW FIRST ROWS
# ==========================================================

print("\n=== First 3 Rows ===")
print(df.head(3))


# ==========================================================
# 5. VIEW LAST ROWS
# ==========================================================

print("\n=== Last 2 Rows ===")
print(df.tail(2))


# ==========================================================
# 6. DATAFRAME INFORMATION
# ==========================================================

print("\n=== DataFrame Information ===")

print("Shape:", df.shape)
print("Number of Rows:", len(df))
print("Number of Columns:", len(df.columns))


# ==========================================================
# 7. SELECT A COLUMN
# ==========================================================

print("\n=== Marks Column ===")
print(df["Marks"])


# ==========================================================
# 8. SELECT MULTIPLE COLUMNS
# ==========================================================

print("\n=== Name and Marks ===")
print(df[["Name", "Marks"]])


# ==========================================================
# 9. FILTER DATA
# ==========================================================

print("\n=== Students with Marks >= 80 ===")

high_scorers = df[df["Marks"] >= 80]

print(high_scorers)


# ==========================================================
# 10. FILTER BY BRANCH
# ==========================================================

print("\n=== AI/ML Students ===")

aiml_students = df[df["Branch"] == "AI/ML"]

print(aiml_students)


# ==========================================================
# 11. BASIC STATISTICS
# ==========================================================

print("\n=== Statistics ===")

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("Total Marks:", df["Marks"].sum())


# ==========================================================
# 12. SORT DATA
# ==========================================================

print("\n=== Students Sorted by Marks ===")

sorted_students = df.sort_values("Marks", ascending=False)

print(sorted_students)


# ==========================================================
# 13. DESCRIBE DATA
# ==========================================================

print("\n=== Statistical Summary ===")

print(df.describe())
