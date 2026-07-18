# Day 04 - If Else Statements

age = int(input("Enter your age: "))

if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote.")


# Check Even or Odd Number
number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print(number, "is an Even Number.")
else:
    print(number, "is an Odd Number.")


# Find the Greater Number
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a)
