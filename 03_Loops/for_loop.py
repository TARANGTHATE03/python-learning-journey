
# Python For Loops
# Topic: Repeating statements using a for loop


# 1. Basic For Loop
# Print numbers from 1 to 5.

print("Example 1: Basic For Loop")

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# 2. Using range()
# range(5) generates numbers from 0 to 4.

print("\nExample 2: Using range()")

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# 3. Using a Step Value
# range(start, stop, step)

print("\nExample 3: Using Step Value")

for i in range(2, 11, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10


# 4. Counting Backwards
# A negative step decreases the value.

print("\nExample 4: Counting Backwards")

for i in range(5, 0, -1):
    print(i)

# Output:
# 5
# 4
# 3
# 2
# 1


# 5. Looping Through a String
# A string is a sequence of characters.

print("\nExample 5: Looping Through a String")

name = "Python"

for character in name:
    print(character)

# Output:
# P
# y
# t
# h
# o
# n


# 6. Looping Through a List
# A for loop can access each item in a list.

print("\nExample 6: Looping Through a List")

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango


# 7. Calculating the Sum of Numbers
# Add numbers from 1 to 5.

print("\nExample 7: Sum of Numbers")

total = 0

for i in range(1, 6):
    total += i

print("Total:", total)

# Output:
# Total: 15


# 8. Multiplication Table
# Print the multiplication table of a number.

print("\nExample 8: Multiplication Table")

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# 9. Using if Inside a For Loop
# Print only even numbers from 1 to 10.

print("\nExample 9: Even Numbers")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Output:
# 2
# 4
# 6
# 8
# 10


# 10. Nested For Loops
# A loop inside another loop.

print("\nExample 10: Nested For Loop")

for i in range(1, 4):
    for j in range(1, 4):
        print(j, end=" ")
    print()

# Output:
# 1 2 3
# 1 2 3
# 1 2 3


# 11. Using enumerate()
# enumerate() gives both the index and the item.

print("\nExample 11: Using enumerate()")

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)

# Output:
# 0 Python
# 1 Java
# 2 C++


# 12. Using else with a For Loop
# The else block runs when the loop finishes normally.

print("\nExample 12: For Loop with else")

for i in range(1, 4):
    print(i)
else:
    print("Loop completed.")

# Output:
# 1
# 2
# 3
# Loop completed.

