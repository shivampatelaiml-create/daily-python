"""
Project : Daily Python Practice
Day     : 12
Topic   : Sets
Author  : Shivam Patel
"""

# Creating a Set
languages = {"Python", "Java", "C++", "Python", "JavaScript"}

print("Programming Languages:")
print(languages)

# Adding an Element
languages.add("Go")

print("\nAfter Adding Go:")
print(languages)

# Removing an Element
languages.remove("Java")

print("\nAfter Removing Java:")
print(languages)

# Checking if an Element Exists
search = input("\nEnter a language to search: ")

if search in languages:
    print(f"{search} is available.")
else:
    print(f"{search} is not available.")

# Loop Through Set
print("\nAvailable Languages:")
for language in languages:
    print("-", language)

# Length of Set
print("\nTotal Languages:", len(languages))

# Creating Another Set
backend = {"Python", "Java", "PHP", "Go"}

# Union
print("\nUnion:")
print(languages.union(backend))

# Intersection
print("\nIntersection:")
print(languages.intersection(backend))

# Difference
print("\nDifference:")
print(languages.difference(backend))
