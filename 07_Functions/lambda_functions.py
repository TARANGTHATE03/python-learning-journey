
# ==========================================
# Python Learning Journey
# Topic: Lambda Functions
# File: lambda_functions.py
# ==========================================


# 1. Basic Lambda Function
print("1. Basic Lambda Function")

square = lambda x: x * x

print("Square of 5:", square(5))


# 2. Lambda with Multiple Arguments
print("\n2. Lambda with Multiple Arguments")

add = lambda a, b: a + b

print("Sum:", add(10, 20))


# 3. Lambda with Three Arguments
print("\n3. Lambda with Three Arguments")

multiply = lambda a, b, c: a * b * c

print("Multiplication:", multiply(2, 3, 4))


# 4. Lambda with Conditional Expression
print("\n4. Lambda with Conditional Expression")

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print("10 is:", check_even(10))
print("7 is:", check_even(7))


# 5. Using Lambda with map()
print("\n5. Lambda with map()")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Original Numbers:", numbers)
print("Squares:", squares)


# 6. Using Lambda with filter()
print("\n6. Lambda with filter()")

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)


# 7. Using Lambda with sorted()
print("\n7. Lambda with sorted()")

students = [
    ("Aarav", 85),
    ("Priya", 92),
    ("Rahul", 78),
    ("Sneha", 95)
]

# Sort students according to marks
sorted_students = sorted(students, key=lambda x: x[1])

print("Students Sorted by Marks:")
print(sorted_students)


# 8. Using Lambda with max()
print("\n8. Lambda with max()")

numbers = [10, 45, 23, 67, 89, 12]

largest = max(numbers, key=lambda x: x)

print("Largest Number:", largest)


# 9. Using Lambda with min()
print("\n9. Lambda with min()")

smallest = min(numbers, key=lambda x: x)

print("Smallest Number:", smallest)


# 10. Lambda with Strings
print("\n10. Lambda with Strings")

names = ["Tarang", "Aarav", "Rahul", "Priya"]

name_lengths = list(map(lambda name: len(name), names))

print("Names:", names)
print("Name Lengths:", name_lengths)


# 11. Lambda with reduce()
print("\n11. Lambda with reduce()")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Numbers:", numbers)
print("Sum:", total)


print("\nLambda functions examples completed!")

