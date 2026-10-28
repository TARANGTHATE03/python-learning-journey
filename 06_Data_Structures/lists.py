
# ==========================================
# Python Learning Journey
# Topic: Lists
# File: lists.py
# ==========================================

# 1. Creating a List
print("1. Creating a List")

fruits = ["apple", "banana", "mango", "orange"]
print("Fruits:", fruits)

numbers = [10, 20, 30, 40, 50]
print("Numbers:", numbers)

mixed = ["Tarang", 21, 75.5, True]
print("Mixed List:", mixed)


# 2. Accessing List Elements
print("\n2. Accessing List Elements")

print("First Fruit:", fruits[0])
print("Second Fruit:", fruits[1])
print("Last Fruit:", fruits[-1])


# 3. List Slicing
print("\n3. List Slicing")

print("First Three Elements:", numbers[0:3])
print("From Index 2:", numbers[2:])
print("Every Second Element:", numbers[::2])
print("Reversed List:", numbers[::-1])


# 4. Adding Elements
print("\n4. Adding Elements")

fruits.append("grapes")
print("After append():", fruits)

fruits.insert(1, "pineapple")
print("After insert():", fruits)

fruits.extend(["kiwi", "watermelon"])
print("After extend():", fruits)


# 5. Updating Elements
print("\n5. Updating Elements")

fruits[0] = "strawberry"
print("Updated Fruits:", fruits)


# 6. Removing Elements
print("\n6. Removing Elements")

fruits.remove("banana")
print("After remove():", fruits)

removed_fruit = fruits.pop()
print("Popped Element:", removed_fruit)
print("After pop():", fruits)

del fruits[0]
print("After del:", fruits)


# 7. Useful List Methods
print("\n7. Useful List Methods")

values = [10, 20, 10, 30, 10, 40]

print("Original List:", values)
print("Count of 10:", values.count(10))
print("Index of 30:", values.index(30))

values_copy = values.copy()
print("Copied List:", values_copy)

values_copy.clear()
print("Cleared List:", values_copy)


# 8. Sorting and Reversing
print("\n8. Sorting and Reversing")

marks = [75, 92, 68, 85, 80]

marks.sort()
print("Ascending Order:", marks)

marks.sort(reverse=True)
print("Descending Order:", marks)

marks.reverse()
print("Reversed Order:", marks)


# 9. Looping Through a List
print("\n9. Looping Through a List")

for fruit in ["apple", "banana", "mango"]:
    print(fruit)

print("Using index:")

for i in range(len(numbers)):
    print(numbers[i])


# 10. List Length and Membership
print("\n10. List Length and Membership")

print("Number of Elements:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

if 30 in numbers:
    print("30 exists in the list")


# 11. List Comprehension
print("\n11. List Comprehension")

squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)


# 12. Nested Lists
print("\n12. Nested Lists")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:", matrix)
print("Element at Row 1, Column 2:", matrix[0][1])


# 13. Copying a List
print("\n13. Copying a List")

original = [1, 2, 3]
copied = original.copy()

copied.append(4)

print("Original List:", original)
print("Copied List:", copied)


print("\nList examples completed!")

