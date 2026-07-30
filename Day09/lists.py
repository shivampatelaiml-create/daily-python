"""
Project : Daily Python Practice
Day     : 09
Topic   : Lists
Author  : Shivam Patel
"""

# Creating a List
languages = ["Python", "Java", "C++", "JavaScript"]

print("Programming Languages:")
print(languages)

# Accessing Elements
print("\nFirst Language:", languages[0])
print("Last Language:", languages[-1])

# Adding an Element
languages.append("Go")
print("\nAfter Adding Go:")
print(languages)

# Removing an Element
languages.remove("Java")
print("\nAfter Removing Java:")
print(languages)

# Updating an Element
languages[1] = "C#"
print("\nAfter Updating C++ to C#:")
print(languages)

# Loop Through List
print("\nAll Languages:")
for language in languages:
    print("-", language)

# Length of List
print("\nTotal Languages:", len(languages))
