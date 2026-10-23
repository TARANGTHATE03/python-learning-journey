
# ==========================================
# Python Learning Journey
# Topic: String Formatting
# File: string_formating.py
# ==========================================

# 1. Basic String Formatting
name = "Tarang"
age = 21

print("1. Basic String Formatting")
print("My name is", name, "and I am", age, "years old.")


# 2. Using f-strings (Recommended)
print("\n2. Using f-strings")

print(f"My name is {name} and I am {age} years old.")

# We can perform calculations inside f-strings
print(f"Next year, I will be {age + 1} years old.")


# 3. Using the format() Method
print("\n3. Using the format() Method")

print("My name is {} and I am {} years old.".format(name, age))

# Using positional indexes
print("Name: {0}, Age: {1}".format(name, age))
print("Age: {1}, Name: {0}".format(name, age))


# 4. Using % Formatting
print("\n4. Using % Formatting")

print("My name is %s and I am %d years old." % (name, age))

# %s represents a string
# %d represents an integer
# %f represents a floating-point number


# 5. Formatting Floating-Point Numbers
print("\n5. Formatting Floating-Point Numbers")

price = 123.456789

print(f"Original price: {price}")
print(f"Price to 2 decimal places: {price:.2f}")
print("Price using format(): {:.2f}".format(price))
print("Price using % formatting: %.2f" % price)


# 6. Aligning Text
print("\n6. Aligning Text")

print(f"|{name:<15}|")  # Left alignment
print(f"|{name:>15}|")  # Right alignment
print(f"|{name:^15}|")  # Center alignment


# 7. Adding Leading Zeros
print("\n7. Adding Leading Zeros")

number = 42

print(f"Number: {number}")
print(f"Formatted number: {number:05d}")


# 8. Formatting Percentages
print("\n8. Formatting Percentages")

percentage = 0.8567

print(f"Percentage: {percentage:.2%}")


# 9. Formatting Numbers with Commas
print("\n9. Formatting Numbers with Commas")

population = 1234567

print(f"Population: {population:,}")


# 10. Displaying Multiple Variables
print("\n10. Displaying Multiple Variables")

course = "Python Programming"
duration = 30
level = "Beginner"

print(f"Course: {course}")
print(f"Duration: {duration} days")
print(f"Level: {level}")

print("\nString formatting examples completed!")

