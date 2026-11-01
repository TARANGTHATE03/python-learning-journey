
# ==========================================
# Python Learning Journey
# Topic: Function Arguments
# File: arguments.py
# ==========================================


# 1. Positional Arguments
print("1. Positional Arguments")

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Tarang", 21)


# 2. Keyword Arguments
print("\n2. Keyword Arguments")

def display(name, course):
    print("Name:", name)
    print("Course:", course)

display(course="B.E. IT", name="Tarang")


# 3. Default Arguments
print("\n3. Default Arguments")

def greet(name="Student"):
    print("Hello,", name)

greet("Tarang")
greet()


# 4. Variable-Length Arguments (*args)
print("\n4. Variable-Length Arguments (*args)")

def add_numbers(*args):
    print("Arguments:", args)
    print("Sum:", sum(args))

add_numbers(10, 20)
add_numbers(10, 20, 30, 40)


# 5. Keyword Variable-Length Arguments (**kwargs)
print("\n5. Keyword Variable-Length Arguments (**kwargs)")

def display_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_details(name="Tarang", age=21, course="B.E. IT")


# 6. Combining Different Arguments
print("\n6. Combining Different Arguments")

def calculate(a, b=10):
    print("First Number:", a)
    print("Second Number:", b)
    print("Sum:", a + b)

calculate(20)
calculate(20, 30)


# 7. Returning Values from a Function
print("\n7. Returning Values")

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)


# 8. Passing a List as an Argument
print("\n8. Passing a List as an Argument")

def display_fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["Apple", "Banana", "Mango"]
display_fruits(my_fruits)


# 9. Passing Multiple Values Using *args
print("\n9. Finding Maximum Using *args")

def find_max(*numbers):
    return max(numbers)

print("Maximum:", find_max(10, 50, 30, 80, 20))


# 10. Keyword Arguments with Default Values
print("\n10. Keyword Arguments with Default Values")

def employee(name, department="IT"):
    print("Employee:", name)
    print("Department:", department)

employee("Tarang")
employee("Rahul", department="HR")


print("\nFunction arguments examples completed!")

