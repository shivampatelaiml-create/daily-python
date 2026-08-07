"""
Project : Daily Python Practice
Day     : 13
Topic   : Strings
Author  : Shivam Patel
"""

# Creating a String
name = "Shivam Patel"

print("Original Name:", name)

# String Length
print("\nLength:", len(name))

# Uppercase and Lowercase
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# Remove Extra Spaces
username = "   shivam_patell   "
print("\nBefore Strip:", username)
print("After Strip:", username.strip())

# Replace Text
message = "I am learning Java"
updated_message = message.replace("Java", "Python")

print("\nOriginal Message:", message)
print("Updated Message:", updated_message)

# Splitting a String
skills = "Python,HTML,CSS,JavaScript"

skill_list = skills.split(",")

print("\nSkills:")
for skill in skill_list:
    print("-", skill)

# Check String Content
email = input("\nEnter your email: ").strip()

if "@" in email and "." in email:
    print("Valid email format.")
else:
    print("Invalid email format.")

# String Slicing
text = "Artificial Intelligence"

print("\nOriginal Text:", text)
print("First 10 Characters:", text[:10])
print("Last 5 Characters:", text[-5:])

# Count Characters
print("Count of 'i':", text.lower().count("i"))

# f-string
age = 21
branch = "AIML"

profile = f"My name is {name}, I am {age} years old and I study {branch}."

print("\nProfile:")
print(profile)
