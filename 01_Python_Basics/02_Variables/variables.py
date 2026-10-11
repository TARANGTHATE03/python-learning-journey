
# ==========================================
# PYTHON VARIABLES
# Author: Tarang
# Description: Understanding variables in Python
# ==========================================

# A variable is a name used to store or reference a value.
# Python creates a variable when you assign a value to it.

# 1. Creating variables
name = "Tarang"
age = 21
height = 5.7
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# 2. Checking the data type of a variable
# The type() function returns the type of a value.

print("\n--- Variable Data Types ---")
print(type(name))        # str
print(type(age))         # int
print(type(height))      # float
print(type(is_student))  # bool


# 3. Assigning new values
# Variables can be reassigned after their creation.

course = "Python"
print("\nOriginal course:", course)

course = "Data Analysis"
print("Updated course:", course)


# 4. Assigning multiple variables
# Different variables can be assigned in one statement.

x, y, z = 10, 20, 30

print("\n--- Multiple Assignment ---")
print("x =", x)
print("y =", y)
print("z =", z)


# 5. Assigning the same value to multiple variables

a = b = c = 100

print("\n--- Same Value Assignment ---")
print("a =", a)
print("b =", b)
print("c =", c)


# 6. Rules for naming variables
# Valid names can contain letters, digits, and underscores.
# A variable name cannot begin with a digit.
# Python variable names are case-sensitive.
# Reserved Python keywords cannot be used as variable names.

student_name = "Rahul"  # Valid
_marks = 85             # Valid
subject2 = "AIML"       # Valid

print("\n--- Valid Variable Names ---")
print(student_name)
print(_marks)
print(subject2)


# 7. Updating a variable's value

score = 50
print("\nOriginal score:", score)

score = score + 10
print("Updated score:", score)


# 8. Using variables in calculations

num1 = 15
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("\n--- Calculations Using Variables ---")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


# End of Python Variables lesson

