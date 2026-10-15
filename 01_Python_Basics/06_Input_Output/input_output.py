
# Python Input and Output
# Topic: Taking input from the user and displaying output

# 1. Basic Output using print()
print("Welcome to Python Learning Journey!")

# 2. Printing Variables
name = "Tarang"
age = 21

print("Name:", name)
print("Age:", age)

# 3. Taking Input from the User
user_name = input("Enter your name: ")
print("Hello,", user_name)

# 4. Taking Integer Input
# input() returns a string, so we use int() to convert it.
user_age = int(input("Enter your age: "))
print("Your age is:", user_age)

# 5. Taking Float Input
height = float(input("Enter your height in meters: "))
print("Your height is:", height)

# 6. Taking Multiple Inputs
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("First number:", a)
print("Second number:", b)

# 7. Performing Calculations with User Input
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# 8. Using f-strings for Output
print(f"Hello {user_name}, you are {user_age} years old.")

# 9. Using sep and end in print()
print("Python", "is", "easy", sep="-")
print("Keep learning!", end=" ")
print("Keep practicing!")

