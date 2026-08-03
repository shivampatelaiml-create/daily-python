"""
Project : Daily Python Practice
Day     : 11
Topic   : Dictionaries
Author  : Shivam Patel
"""

# Creating a Dictionary
student = {
    "name": "Shivam Patel",
    "age": 21,
    "branch": "AIML",
    "college": "BGI",
    "cgpa": 8.5
}

print("Student Details:")
print(student)

# Accessing Values
print("\nName:", student["name"])
print("Branch:", student["branch"])

# Adding a New Key-Value Pair
student["city"] = "Vidisha"

print("\nAfter Adding City:")
print(student)

# Updating a Value
student["cgpa"] = 9.0

print("\nAfter Updating CGPA:")
print(student)

# Removing a Key
student.pop("age")

print("\nAfter Removing Age:")
print(student)

# Loop Through Dictionary
print("\nDictionary Data:")

for key, value in student.items():
    print(f"{key} : {value}")

# Checking if Key Exists
key = input("\nEnter a key to search: ")

if key in student:
    print(f"{key} = {student[key]}")
else:
    print("Key Not Found!")

# Total Keys
print("\nTotal Keys:", len(student))
