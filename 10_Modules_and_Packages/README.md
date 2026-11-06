# Modules and Packages in Python

This folder contains beginner-friendly examples of **Python Modules and Packages**.

Modules and packages help organize Python code into reusable files and folders.

## Topics Covered

### 1. Modules
- Understanding what a module is.
- Importing built-in Python modules using `import`.

### 2. Importing Specific Functions
- Importing selected functions using `from ... import`.
- Using functions without writing the module name every time.

### 3. Module Aliases
- Using the `as` keyword to give a module a shorter name.

### 4. Built-in Modules

Examples covered:

- `math` – Mathematical operations.
- `random` – Generating random numbers and selecting random items.
- `datetime` – Working with dates and times.
- `os` – Interacting with the operating system.
- `platform` – Getting system information.
- `statistics` – Performing statistical calculations.

### 5. User-Defined Modules
- Creating our own Python module.
- Importing functions from another Python file.
- Reusing code from different files.

### 6. dir() Function
- Displaying available functions and attributes inside a module.

### 7. __name__ Variable
- Understanding the special `__name__` variable.
- Using `if __name__ == "__main__":`.

### 8. Packages
- Understanding what a Python package is.
- Organizing multiple modules inside a folder.
- Using an `__init__.py` file to identify and initialize a package.

## Difference Between Modules and Packages

- **Module:** A single Python file containing functions, variables, and classes.
- **Package:** A folder used to organize related Python modules.

## Example Package Structure

```text
my_package/
│
├── __init__.py
├── module1.py
└── module2.py
```

## How to Run

Open the terminal in this folder and execute:

```bash
python modules.py
```

## Learning Outcomes

After completing these examples, I learned:

- How to import and use Python modules.
- How to work with built-in modules.
- How to import specific functions and use aliases.
- How to create and import user-defined modules.
- How to understand Python packages.
- How to use `dir()` and `__name__`.

## Practice Questions

1. Import the math module and calculate the square root of a number.
2. Generate a random number between 1 and 100.
3. Display the current date using the datetime module.
4. Create a user-defined module containing addition and subtraction functions.
5. Create a package containing two Python modules and import a function from one of them.
