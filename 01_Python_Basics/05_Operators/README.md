# Python Operators

## Introduction

Operators in Python are special symbols or keywords used to perform operations on variables and values.

For example, operators can be used to perform mathematical calculations, compare values, assign values, and check logical conditions.

## Types of Operators in Python

### 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `//` Floor Division
- `%` Modulus (remainder)
- `**` Exponentiation (power)

Example:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### 2. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

Example:

```python
a = 10
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
```

### 3. Assignment Operators

Assignment operators are used to assign or update values in variables.

- `=` Assign a value
- `+=` Add and assign
- `-=` Subtract and assign
- `*=` Multiply and assign
- `/=` Divide and assign

Example:

```python
x = 10

x += 5
print(x)  # 15

x -= 3
print(x)  # 12

x *= 2
print(x)  # 24
```

### 4. Logical Operators

Logical operators combine or reverse conditions.

- `and` Returns `True` if both conditions are true.
- `or` Returns `True` if at least one condition is true.
- `not` Reverses the result.

Example:

```python
a = 10
b = 5

print(a > 5 and b < 10)  # True
print(a > 15 or b < 10)  # True
print(not(a > 5))        # False
```

### 5. Membership Operators

Membership operators check whether a value exists in a sequence, such as a string, list, or tuple.

- `in` Checks whether a value exists.
- `not in` Checks whether a value does not exist.

Example:

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("orange" not in fruits)  # True
```

### 6. Identity Operators

Identity operators check whether two variables refer to the same object in memory.

- `is` Returns `True` if both refer to the same object.
- `is not` Returns `True` if they refer to different objects.

Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False
```

Note: `==` compares values, whereas `is` checks object identity.

## Expected Output

When you run the examples, Python displays the results of each operation, such as arithmetic calculations, comparison results (`True` or `False`), and membership or identity checks.

## What I Learned

- What operators are and why they are used in Python.
- How to perform mathematical calculations using arithmetic operators.
- How to compare values using comparison operators.
- How to update variable values using assignment operators.
- How to combine conditions using logical operators.
- How to check membership and object identity.

## Practice Tasks

1. Create two variables and perform all arithmetic operations on them.
2. Compare two numbers using all comparison operators.
3. Create a variable and update it using `+=`, `-=`, and `*=`.
4. Use logical operators to check whether a number is between 10 and 50.
5. Check whether a fruit exists in a list using membership operators.
6. Experiment with `==` and `is` to understand the difference.

## Conclusion

Operators are an essential part of Python programming. They help us perform calculations, compare values, manage variables, and build logical conditions.

## Next Topic

**Input and Output in Python** — learning how to take input from users using `input()` and display results using `print()`.