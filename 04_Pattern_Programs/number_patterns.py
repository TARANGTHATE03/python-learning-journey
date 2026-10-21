
# Python Pattern Programs - Number Patterns
# Learn nested loops by printing different number patterns.

# 1. Increasing Number Pattern
# Output:
# 1 2 3 4 5

print("1. Increasing Number Pattern")

for i in range(1, 6):
    print(i, end=" ")
print("\n")


# 2. Decreasing Number Pattern
# Output:
# 5 4 3 2 1

print("2. Decreasing Number Pattern")

for i in range(5, 0, -1):
    print(i, end=" ")
print("\n")


# 3. Square Number Pattern
# Prints a 5x5 square using numbers.

# Output:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

print("3. Square Number Pattern")

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()


# 4. Increasing Number Triangle
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("\n4. Increasing Number Triangle")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 5. Repeated Number Triangle
# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

print("\n5. Repeated Number Triangle")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()


# 6. Inverted Number Triangle
# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

print("\n6. Inverted Number Triangle")

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 7. Continuous Number Triangle
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

print("\n7. Continuous Number Triangle")

number = 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()


# 8. Right-Aligned Number Triangle
# Output:
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

print("\n8. Right-Aligned Number Triangle")

for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end="  ")

    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 9. Number Pyramid
# Output:
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

print("\n9. Number Pyramid")

for i in range(1, 6):
    # Print leading spaces
    for space in range(5 - i):
        print(" ", end=" ")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()


# 10. Multiplication Number Pattern
# Output:
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25

print("\n10. Multiplication Number Pattern")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

