
# 1. Creating a file
# The "w" mode creates a new file or overwrites an existing file.

file = open("sample.txt", "w")
file.write("Hello, Python!\n")
file.write("Learning File Handling.")
file.close()

print("File created successfully.")


# 2. Reading a file
# The "r" mode is used to read an existing file.

file = open("sample.txt", "r")
content = file.read()
print("\nFile Content:")
print(content)
file.close()


# 3. Writing to a file
# The "w" mode overwrites the existing content.

file = open("sample.txt", "w")
file.write("This is new content.\n")
file.write("Old content has been replaced.")
file.close()

print("\nContent written successfully.")


# 4. Appending to a file
# The "a" mode adds content at the end of the file.

file = open("sample.txt", "a")
file.write("\nThis line is appended.")
file.close()

print("\nContent appended successfully.")


# 5. Reading line by line
# readline() reads one line at a time.

file = open("sample.txt", "r")
print("\nReading line by line:")

print(file.readline(), end="")
print(file.readline(), end="")

file.close()


# 6. Reading all lines
# readlines() returns all lines as a list.

file = open("sample.txt", "r")
lines = file.readlines()

print("\nAll Lines:")
print(lines)

file.close()


# 7. Using with statement
# The with statement automatically closes the file.

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nUsing with statement:")
    print(content)


# 8. Checking file properties
# name, mode and closed provide file information.

file = open("sample.txt", "r")

print("\nFile Name:", file.name)
print("File Mode:", file.mode)
print("Is File Closed?", file.closed)

file.close()

print("Is File Closed After Closing?", file.closed)


# 9. File pointer using seek() and tell()
# tell() returns the current position of the file pointer.
# seek() moves the file pointer to a specified position.

file = open("sample.txt", "r")

print("\nFile Pointer Position:", file.tell())

print("First 5 Characters:", file.read(5))

print("Current Position:", file.tell())

file.seek(0)
print("After seek(0):", file.read(5))

file.close()


# 10. Renaming and deleting a file
# The os module provides file management operations.

import os

with open("oldfile.txt", "w") as file:
    file.write("This file will be renamed.")

if os.path.exists("oldfile.txt"):
    os.rename("oldfile.txt", "newfile.txt")
    print("\nFile renamed successfully.")

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File deleted successfully.")


# 11. Handling file errors
# FileNotFoundError occurs when the file does not exist.

try:
    file = open("missing.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("\nError: File not found.")

