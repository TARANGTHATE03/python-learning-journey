# Python Variables 📦

## 📌 Introduction

Variables are fundamental building blocks in Python programming. A variable is a name that refers to a value, allowing us to store, access, and reuse data throughout a program.

Python does not require explicit variable type declarations. The type is determined by the value assigned to the variable.

## 💻 Creating Variables

In Python, we create a variable using the assignment operator (`=`).

```python
name = "Tarang"
age = 21
height = 5.7
is_student = True
```

Here:
- `name` refers to a string value.
- `age` refers to an integer value.
- `height` refers to a floating-point value.
- `is_student` refers to a Boolean value.

## 🔍 Checking Variable Types

The built-in `type()` function tells us the type of a variable's current value.

```python
age = 21
print(type(age))
```

Output:

```text
<class 'int'>
```

## 🔄 Reassigning Variables

A variable can refer to a different value later in the program.

```python
course = "Python"
print(course)

course = "Data Analysis"
print(course)
```

Output:

```text
Python
Data Analysis
```

## 🔢 Multiple Assignment

Python allows us to assign values to multiple variables in one statement.

```python
x, y, z = 10, 20, 30
print(x, y, z)
```

Output:

```text
10 20 30
```

We can also assign the same value to multiple variables:

```python
a = b = c = 100
```

## 📝 Rules for Naming Variables

1. A variable name can contain letters, digits, and underscores.
2. A variable name cannot start with a digit.
3. Variable names are case-sensitive. For example, `age` and `Age` are different names.
4. Spaces are not allowed in variable names.
5. Python keywords, such as `if`, `for`, and `class`, cannot be used as variable names.
6. Descriptive names such as `student_name` are recommended for readability.

Examples:

```python
student_name = "Rahul"  # Valid
_marks = 85             # Valid
subject2 = "AIML"       # Valid

# 2subject = "Python"   # Invalid: starts with a digit
```

## ➕ Using Variables in Calculations

Variables can store the results of mathematical operations.

```python
num1 = 15
num2 = 5

print(num1 + num2)  # Addition: 20
print(num1 - num2)  # Subtraction: 10
print(num1 * num2)  # Multiplication: 75
print(num1 / num2)  # Division: 3.0
```

## 🧠 What I Learned

- What variables are and why they are used.
- How to create and reassign variables.
- How to inspect data types using `type()`.
- How to assign values to multiple variables.
- The rules for naming variables.
- How to perform calculations using variables.

## 🎯 Practice Tasks

- Create variables for your name, age, and favorite programming language.
- Create two numeric variables and calculate their sum.
- Swap the values of two variables.
- Experiment with assigning a new value to an existing variable.
- Create variables using valid names and identify invalid names.

## 📂 Next Topic

**Data Types in Python** — understanding integers, floats, strings, Booleans, collections, and other built-in types.



*Python Learning Journey | Learning step by step, one concept at a time.*