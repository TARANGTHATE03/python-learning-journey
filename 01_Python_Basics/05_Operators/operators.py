
# ==========================================
# PYTHON OPERATORS
# Author: Tarang
# Description: Understanding operators in Python
# ==========================================

# Operators are symbols or keywords used to perform
# operations on values and variables.


# 1. ARITHMETIC OPERATORS
# Used to perform mathematical calculations.

a = 10
b = 3

print("--- Arithmetic Operators ---")
print("Addition:", a + b)             # 13
print("Subtraction:", a - b)          # 7
print("Multiplication:", a * b)       # 30
print("Division:", a / b)             # 3.333...
print("Floor Division:", a // b)      # 3
print("Modulus:", a % b)              # 1
print("Exponentiation:", a ** b)      # 1000


# 2. COMPARISON OPERATORS
# Compare two values and return True or False.

print("\n--- Comparison Operators ---")
print("Equal:", a == b)               # False
print("Not Equal:", a != b)           # True
print("Greater Than:", a > b)         # True
print("Less Than:", a < b)            # False
print("Greater or Equal:", a >= b)    # True
print("Less or Equal:", a <= b)       # False


# 3. ASSIGNMENT OPERATORS
# Assign values to variables or update their values.

print("\n--- Assignment Operators ---")

x = 10
print("Initial x:", x)

x += 5       # Same as x = x + 5
print("After += 5:", x)

x -= 3       # Same as x = x - 3
print("After -= 3:", x)

x *= 2       # Same as x = x * 2
print("After *= 2:", x)

x /= 4       # Same as x = x / 4
print("After /= 4:", x)

x = 10
x //= 3      # Same as x = x // 3
print("After //= 3:", x)

x = 10
x %= 3       # Same as x = x % 3
print("After %= 3:", x)

x = 2
x **= 3      # Same as x = x ** 3
print("After **= 3:", x)


# 4. LOGICAL OPERATORS
# Combine or reverse Boolean conditions.
# and: True when both conditions are True.
# or: True when at least one condition is True.
# not: Reverses the truth value.

age = 21
has_id = True

print("\n--- Logical Operators ---")
print("Eligible by age and ID:", age >= 18 and has_id)
print("Eligible by age or ID:", age >= 18 or has_id)
print("Not has_id:", not has_id)


# 5. MEMBERSHIP OPERATORS
# Check whether a value exists in a collection.
# in: Returns True if the value is present.
# not in: Returns True if the value is absent.

languages = ["Python", "Java", "C++"]

print("\n--- Membership Operators ---")
print("'Python' in languages:", "Python" in languages)
print("'JavaScript' in languages:", "JavaScript" in languages)
print("'JavaScript' not in languages:",
      "JavaScript" not in languages)


# 6. IDENTITY OPERATORS
# Check whether two references point to the same object.
# is: True if both refer to the same object.
# is not: True if they refer to different objects.

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("\n--- Identity Operators ---")
print("list1 is list2:", list1 is list2)       # True
print("list1 is list3:", list1 is list3)       # False
print("list1 is not list3:", list1 is not list3)  # True

# Note:
# list1 == list3 is True because their contents are equal.
# list1 is list3 is False because they are separate objects.


# 7. BITWISE OPERATORS
# Operate on the binary representation of integers.

p = 5       # Binary: 0101
q = 3       # Binary: 0011

print("\n--- Bitwise Operators ---")
print("AND (&):", p & q)           # 1
print("OR (|):", p | q)            # 7
print("XOR (^):", p ^ q)           # 6
print("NOT (~):", ~p)              # -6
print("Left Shift (<<):", p << 1)  # 10
print("Right Shift (>>):", p >> 1) # 2


# 8. OPERATOR PRECEDENCE
# Precedence determines which operations are evaluated first.
# Parentheses can make the intended order explicit.

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4

print("\n--- Operator Precedence ---")
print("2 + 3 * 4 =", result1)       # 14
print("(2 + 3) * 4 =", result2)     # 20


# ==========================================
# END OF PYTHON OPERATORS LESSON
# ==========================================

