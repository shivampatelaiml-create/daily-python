"""
Project : Daily Python Practice
Day     : 10
Topic   : Tuples
Author  : Shivam Patel
"""

# Creating a Tuple
fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits Tuple:")
print(fruits)

# Accessing Elements
print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Length of Tuple
print("\nTotal Fruits:", len(fruits))

# Loop Through Tuple
print("\nAll Fruits:")
for fruit in fruits:
    print("-", fruit)

# Membership Test
search = input("\nEnter a fruit to search: ")

if search in fruits:
    print(search, "is available in the tuple.")
else:
    print(search, "is not available in the tuple.")

# Count Method
numbers = (10, 20, 30, 20, 40, 20)

print("\nCount of 20:", numbers.count(20))

# Index Method
print("Index of Mango:", fruits.index("Mango"))
