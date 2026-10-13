
# ==========================================
# PYTHON TYPE CONVERSION
# Author: Tarang
# Description: Understanding type conversion in Python
# ==========================================

# Type conversion means changing a value from one data type
# to another data type.


# 1. IMPLICIT TYPE CONVERSION
# Python automatically converts one compatible type into another.
# Here, an integer is converted into a float during addition.

num1 = 10       # int
num2 = 5.5      # float

result = num1 + num2

print("--- Implicit Type Conversion ---")
print("Integer:", num1)
print("Float:", num2)
print("Result:", result)
print("Result type:", type(result))


# 2. EXPLICIT TYPE CONVERSION
# We manually convert a value using functions such as int(),
# float(), str(), and bool().


# 2.1 Integer Conversion (int)
# Converts compatible values into integers.
# Converting a float to int removes the fractional part;
# it does not round the number.

decimal_number = 12.8
converted_integer = int(decimal_number)

print("\n--- Integer Conversion ---")
print("Original value:", decimal_number)
print("Converted value:", converted_integer)
print("Data type:", type(converted_integer))


# 2.2 Float Conversion (float)
# Converts compatible numbers or numeric strings into floats.

number = 25
converted_float = float(number)

print("\n--- Float Conversion ---")
print("Original value:", number)
print("Converted value:", converted_float)
print("Data type:", type(converted_float))


# 2.3 String Conversion (str)
# Converts many types of values into their string representation.

age = 21
converted_string = str(age)

print("\n--- String Conversion ---")
print("Original value:", age)
print("Converted value:", converted_string)
print("Data type:", type(converted_string))


# 2.4 Boolean Conversion (bool)
# bool() returns False for values such as 0, 0.0, "",
# None, and empty collections.
# Most other values return True.

print("\n--- Boolean Conversion ---")
print("bool(1):", bool(1))
print("bool(0):", bool(0))
print("bool('Python'):", bool("Python"))
print("bool(''):", bool(""))
print("bool([]):", bool([]))


# 2.5 List Conversion (list)
# Converts an iterable, such as a tuple or string, into a list.

my_tuple = (10, 20, 30)
converted_list = list(my_tuple)

print("\n--- List Conversion ---")
print("Original tuple:", my_tuple)
print("Converted list:", converted_list)
print("Data type:", type(converted_list))


# 2.6 Tuple Conversion (tuple)
# Converts an iterable into a tuple.

my_list = [1, 2, 3]
converted_tuple = tuple(my_list)

print("\n--- Tuple Conversion ---")
print("Original list:", my_list)
print("Converted tuple:", converted_tuple)
print("Data type:", type(converted_tuple))


# 2.7 Set Conversion (set)
# Converts an iterable into a set.
# Duplicate elements are removed.

numbers = [1, 2, 2, 3, 3, 4]
converted_set = set(numbers)

print("\n--- Set Conversion ---")
print("Original list:", numbers)
print("Converted set:", converted_set)


# 2.8 Dictionary Conversion (dict)
# dict() can convert an iterable of key-value pairs
# into a dictionary.

pairs = [("name", "Tarang"), ("age", 21)]
student = dict(pairs)

print("\n--- Dictionary Conversion ---")
print("Dictionary:", student)
print("Student name:", student["name"])


# 3. CONVERTING USER INPUT
# The input() function always returns a string.
# Convert the input if you need to perform numeric calculations.

# Uncomment these lines to try user input:
# user_age = int(input("Enter your age: "))
# print("Next year, your age will be:", user_age + 1)


# 4. TYPE CONVERSION ERRORS
# Conversion fails when a value is not compatible with the target type.
# For example, int("hello") raises a ValueError.
# Use try-except to handle such errors safely.

text_number = "hello"

print("\n--- Handling Conversion Errors ---")

try:
    converted_number = int(text_number)
    print("Converted number:", converted_number)
except ValueError:
    print("Error: This string cannot be converted to an integer.")


# 5. PRACTICAL EXAMPLE
# Convert strings containing numbers into integers
# before adding them.

first_number = "100"
second_number = "200"

total = int(first_number) + int(second_number)

print("\n--- Practical Example ---")
print("First number:", first_number)
print("Second number:", second_number)
print("Total:", total)


# ==========================================
# END OF PYTHON TYPE CONVERSION LESSON
# ==========================================

