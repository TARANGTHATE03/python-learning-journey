
# 1. Importing a Built-in Module
# A module is a Python file containing functions and variables.

import math

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Value of Pi:", math.pi)


# 2. Importing Specific Functions
# We can import only the functions we need from a module.

from math import factorial, ceil, floor

print("\nFactorial:", factorial(5))
print("Ceiling:", ceil(4.3))
print("Floor:", floor(4.8))


# 3. Importing a Module with an Alias
# The "as" keyword gives a module a shorter name.

import random as r

print("\nRandom Number:", r.randint(1, 100))
print("Random Choice:", r.choice(["Apple", "Banana", "Mango"]))


# 4. Using the datetime Module
# Used to work with dates and times.

import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().time()

print("\nCurrent Date:", current_date)
print("Current Time:", current_time)


# 5. Using the os Module
# Used for interacting with the operating system.

import os

print("\nCurrent Working Directory:", os.getcwd())
print("Operating System Name:", os.name)


# 6. Using the platform Module
# Provides information about the system and Python version.

import platform

print("\nSystem:", platform.system())
print("Processor:", platform.processor())
print("Python Version:", platform.python_version())


# 7. Using the statistics Module
# Provides mathematical statistical functions.

import statistics

numbers = [10, 20, 30, 40, 50]

print("\nMean:", statistics.mean(numbers))
print("Median:", statistics.median(numbers))
print("Standard Deviation:", statistics.stdev(numbers))


# 8. Creating and Using Your Own Module
# A user-defined module is a Python file created by the programmer.
# Create a separate file named mymodule.py in this same folder.

# Example code for mymodule.py:
#
# def greet(name):
#     return "Hello, " + name
#
# def add(a, b):
#     return a + b

# Uncomment these lines after creating mymodule.py:

# import mymodule
# print("\n", mymodule.greet("Tarang"))
# print("Addition:", mymodule.add(10, 20))


# 9. Using the dir() Function
# dir() displays the names available inside a module.

import math

print("\nSome Math Module Functions:")
print(dir(math)[:10])


# 10. The __name__ Variable
# When a Python file runs directly, its __name__ is "__main__".

if __name__ == "__main__":
    print("\nThis file is running directly.")

