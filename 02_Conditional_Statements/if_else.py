
# Python If-Else Statements
# Topic: Making decisions using conditions

# 1. Simple if Statement
# Executes the code only when the condition is True.

age = 21

if age >= 18:
    print("You are an adult.")

# 2. if-else Statement
# if runs when the condition is True.
# else runs when the condition is False.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 3. Checking Even or Odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 4. Checking Positive or Negative

number = int(input("Enter a number: "))

if number >= 0:
    print("The number is positive or zero.")
else:
    print("The number is negative.")

# 5. Checking Pass or Fail

marks = int(input("Enter your marks (0-100): "))

if 0 <= marks <= 100:
    if marks >= 40:
        print("Result: Pass")
    else:
        print("Result: Fail")
else:
    print("Invalid marks. Enter a value between 0 and 100.")

# 6. Checking the Greater of Two Numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("The first number is greater.")
else:
    print("The second number is greater or both numbers are equal.")

# 7. Using Logical Operators with if-else

user_age = int(input("Enter your age: "))

if user_age >= 18 and user_age <= 60:
    print("You are between 18 and 60.")
else:
    print("You are outside the age range.")

# 8. Short-Hand If-Else (Ternary Operator)

number = 10

result = "Even" if number % 2 == 0 else "Odd"

print("The number is:", result)

