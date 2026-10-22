
# ==========================================
# Python Learning Journey
# Topic: Star Patterns
# File: star_patterns.py
# ==========================================


# 1. Right-Angled Triangle
print("\n1. Right-Angled Triangle")

for i in range(1, 6):
    print("* " * i)


# 2. Inverted Right-Angled Triangle
print("\n2. Inverted Right-Angled Triangle")

for i in range(5, 0, -1):
    print("* " * i)


# 3. Square Pattern
print("\n3. Square Pattern")

for i in range(5):
    print("* " * 5)


# 4. Hollow Square Pattern
print("\n4. Hollow Square Pattern")

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 5. Right-Aligned Triangle
print("\n5. Right-Aligned Triangle")

for i in range(1, 6):
    print("  " * (5 - i) + "* " * i)


# 6. Pyramid Pattern
print("\n6. Pyramid Pattern")

for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "* " * i
    print(spaces + stars)


# 7. Inverted Pyramid
print("\n7. Inverted Pyramid")

for i in range(5, 0, -1):
    spaces = " " * (5 - i)
    stars = "* " * i
    print(spaces + stars)


# 8. Diamond Pattern
print("\n8. Diamond Pattern")

# Upper half
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "* " * i
    print(spaces + stars)

# Lower half
for i in range(4, 0, -1):
    spaces = " " * (5 - i)
    stars = "* " * i
    print(spaces + stars)


# 9. Hollow Right-Angled Triangle
print("\n9. Hollow Right-Angled Triangle")

for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 10. X Pattern
print("\n10. X Pattern")

size = 5

for i in range(size):
    for j in range(size):
        if j == i or j == size - 1 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

