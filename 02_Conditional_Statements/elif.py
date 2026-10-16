
# Python Conditional Statements
# Topic: if, elif, and else

# 1. Simple if Statement
# The code runs only when the condition is True.

age = 21

if age >= 18:
    print("You are eligible to vote.")

# 2. if-else Statement
# if runs when the condition is True.
# else runs when the condition is False.

number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 3. if-elif-else Statement
# elif checks another condition if the previous one is False.

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

# 4. Checking Positive, Negative, or Zero

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 5. Multiple Conditions using Logical Operators

user_age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()

if user_age >= 18 and has_id == "yes":
    print("You can enter.")
else:
    print("You cannot enter.")

# 6. Nested if Statement
# An if statement can be placed inside another if statement.

temperature = int(input("Enter the temperature in Celsius: "))

if temperature >= 0:
    if temperature > 30:
        print("It is hot outside.")
    else:
        print("The temperature is moderate.")
else:
    print("It is freezing outside.")

# 7. Short-hand Conditional Expression (Ternary Operator)

num = 10

result = "Even" if num % 2 == 0 else "Odd"

print("The number is:", result)

