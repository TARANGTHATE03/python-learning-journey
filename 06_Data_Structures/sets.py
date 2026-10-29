
# ==========================================
# Python Learning Journey
# Topic: Sets
# File: sets.py
# ==========================================

# 1. Creating a Set
print("1. Creating a Set")

fruits = {"apple", "banana", "mango", "orange"}
print("Fruits:", fruits)

# Sets automatically remove duplicate values
numbers = {1, 2, 3, 2, 1, 4}
print("Numbers:", numbers)

# Creating an empty set
empty_set = set()
print("Empty Set:", empty_set)


# 2. Adding Elements
print("\n2. Adding Elements")

fruits.add("grapes")
print("After add():", fruits)

# Add multiple elements
fruits.update(["kiwi", "watermelon"])
print("After update():", fruits)


# 3. Removing Elements
print("\n3. Removing Elements")

fruits.remove("banana")
print("After remove():", fruits)

# discard() does not raise an error if the element is absent
fruits.discard("pineapple")
print("After discard():", fruits)

# pop() removes and returns an arbitrary element
removed = fruits.pop()
print("Removed Element:", removed)
print("After pop():", fruits)


# 4. Checking Membership
print("\n4. Checking Membership")

colors = {"red", "green", "blue"}

print("Is red present?", "red" in colors)
print("Is yellow present?", "yellow" in colors)


# 5. Set Union
print("\n5. Set Union")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)

print("Union:", a.union(b))
print("Union using |:", a | b)


# 6. Set Intersection
print("\n6. Set Intersection")

print("Intersection:", a.intersection(b))
print("Intersection using &:", a & b)


# 7. Set Difference
print("\n7. Set Difference")

print("A - B:", a.difference(b))
print("B - A:", b.difference(a))
print("Difference using -:", a - b)


# 8. Symmetric Difference
print("\n8. Symmetric Difference")

print("Symmetric Difference:", a.symmetric_difference(b))
print("Using ^:", a ^ b)


# 9. Subset, Superset, and Disjoint
print("\n9. Set Relationships")

x = {1, 2}
y = {1, 2, 3, 4}
z = {7, 8}

print("Is X a subset of Y?", x.issubset(y))
print("Is Y a superset of X?", y.issuperset(x))
print("Are X and Z disjoint?", x.isdisjoint(z))


# 10. Useful Set Methods
print("\n10. Useful Set Methods")

values = {10, 20, 30}

print("Original Set:", values)
print("Number of Elements:", len(values))

values_copy = values.copy()
print("Copied Set:", values_copy)

values.clear()
print("After clear():", values)


# 11. Removing Duplicates from a List
print("\n11. Removing Duplicates")

items = [1, 2, 2, 3, 3, 4, 4, 5]
unique_items = set(items)

print("Original List:", items)
print("Unique Elements:", unique_items)

# Convert back to a list if needed
unique_list = list(unique_items)
print("Unique List:", unique_list)


# 12. Looping Through a Set
print("\n12. Looping Through a Set")

languages = {"Python", "Java", "C++"}

for language in languages:
    print(language)

# Set iteration order is not guaranteed.


print("\nSet examples completed!")

