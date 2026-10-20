
# Python While Loops
# Topic: Repeating statements while a condition is True


# 1. Basic While Loop
# The loop runs as long as the condition is True.

print("Example 1: Basic While Loop")

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# 2. Counting Backwards

print("\nExample 2: Counting Backwards")

count = 5

while count >= 1:
    print(count)
    count -= 1

# Output:
# 5
# 4
# 3
# 2
# 1


# 3. Sum of Numbers
# Calculate the sum of numbers from 1 to 10.

print("\nExample 3: Sum of Numbers")

number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Total:", total)

# Output:
# Total: 55


# 4. While Loop with User Input
# Repeat until the user enters 0.

print("\nExample 4: User Input")

number = int(input("Enter a number (0 to stop): "))

while number != 0:
    print("You entered:", number)
    number = int(input("Enter another number (0 to stop): "))

print("Loop stopped.")

# Example: Entering 5, then 3, then 0
# You entered: 5
# You entered: 3
# Loop stopped.


# 5. Using break
# break immediately terminates the loop.

print("\nExample 5: Using break")

count = 1

while count <= 10:
    if count == 6:
        break

    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# 6. Using continue
# continue skips the rest of the current iteration.

print("\nExample 6: Using continue")

count = 0

while count < 10:
    count += 1

    if count % 2 == 0:
        continue

    print(count, end=" ")

print()

# Output:
# 1 3 5 7 9


# 7. Multiplication Table

print("\nExample 7: Multiplication Table")

number = 5
count = 1

while count <= 10:
    print(f"{number} x {count} = {number * count}")
    count += 1

# Output starts with:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# 8. Using else with a While Loop
# The else block runs if the loop finishes normally.

print("\nExample 8: While Loop with else")

count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed.")

# Output:
# 1
# 2
# 3
# Loop completed.


# 9. Using pass
# pass does nothing and acts as a placeholder.

print("\nExample 9: Using pass")

count = 1

while count <= 3:
    if count == 2:
        pass  # Placeholder for future code.

    print(count)
    count += 1

# Output:
# 1
# 2
# 3


# 10. Avoiding an Infinite Loop
# Update the loop variable so the condition eventually becomes False.

print("\nExample 10: Updating the Counter")

count = 1

while count <= 3:
    print("Learning Python")
    count += 1

# Output:
# Learning Python
# Learning Python
# Learning Python

