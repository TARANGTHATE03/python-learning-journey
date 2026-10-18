# Conditional Statements in Python 🐍

## Introduction

Conditional statements allow a Python program to make decisions based on specific conditions.

They help a program execute different blocks of code depending on whether a condition is `True` or `False`.

In this section of my Python Learning Journey, I explore conditional statements through practical examples and coding exercises.

## Learning Objectives

- Understand how conditions work in Python.
- Use `if`, `elif`, and `else` to control program execution.
- Implement nested `if` statements.
- Combine conditions using logical operators.
- Apply conditional statements to real-world problems.
- Improve problem-solving skills through coding practice.

## Topics Covered

### 1. Conditional Statements — `if`, `elif`, and `else`

Learn how to execute different blocks of code based on conditions.

**Concepts covered:**
- The `if` statement
- The `elif` statement
- The `else` statement
- Comparison operators
- Logical operators in conditions

**Example:**

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

Output:

```text
Grade B
```

[Explore Conditional Statements](./07_Conditional_Statements/)

### 2. If-Else Statements

Learn how to choose between two possible outcomes.

**Concepts covered:**
- `if` and `else`
- Checking even and odd numbers
- Checking positive and negative numbers
- Comparing two values
- Conditional expressions

**Example:**

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

Output:

```text
Odd
```

[Explore If-Else](./08_If_Else/)

### 3. Nested If Statements

Learn how to place one `if` statement inside another to check multiple levels of conditions.

**Concepts covered:**
- Nested `if`
- Nested `if-else`
- Multiple condition checks
- Indentation in nested blocks

**Example:**

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Age requirement not met")
```

Output:

```text
Entry allowed
```

[Explore Nested If](./09_Nested_If/)

## Important Concepts

- **Condition:** An expression that evaluates to `True` or `False`.
- **`if`:** Executes code when a condition is true.
- **`elif`:** Checks another condition if previous conditions were false.
- **`else`:** Executes when none of the preceding conditions is true.
- **Nested `if`:** An `if` statement placed inside another conditional block.
- **Indentation:** Defines which statements belong to each block.

## What I Learned

- How to control program execution using conditions.
- How to choose between different outcomes.
- How to validate user input.
- How to combine conditions using `and`, `or`, and `not`.
- How to write nested conditions.
- How to apply decision-making logic to practical problems.

## Practice Tasks

1. Check whether a number is positive, negative, or zero.
2. Check whether a number is even or odd.
3. Determine whether a student has passed or failed.
4. Assign grades based on marks.
5. Find the greatest of three numbers.
6. Check whether a person meets an age requirement and has valid identification.
7. Create a simple login simulation using nested `if` statements.
8. Build a calculator that performs an operation based on the user's choice.

## Conclusion

Conditional statements are fundamental to programming because they allow applications to make decisions and respond differently to different situations.

Understanding `if`, `elif`, `else`, and nested conditions provides a strong foundation for more advanced Python concepts.

## Next Topic

**Loops in Python** — learning how to repeat instructions using `for` and `while` loops.

---

*Part of my Python Learning Journey — learning, practicing, and building one concept at a time.* 🚀