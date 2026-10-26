
# ==========================================
# Python Learning Journey
# Topic: String Slicing
# File: string_slicing.py
# ==========================================

text = "Python Programming"

# 1. Accessing Individual Characters
print("1. Accessing Individual Characters")

print("Original String:", text)
print("First Character:", text[0])
print("Third Character:", text[2])
print("Last Character:", text[-1])


# 2. Basic String Slicing
print("\n2. Basic String Slicing")

print("Characters from index 0 to 5:", text[0:6])
print("Characters from index 7 to 17:", text[7:18])


# 3. Omitting Start and Stop Index
print("\n3. Omitting Start and Stop Index")

print("First 6 Characters:", text[:6])
print("From index 7 to end:", text[7:])
print("Complete String:", text[:])


# 4. Negative Index Slicing
print("\n4. Negative Index Slicing")

print("Last 6 Characters:", text[-6:])
print("Everything except last 6:", text[:-6])
print("Characters from -11 to -7:", text[-11:-7])


# 5. Using Step in Slicing
print("\n5. Using Step in Slicing")

word = "ABCDEFGHIJ"

print("Original:", word)
print("Every 2nd Character:", word[::2])
print("Every 3rd Character:", word[::3])
print("Characters from index 1 to 7, step 2:", word[1:8:2])


# 6. Reversing a String
print("\n6. Reversing a String")

print("Original:", text)
print("Reversed:", text[::-1])


# 7. Extracting Parts of a String
print("\n7. Extracting Parts of a String")

email = "tarang@example.com"

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print("Email:", email)
print("Username:", username)
print("Domain:", domain)


# 8. Slicing with Variables
print("\n8. Slicing with Variables")

start = 0
end = 6

print("Selected Text:", text[start:end])


# 9. Slicing a String with a Step
print("\n9. Slicing with a Negative Step")

numbers = "123456789"

print("Original:", numbers)
print("Reverse Order:", numbers[::-1])
print("Reverse Every Second Character:", numbers[::-2])


# 10. Strings Are Immutable
print("\n10. Strings Are Immutable")

language = "Python"
part = language[0:3]

print("Original String:", language)
print("Sliced String:", part)

# Slicing creates a new string.
# It does not modify the original string.

print("\nString slicing examples completed!")

