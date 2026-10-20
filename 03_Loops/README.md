# Loops in Python 🐍

## Introduction

Loops in Python are used to execute a block of code repeatedly. They help reduce code repetition and make programs more efficient.

Python provides `for` loops and `while` loops. It also provides loop control statements such as `break`, `continue`, and `pass` to control how loops behave.

This section documents my learning of loops through examples, practical programs, and coding exercises.

## Learning Objectives

- Understand the purpose of loops in Python.
- Use `for` loops to iterate over sequences.
- Use `while` loops to repeat code while a condition is true.
- Control loop execution using `break`, `continue`, and `pass`.
- Understand nested loops and loop counters.
- Solve basic programming problems using loops.

## Topics Covered

### 1. For Loop

A `for` loop is used to iterate over a sequence, such as a list, string, or range of numbers.

**Concepts covered:**
- Basic `for` loops
- The `range()` function
- Start, stop, and step values
- Iterating through strings and lists
- Nested `for` loops
- The `enumerate()` function
- The `else` block with a loop

**Example:**

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

[Explore For Loop](./for_loop.py)

### 2. While Loop

A `while` loop repeats a block of code as long as its condition remains true.

**Concepts covered:**
- Basic `while` loops
- Loop counters
- Incrementing and decrementing values
- Taking user input inside loops
- Using `break` and `continue`
- Avoiding infinite loops
- The `else` block with a loop

**Example:**

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

[Explore While Loop](./while_loop.py)

### 3. Break, Continue, and Pass

These statements change how code executes inside loops.

**`break`**

Terminates the loop immediately.

```python
for number in range(1, 6):
    if number == 3:
        break

    print(number)
```

Output:

```text
1
2
```

**`continue`**

Skips the current iteration and moves to the next one.

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

**`pass`**

Does nothing and acts as a placeholder when a statement is required syntactically.

```python
for number in range(1, 4):
    if number == 2:
        pass

    print(number)
```

Output:

```text
1
2
3
```

[Explore Break, Continue, and Pass](./break_continue_pass.py)

## Difference Between For and While Loops

A `for` loop is commonly used when iterating through a sequence or a known range of values.

A `while` loop is commonly used when repetition depends on a condition that may change during execution.

Both loops can be used to solve many of the same problems.

## Important Concepts

- **Iteration:** One execution of a loop.
- **`range()`:** Generates a sequence of numbers.
- **Loop counter:** A variable used to track progress through a loop.
- **Nested loop:** A loop placed inside another loop.
- **Infinite loop:** A loop that does not stop because its condition never becomes false.
- **Loop control statements:** `break`, `continue`, and `pass`.

## What I Learned

- How to repeat instructions using `for` and `while` loops.
- How to iterate through sequences and ranges.
- How to use counters and update variables.
- How to terminate or skip iterations.
- How to use `pass` as a placeholder.
- How to write nested loops and simple repetitive programs.
- How to avoid infinite loops by updating loop conditions correctly.

## Practice Tasks

1. Print numbers from 1 to 100 using a `for` loop.
2. Print all even numbers between 1 and 50.
3. Calculate the sum of numbers from 1 to 100.
4. Print the multiplication table of a user-entered number.
5. Calculate the factorial of a number using a loop.
6. Reverse a number using a `while` loop.
7. Count the vowels in a string.
8. Print numbers from 1 to 20, skipping multiples of 3 using `continue`.
9. Stop a loop when a particular number is found using `break`.
10. Create a simple number-guessing game using a `while` loop.

## Tools and Technologies

- **Programming Language:** Python
- **Code Editor:** Visual Studio Code
- **Version Control:** Git
- **Repository Hosting:** GitHub

## Conclusion

Loops are fundamental to Python programming. They allow repetitive tasks to be performed efficiently and form the foundation for working with collections, processing data, and solving more complex problems.

## Next Topic

**Functions in Python** — learning how to organize reusable blocks of code using functions, parameters, arguments, and return values.

---

*Part of my Python Learning Journey — learning, practicing, and building one concept at a time.* 🚀