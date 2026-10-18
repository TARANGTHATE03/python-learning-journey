
# Python Nested If Statements
# Topic: Using an if statement inside another if statement

# 1. Basic Nested If
# The inner if runs only when the outer if condition is True.

age = 20

if age >= 18:
    print("You are an adult.")

    if age >= 21:
        print("You are 21 or older.")
    else:
        print("You are younger than 21.")
else:
    print("You are not an adult.")

# 2. Nested If with User Input
# Check eligibility based on age and a valid ID.

age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("You are eligible to enter.")
    else:
        print("You need a valid ID to enter.")
else:
    print("You must be at least 18 years old.")

# 3. Nested If for Positive, Negative, or Zero

number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

# 4. Nested If for Student Results
# First validate the marks, then check pass/fail and distinction.

marks = int(input("Enter your marks (0-100): "))

if 0 <= marks <= 100:
    if marks >= 40:
        print("Result: Pass")

        if marks >= 75:
            print("You have achieved distinction.")
        else:
            print("Keep working hard to achieve distinction.")
    else:
        print("Result: Fail")
else:
    print("Invalid marks. Enter a value between 0 and 100.")

# 5. Nested If for Login Simulation
# This is only a basic practice example, not secure authentication.

correct_username = "student"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username:
    if password == correct_password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# 6. Nested If with Even and Positive Checks

number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is zero or negative.")

