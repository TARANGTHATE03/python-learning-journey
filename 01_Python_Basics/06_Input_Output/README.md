# Python Input and Output

## Introduction

Input and Output are important concepts in Python programming.

- **Input** allows a program to receive information from the user.
- **Output** allows a program to display information on the screen.

Python provides built-in functions such as `input()` and `print()` to perform these operations.

## 1. Output Using `print()`

The `print()` function displays text, variables, and results on the screen.

Example:

```python
print("Hello, World!")
print("Welcome to Python")
```

Output:

```text
Hello, World!
Welcome to Python
```

## 2. Input Using `input()`

The `input()` function allows users to enter information while a program is running.

Example:

```python
name = input("Enter your name: ")
print("Hello,", name)
```

Example output:

```text
Enter your name: Tarang
Hello, Tarang
```

Note: The `input()` function returns the entered value as a string.

## 3. Integer Input Using `int()`

Use `int()` to convert user input into an integer when you need to perform mathematical calculations.

Example:

```python
age = int(input("Enter your age: "))
print("Your age is:", age)
```

Example output:

```text
Enter your age: 21
Your age is: 21
```

## 4. Decimal Input Using `float()`

Use `float()` to convert user input into a decimal number.

Example:

```python
height = float(input("Enter your height: "))
print("Your height is:", height)
```

Example output:

```text
Enter your height: 1.75
Your height is: 1.75
```

## 5. Taking Multiple Inputs

We can take input multiple times and store each value in a separate variable.

Example:

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
```

Example output:

```text
Enter first number: 10
Enter second number: 20
Sum: 30
```

## 6. Using f-Strings

An f-string allows us to insert variables directly into a string using curly braces `{}`.

Example:

```python
name = "Tarang"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Tarang and I am 21 years old.
```

## 7. Using `sep` and `end`

The `sep` parameter specifies the separator between multiple values printed by `print()`.

Example:

```python
print("Python", "is", "easy", sep="-")
```

Output:

```text
Python-is-easy
```

The `end` parameter specifies what should be printed at the end. By default, `print()` ends with a newline.

Example:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

## What I Learned

- How to display information using `print()`.
- How to accept user input using `input()`.
- How to convert input into integers using `int()`.
- How to convert input into decimal numbers using `float()`.
- How to take multiple inputs and perform calculations.
- How to format output using f-strings.
- How to use the `sep` and `end` parameters.

## Practice Tasks

1. Ask the user for their name and print a welcome message.
2. Ask the user for their age and display it.
3. Take two numbers and display their sum, difference, product, and division.
4. Ask for the user's height using `float()`.
5. Ask for the user's name and city, then display both using an f-string.
6. Print three words separated by hyphens using `sep`.
7. Print two messages on the same line using `end`.

## Conclusion

Input and Output allow Python programs to interact with users. The `input()` function receives information, while `print()` displays information. Type conversion and f-strings make these operations more useful.

## Next Topic

**Conditional Statements in Python** — learning how to make decisions using `if`, `elif`, and `else`.