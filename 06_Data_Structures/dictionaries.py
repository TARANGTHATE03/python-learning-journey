
# ==========================================
# Python Learning Journey
# Topic: Dictionaries
# File: dictionaries.py
# ==========================================


# 1. Creating a Dictionary
print("1. Creating a Dictionary")

student = {
    "name": "Tarang",
    "age": 21,
    "course": "B.E. IT",
    "city": "Thane"
}

print(student)


# 2. Accessing Dictionary Values
print("\n2. Accessing Dictionary Values")

print("Name:", student["name"])
print("Age:", student["age"])

# get() safely accesses a key
print("Course:", student.get("course"))
print("Country:", student.get("country", "Not available"))


# 3. Adding New Items
print("\n3. Adding New Items")

student["college"] = "Mumbai University"
student["year"] = "Third Year"

print(student)


# 4. Updating Existing Values
print("\n4. Updating Values")

student["age"] = 22
student["city"] = "Mumbai"

print(student)


# 5. Removing Items
print("\n5. Removing Items")

# pop() removes an item using its key
student.pop("year")
print("After pop():", student)

# popitem() removes the last inserted item
student.popitem()
print("After popitem():", student)

# del removes a specific key
del student["city"]
print("After del:", student)


# 6. Dictionary Methods
print("\n6. Dictionary Methods")

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())


# 7. Looping Through a Dictionary
print("\n7. Looping Through a Dictionary")

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through keys and values
for key, value in student.items():
    print(key, ":", value)


# 8. Checking if a Key Exists
print("\n8. Checking if a Key Exists")

if "name" in student:
    print("Name key exists")

if "marks" not in student:
    print("Marks key does not exist")


# 9. Dictionary Length and Copy
print("\n9. Dictionary Length and Copy")

print("Number of items:", len(student))

student_copy = student.copy()
print("Copied Dictionary:", student_copy)


# 10. Nested Dictionaries
print("\n10. Nested Dictionaries")

students = {
    "student1": {
        "name": "Aarav",
        "marks": 85
    },
    "student2": {
        "name": "Priya",
        "marks": 92
    }
}

print(students)
print("First Student:", students["student1"]["name"])
print("Second Student Marks:", students["student2"]["marks"])


# 11. Updating with update()
print("\n11. Updating with update()")

student.update({"course": "Information Technology"})
student.update({"marks": 90})

print(student)


# 12. Clearing a Dictionary
print("\n12. Clearing a Dictionary")

temporary = {"a": 1, "b": 2}
print("Before clear:", temporary)

temporary.clear()
print("After clear:", temporary)


print("\nDictionary examples completed!")

