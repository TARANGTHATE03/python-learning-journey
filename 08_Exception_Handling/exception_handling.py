
# 1. Basic try-except
# Handles an error without stopping the program.

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Error: Please enter a valid integer.")


# 2. Handling ZeroDivisionError
# Occurs when a number is divided by zero.

try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


# 3. Using multiple except blocks
# Different errors can be handled separately.

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("Error: Enter numbers only.")

except ZeroDivisionError:
    print("Error: Number cannot be zero.")


# 4. Using else
# The else block runs only when no exception occurs.

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input.")

else:
    print("No error occurred.")


# 5. Using finally
# The finally block always executes.

try:
    num = int(input("Enter a number: "))
    print("Number:", num)

except ValueError:
    print("Invalid input.")

finally:
    print("This block always executes.")


# 6. Using Exception
# Exception can handle different types of errors.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Division:", a / b)

except Exception as error:
    print("An error occurred:", error)


# 7. IndexError
# Occurs when accessing an invalid list index.

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Error: List index does not exist.")


# 8. KeyError
# Occurs when accessing a dictionary key that does not exist.

try:
    student = {"name": "Tarang", "age": 21}
    print(student["marks"])

except KeyError:
    print("Error: Dictionary key not found.")


# 9. Raising an exception
# The raise keyword is used to generate an exception manually.

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible.")

except ValueError as error:
    print("Error:", error)


# 10. Custom Exception
# We can create our own exception class.

class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")

    print("Marks:", marks)

except InvalidMarksError as error:
    print("Custom Error:", error)

except ValueError:
    print("Please enter valid numeric marks.")

