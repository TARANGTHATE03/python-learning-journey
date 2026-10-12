# Python Data Types 🐍

## 📌 Introduction

A data type defines the kind of value a variable represents and the operations that can be performed on it.

Python is dynamically typed, which means you do not need to declare a variable's type explicitly. Python determines the type from the value assigned to it.

Example:

```python
age = 21
name = "Tarang"

print(type(age))
print(type(name))
```

Output:

```text
<class 'int'>
<class 'str'>
```

## 📚 Built-in Python Data Types

### 1. Integer (`int`)

Stores whole numbers without a decimal component.

```python
age = 21
marks = 85

print(age)
print(type(age))
```

### 2. Float (`float`)

Stores floating-point numbers, commonly used for decimal values.

```python
price = 99.99
height = 5.7

print(price)
print(type(price))
```

### 3. String (`str`)

Stores text using single, double, or triple quotation marks.

```python
name = "Tarang"
language = 'Python'

print(name)
print(type(name))
```

Strings are immutable, meaning their individual characters cannot be changed in place.

### 4. Boolean (`bool`)

Represents logical values: `True` and `False`.

```python
is_student = True
has_experience = False

print(is_student)
print(type(is_student))
```

Booleans are commonly used in conditions and decision-making.

### 5. List (`list`)

An ordered, mutable collection that allows duplicate values and elements of different types.

```python
subjects = ["Python", "AIML", "Python"]

subjects.append("Data Analysis")

print(subjects)
```

Lists are useful when you need to maintain and update a collection of items.

### 6. Tuple (`tuple`)

An ordered, immutable collection that allows duplicate values.

```python
coordinates = (10, 20, 10)

print(coordinates)
print(type(coordinates))
```

Tuples are useful for collections that should not be modified after creation.

### 7. Set (`set`)

A collection of unique elements. Sets do not preserve a guaranteed positional order.

```python
numbers = {1, 2, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

Sets are useful for removing duplicates and performing set operations.

### 8. Dictionary (`dict`)

Stores data as key-value pairs.

```python
student = {
    "name": "Tarang",
    "age": 21,
    "course": "B.E. IT"
}

print(student["name"])
```

Output:

```text
Tarang
```

Dictionaries are useful for representing structured information.

### 9. Range (`range`)

Represents an arithmetic sequence of integers, often used in loops.

```python
numbers = range(1, 6)

print(list(numbers))
```

Output:

```text
[1, 2, 3, 4, 5]
```

### 10. NoneType (`None`)

`None` represents the absence of a value.

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

## 🔄 Type Conversion

Type conversion changes a value from one data type to another.

```python
number = "100"

converted_number = int(number)
decimal_number = float(converted_number)

print(converted_number)
print(decimal_number)
```

Output:

```text
100
100.0
```

Python provides functions such as `int()`, `float()`, `str()`, and `bool()` for common conversions. Some conversions are not valid; for example, `int("hello")` raises a `ValueError`.

## 📊 Quick Comparison

| Data type | Example | Mutable? |
|---|---|---|
| `int` | `10` | No |
| `float` | `10.5` | No |
| `str` | `"Python"` | No |
| `bool` | `True` | No |
| `list` | `[1, 2, 3]` | Yes |
| `tuple` | `(1, 2, 3)` | No |
| `set` | `{1, 2, 3}` | Yes |
| `dict` | `{"age": 21}` | Yes |
| `range` | `range(5)` | No |
| `NoneType` | `None` | No |

## 🧠 What I Learned

- The purpose of data types in Python.
- The difference between numeric, text, and Boolean types.
- How lists, tuples, sets, and dictionaries store collections.
- How to inspect data types using `type()`.
- How type conversion works.
- The difference between mutable and immutable objects.

## 🎯 Practice Tasks

1. Create variables containing an integer, float, string, and Boolean.
2. Create a list of five programming languages and add another language.
3. Convert the string `"250"` into an integer.
4. Create a set containing duplicate numbers and observe the result.
5. Create a dictionary containing a student's name, age, and course.
6. Use `type()` to inspect each variable.

## 📂 Next Topic

**Type Conversion in Python** — exploring implicit and explicit conversion, conversion functions, and common errors.

---

*Python Learning Journey | Learning step by step, one concept at a time.*