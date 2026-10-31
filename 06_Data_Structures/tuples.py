
# ==========================================
# Python Learning Journey
# Topic: Tuples
# File: tuples.py
# ==========================================


# 1. Creating a Tuple
print("1. Creating a Tuple")

fruits = ("apple", "banana", "mango", "orange")
print("Fruits:", fruits)

numbers = (10, 20, 30, 40, 50)
print("Numbers:", numbers)

# Tuple with mixed data types
mixed = ("Tarang", 21, 75.5, True)
print("Mixed Tuple:", mixed)


# 2. Creating a Single Element Tuple
print("\n2. Single Element Tuple")

single = (10,)
print("Single Element Tuple:", single)

# Without comma, it is treated as an integer
not_a_tuple = (10)
print("Without comma:", type(not_a_tuple))
print("With comma:", type(single))


# 3. Accessing Tuple Elements
print("\n3. Accessing Tuple Elements")

print("First Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])


# 4. Tuple Slicing
print("\n4. Tuple Slicing")

print("First Three Elements:", numbers[0:3])
print("From Index 2:", numbers[2:])
print("Every Second Element:", numbers[::2])
print("Reversed Tuple:", numbers[::-1])


# 5. Tuple Methods
print("\n5. Tuple Methods")

values = (10, 20, 10, 30, 10, 40)

print("Original Tuple:", values)
print("Count of 10:", values.count(10))
print("Index of 30:", values.index(30))


# 6. Tuple Length and Membership
print("\n6. Tuple Length and Membership")

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

print("Is 30 present?", 30 in numbers)
print("Is 100 present?", 100 in numbers)


# 7. Looping Through a Tuple
print("\n7. Looping Through a Tuple")

for fruit in fruits:
    print(fruit)

print("Using Index:")

for i in range(len(fruits)):
    print(fruits[i])


# 8. Tuple Packing and Unpacking
print("\n8. Tuple Packing and Unpacking")

# Packing
student = ("Tarang", 21, "B.E. IT")
print("Packed Tuple:", student)

# Unpacking
name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# 9. Nested Tuples
print("\n9. Nested Tuples")

students = (
    ("Aarav", 85),
    ("Priya", 92),
    ("Rahul", 78)
)

print("Students:", students)
print("First Student:", students[0])
print("First Student Name:", students[0][0])
print("Second Student Marks:", students[1][1])


# 10. Tuple Concatenation and Repetition
print("\n10. Concatenation and Repetition")

a = (1, 2, 3)
b = (4, 5, 6)

print("Concatenation:", a + b)
print("Repetition:", a * 2)


# 11. Converting List into Tuple
print("\n11. List to Tuple")

my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)

print("Original List:", my_list)
print("Converted Tuple:", my_tuple)


# 12. Converting Tuple into List
print("\n12. Tuple to List")

my_tuple = ("Python", "Java", "C++")
my_list = list(my_tuple)

print("Original Tuple:", my_tuple)
print("Converted List:", my_list)


# 13. Tuple Immutability
print("\n13. Tuple Immutability")

colors = ("red", "green", "blue")

print("Original Tuple:", colors)

# Tuples cannot be modified directly.
# The following statement would cause a TypeError:
# colors[0] = "yellow"

print("Tuples cannot be changed after creation.")


print("\nTuple examples completed!")

