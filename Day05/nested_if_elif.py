# Day 05 - Nested If and Elif

marks = int(input("Enter your marks (0-100): "))

if marks >= 0 and marks <= 100:

    if marks >= 90:
        grade = "A+"

    elif marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    elif marks >= 50:
        grade = "D"

    else:
        grade = "Fail"

    print("\nYour Grade is:", grade)

    # Check Pass or Fail
    if marks >= 50:
        print("🎉 Congratulations! You Passed.")
    else:
        print("❌ Better Luck Next Time.")

else:
    print("Invalid Marks! Please enter marks between 0 and 100.")
