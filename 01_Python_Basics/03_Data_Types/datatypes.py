
# ==========================================
# PYTHON DATA TYPES
# Author: Tarang
# Description: Understanding built-in data types
# ==========================================

# Data types define the kind of value a variable stores.
# Python determines the type automatically from the assigned value.


# 1. INTEGER (int)
# Stores whole numbers without decimal points.

age = 21
marks = 85

print("--- Integer (int) ---")
print("Age:", age)
print("Marks:", marks)
print("Data type:", type(age))


# 2. FLOAT (float)
# Stores numbers with decimal points.

height = 5.7
price = 99.99

print("\n--- Float (float) ---")
print("Height:", height)
print("Price:", price)
print("Data type:", type(height))


# 3. STRING (str)
# Stores text inside single, double, or triple quotes.

name = "Tarang"
language = 'Python'

print("\n--- String (str) ---")
print("Name:", name)
print("Language:", language)
print("Data type:", type(name))


# 4. BOOLEAN (bool)
# Stores either True or False.
# Boolean values must begin with capital letters.

is_student = True
has_experience = False

print("\n--- Boolean (bool) ---")
print("Is student:", is_student)
print("Has experience:", has_experience)
print("Data type:", type(is_student))


# 5. LIST (list)
# An ordered and mutable collection.
# Mutable means elements can be changed.
# Lists allow duplicate values and mixed data types.

subjects = ["Python", "AIML", "Python"]
mixed_list = ["Tarang", 21, True]

print("\n--- List (list) ---")
print("Subjects:", subjects)
print("Mixed list:", mixed_list)
subjects.append("Data Analysis")
print("Updated subjects:", subjects)
print("Data type:", type(subjects))


# 6. TUPLE (tuple)
# An ordered and immutable collection.
# Immutable means elements cannot be changed after creation.
# Tuples allow duplicate values.

coordinates = (10, 20, 10)

print("\n--- Tuple (tuple) ---")
print("Coordinates:", coordinates)
print("Data type:", type(coordinates))


# 7. SET (set)
# Stores unique elements and removes duplicates.
# Sets are unordered collections.
# Sets can be modified after creation.

numbers = {1, 2, 3, 3, 4}

print("\n--- Set (set) ---")
print("Numbers:", numbers)
print("Data type:", type(numbers))


# 8. DICTIONARY (dict)
# Stores information in key-value pairs.
# Values are accessed using their keys.

student = {
    "name": "Tarang",
    "age": 21,
    "course": "B.E. IT"
}

print("\n--- Dictionary (dict) ---")
print("Student details:", student)
print("Student name:", student["name"])
print("Data type:", type(student))


# 9. RANGE (range)
# Represents a sequence of integers.
# Commonly used in loops.

sequence = range(1, 6)

print("\n--- Range (range) ---")
print("Sequence:", list(sequence))
print("Data type:", type(sequence))


# 10. NONE TYPE (NoneType)
# None represents the absence of a value.
# It is different from 0, False, or an empty string.

result = None

print("\n--- NoneType ---")
print("Result:", result)
print("Data type:", type(result))


# ==========================================
# TYPE CONVERSION
# Type conversion changes a value from one type to another.
# ==========================================

number = "100"       # A string containing digits
converted_number = int(number)

decimal_number = float(converted_number)

print("\n--- Type Conversion ---")
print("Original value:", number)
print("Original type:", type(number))
print("Converted integer:", converted_number)
print("Converted type:", type(converted_number))
print("Converted float:", decimal_number)


# ==========================================
# END OF PYTHON DATA TYPES LESSON
# ==========================================
