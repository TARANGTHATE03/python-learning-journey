# File Handling in Python

This folder contains beginner-friendly examples of **File Handling and File Operations in Python**.

File handling allows us to create, read, write, update, and delete files using Python.

## Topics Covered

### 1. Creating a File
- Creating files using `open()`.
- Using write mode (`w`).

### 2. Reading a File
- Reading complete file content using `read()`.
- Reading one line using `readline()`.
- Reading all lines using `readlines()`.

### 3. Writing to a File
- Writing content using `write()`.
- Understanding how write mode overwrites existing content.

### 4. Appending to a File
- Adding new content using append mode (`a`).

### 5. File Modes
- `r` – Read mode.
- `w` – Write mode.
- `a` – Append mode.
- `x` – Create a new file; gives an error if it already exists.
- `r+` – Read and write mode.

### 6. With Statement
- Using `with open()` to work with files.
- Automatically closing files after operations.

### 7. File Properties
- Getting file name using `name`.
- Checking file mode using `mode`.
- Checking whether a file is closed using `closed`.

### 8. File Pointer Operations
- `tell()` – Returns the current file pointer position.
- `seek()` – Moves the file pointer to a specified position.

### 9. File Management
- Using the `os` module.
- Checking file existence using `os.path.exists()`.
- Renaming files using `os.rename()`.
- Deleting files using `os.remove()`.

### 10. Exception Handling
- Handling missing files using `FileNotFoundError`.

## File Structure

```text
09_filehandling/
│
├── fileoperations.py
└── README.md
```

## How to Run

Open the terminal in this folder and execute:

```bash
python fileoperations.py
```

## Learning Outcomes

After completing these examples, I learned:

- How to create and manage files using Python.
- How to read, write, and append file content.
- How to work with different file modes.
- How to use the `with` statement.
- How to manage file pointers.
- How to rename and delete files.
- How to handle file-related errors.

## Practice Questions

1. Write a program to create and read a text file.
2. Write a program to append text to an existing file.
3. Count the number of lines in a file.
4. Copy the contents of one file into another.
5. Rename and delete a file using the `os` module.

