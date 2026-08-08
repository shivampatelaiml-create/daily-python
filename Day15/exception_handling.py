"""
Project : Daily Python Practice
Day     : 15
Topic   : Exception Handling
Author  : Shivam Patel
"""

# Basic Try-Except
print("=== Basic Exception Handling ===")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("❌ Invalid input! Please enter a valid number.")


# Handling Division by Zero
print("\n=== Division Calculator ===")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("❌ Please enter numbers only.")

except ZeroDivisionError:
    print("❌ Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("✅ Division operation completed.")


# Multiple Exception Handling
print("\n=== List Access ===")

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index (0-4): "))
    print("Value:", numbers[index])

except ValueError:
    print("❌ Index must be a number.")

except IndexError:
    print("❌ Index out of range.")

finally:
    print("List operation completed.")
  
