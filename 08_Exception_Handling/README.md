# Exception Handling in Python

This folder contains beginner-friendly examples of **Exception Handling in Python**.

Exception handling helps us manage runtime errors and prevents a program from terminating unexpectedly.

## Topics Covered

### 1. Basic Try-Except
- Using `try` and `except` blocks.
- Handling errors without stopping the program.

### 2. Common Exceptions
- `ValueError` – Invalid value or input.
- `ZeroDivisionError` – Division by zero.
- `IndexError` – Accessing an invalid list index.
- `KeyError` – Accessing a missing dictionary key.
- `TypeError` – Performing an operation on an incompatible data type.

### 3. Multiple Except Blocks
- Handling different exceptions separately.

### 4. Else Block
- Executes when no exception occurs in the `try` block.

### 5. Finally Block
- Always executes, whether an exception occurs or not.

### 6. Exception Class
- Using `Exception` to handle different types of errors.
- Accessing error details using `as`.

### 7. Raise Keyword
- Manually generating an exception using `raise`.

### 8. Custom Exceptions
- Creating user-defined exceptions using a class.

## File Structure

```text
08_exceptionhandling/
│
├── exceptionhandling.py
└── README.md
```

## How to Run

Open the terminal in this folder and execute:

```bash
python exceptionhandling.py
```

## Learning Outcomes

After completing these examples, I learned:

- How to identify and handle runtime errors.
- How to use `try`, `except`, `else`, and `finally`.
- How to handle multiple exceptions.
- How to raise exceptions manually.
- How to create custom exception classes.

## Practice Questions

1. Write a program to handle division by zero.
2. Handle invalid user input using `ValueError`.
3. Demonstrate the use of `else` and `finally`.
4. Write a program using multiple `except` blocks.
5. Create a custom exception for invalid age.
