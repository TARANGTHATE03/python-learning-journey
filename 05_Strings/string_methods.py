
# ==========================================
# Python Learning Journey
# Topic: String Methods
# File: string_methods.py
# ==========================================

text = "  Hello, Python World!  "

# 1. Changing Case
print("1. Changing Case")

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())
print("Swap Case:", text.swapcase())


# 2. Removing Whitespace
print("\n2. Removing Whitespace")

print("Strip:", text.strip())
print("Left Strip:", text.lstrip())
print("Right Strip:", text.rstrip())


# 3. Searching in Strings
print("\n3. Searching in Strings")

message = "Python is easy to learn"

print("Find 'easy':", message.find("easy"))
print("Index of 'Python':", message.index("Python"))
print("Count of 'o':", message.count("o"))
print("Starts with 'Python':", message.startswith("Python"))
print("Ends with 'learn':", message.endswith("learn"))


# 4. Replacing Text
print("\n4. Replacing Text")

sentence = "I like Java"

print("Original:", sentence)
print("After Replace:", sentence.replace("Java", "Python"))


# 5. Splitting a String
print("\n5. Splitting a String")

fruits = "apple,banana,mango"

print("Split:", fruits.split(","))
print("Split by spaces:", "Python is easy".split())


# 6. Joining Strings
print("\n6. Joining Strings")

words = ["Python", "is", "awesome"]

print("Joined with spaces:", " ".join(words))
print("Joined with hyphens:", "-".join(words))


# 7. Checking String Content
print("\n7. Checking String Content")

print("Is alphabetic:", "Python".isalpha())
print("Is numeric:", "12345".isnumeric())
print("Is alphanumeric:", "Python123".isalnum())
print("Is lowercase:", "hello".islower())
print("Is uppercase:", "HELLO".isupper())
print("Is title case:", "Hello World".istitle())
print("Is whitespace:", "   ".isspace())


# 8. Checking and Formatting Text
print("\n8. Checking and Formatting Text")

print("Left Justify:", "Python".ljust(12, "-"))
print("Right Justify:", "Python".rjust(12, "-"))
print("Center:", "Python".center(12, "-"))
print("Zero Fill:", "42".zfill(5))


# 9. Removing Characters from Both Ends
print("\n9. Removing Characters")

word = "Python!!!"

print("Original:", word)
print("Remove !:", word.rstrip("!"))

sample = "www.example.com"
print("Remove w and . from ends:", sample.strip("w."))


# 10. String Length
print("\n10. String Length")

language = "Python"

print("String:", language)
print("Length:", len(language))


# Important: Strings Are Immutable
print("\n11. Strings Are Immutable")

original = "python"
updated = original.upper()

print("Original string:", original)
print("Updated string:", updated)

# upper() returns a new string; it does not modify the original.

print("\nString methods examples completed!")

