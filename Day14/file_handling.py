"""
Project : Daily Python Practice
Day     : 14
Topic   : File Handling
Author  : Shivam Patel
"""

# File name
file_name = "student_data.txt"

# 1. Write data to a file
with open(file_name, "w") as file:
    file.write("Student Information\n")
    file.write("-------------------\n")
    file.write("Name: Shivam Patel\n")
    file.write("Branch: AIML\n")
    file.write("Learning: Python\n")

print("✅ Data written successfully.")


# 2. Read data from the file
print("\n📖 File Content:")

with open(file_name, "r") as file:
    content = file.read()
    print(content)


# 3. Append new data
with open(file_name, "a") as file:
    file.write("Goal: AI Engineer\n")

print("✅ New data added successfully.")


# 4. Read updated file
print("\n📖 Updated File Content:")

with open(file_name, "r") as file:
    print(file.read())


# 5. Read file line by line
print("📋 Reading Line by Line:")

with open(file_name, "r") as file:
    for line in file:
        print("-", line.strip())







