
# ==========================================
# Python Learning Journey
# Topic: Basic Functions
# File: basicfunctions.py
# ==========================================


# 1. Creating a Simple Function
print("1. Simple Function")

def greet():
    print("Hello, Welcome to Python!")

# Calling the function
greet()


# 2. Function with Parameters
print("\n2. Function with Parameters")

def greet_user(name):
    print("Hello,", name)

greet_user("Tarang")
greet_user("Rahul")


# 3. Function with Multiple Parameters
print("\n3. Multiple Parameters")

def add(a, b):
    print("Sum:", a + b)

add(10, 20)


# 4. Function with Return Statement
print("\n4. Return Statement")

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication:", result)


# 5. Function with Default Parameters
print("\n5. Default Parameters")

def welcome(name="Student"):
    print("Welcome,", name)

welcome("Tarang")
welcome()


# 6. Function Returning Multiple Values
print("\n6. Returning Multiple Values")

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

sum_result, difference = calculate(20, 10)

print("Addition:", sum_result)
print("Subtraction:", difference)


# 7. Function to Find Square
print("\n7. Square of a Number")

def square(number):
    return number ** 2

print("Square:", square(5))


# 8. Function to Check Even or Odd
print("\n8. Even or Odd")

def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Number 10 is:", check_number(10))
print("Number 7 is:", check_number(7))


# 9. Function to Find Factorial
print("\n9. Factorial")

def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result

print("Factorial of 5:", factorial(5))


# 10. Function to Find Maximum of Two Numbers
print("\n10. Maximum of Two Numbers")

def find_max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", find_max(25, 40))


# 11. Function with No Return Statement
print("\n11. Function Without Return")

def display_message():
    print("Learning Python Functions!")

result = display_message()
print("Returned Value:", result)  # None


# 12. Main Function
print("\n12. Main Function")

def main():
    print("Python Learning Journey")
    print("Practicing Basic Functions")

if __name__ == "__main__":
    main()


print("\nBasic functions examples completed!")

