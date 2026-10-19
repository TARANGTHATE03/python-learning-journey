
# Python Loops: break, continue, and pass
# These statements change how loops behave.

# 1. break Statement
# break immediately terminates the loop.

print("Example 1: break")

for i in range(1, 11):
    if i == 5:
        break

    print(i)

# Output:
# 1
# 2
# 3
# 4


# 2. continue Statement
# continue skips the current iteration and moves to the next one.

print("\nExample 2: continue")

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5


# 3. pass Statement
# pass does nothing; it acts as a placeholder.
# The loop continues normally.

print("\nExample 3: pass")

for i in range(1, 6):
    if i == 3:
        pass  # Placeholder for code we may add later.

    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# 4. Using break in a while Loop
# Stop the loop when the counter reaches 4.

print("\nExample 4: break in while loop")

count = 1

while count <= 10:
    if count == 4:
        break

    print(count)
    count += 1

# Output:
# 1
# 2
# 3


# 5. Using continue in a while Loop
# Print numbers from 1 to 5, skipping 3.

print("\nExample 5: continue in while loop")

count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)

# Output:
# 1
# 2
# 4
# 5


# 6. Using break to Find a Number
# Stop searching when the target number is found.

print("\nExample 6: searching for a number")

numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print("Target found:", number)
        break

# Output:
# Target found: 30


# 7. Using continue to Skip Even Numbers
# Print only odd numbers between 1 and 10.

print("\nExample 7: skipping even numbers")

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number, end=" ")

# Output:
# 1 3 5 7 9


# 8. Using pass as a Function Placeholder
# pass can also be used inside an empty function.

print("\n\nExample 8: pass in a function")

def future_function():
    pass  # Function implementation can be added later.

print("Placeholder function defined successfully.")

