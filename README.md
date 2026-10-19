# Python Fundamentals — Complete Beginner Roadmap

Python is a beginner-friendly programming language used in cybersecurity, automation, web development, data science, and artificial intelligence.

This roadmap covers the essential concepts you need to learn Python from zero to a practical level.

## Table of Contents

1. [Introduction to Python](#1-introduction-to-python)
2. [Variables and Data Types](#2-variables-and-data-types)
3. [Input and Output](#3-input-and-output)
4. [Operators](#4-operators)
5. [Conditions](#5-conditions)
6. [Loops](#6-loops)
7. [Strings](#7-strings)
8. [Lists, Tuples, Sets, and Dictionaries](#8-lists-tuples-sets-and-dictionaries)
9. [Functions](#9-functions)
10. [Modules and Packages](#10-modules-and-packages)
11. [File Handling](#11-file-handling)
12. [Exception Handling](#12-exception-handling)
13. [Object-Oriented Programming](#13-object-oriented-programming)
14. [Virtual Environments and pip](#14-virtual-environments-and-pip)
15. [Practice Projects](#15-practice-projects)
16. [Cybersecurity with Python](#16-cybersecurity-with-python)

---

## 1. Introduction to Python

Python is a high-level, interpreted programming language known for its readable syntax.

### Your first Python program

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

### Comments

Comments explain code and are ignored by Python.

```python
# This is a single-line comment

print("Learning Python")
```

### Running Python on Linux

Check your Python version:

```bash
python3 --version
```

Create a Python file:

```bash
nano main.py
```

Run the file:

```bash
python3 main.py
```

---

## 2. Variables and Data Types

Variables store values that programs can use.

```python
name = "Abdellah"
age = 18
height = 1.74
is_student = True
```

### Fundamental data types

| Data Type | Example | Description |
|---|---|---|
| `str` | `"Hello"` | Text |
| `int` | `25` | Integer |
| `float` | `1.74` | Decimal number |
| `bool` | `True` | Boolean value |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `tuple` | `(1, 2, 3)` | Ordered, immutable collection |
| `dict` | `{"name": "Ali"}` | Key-value pairs |
| `set` | `{1, 2, 3}` | Unique values |

### Checking data types

Use the `type()` function.

```python
age = 18

print(type(age))
```

Output:

```text
<class 'int'>
```

### Changing data types

```python
age = "18"

age = int(age)

print(age + 2)
```

Output:

```text
20
```

---

## 3. Input and Output

### Output with `print()`

```python
name = "Ali"

print("Hello", name)
```

### Input with `input()`

```python
name = input("Enter your name: ")

print("Hello", name)
```

### Converting user input

The `input()` function returns a string by default.

```python
age = int(input("Enter your age: "))

print("Next year:", age + 1)
```

For decimal input, use `float()`:

```python
height = float(input("Enter your height: "))

print(height)
```

---

## 4. Operators

### Arithmetic operators

```python
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Exponentiation
```

### Comparison operators

```python
print(10 > 5)    # True
print(10 < 5)    # False
print(10 == 10)  # True
print(10 != 5)   # True
print(10 >= 10)  # True
print(5 <= 10)   # True
```

### Logical operators

```python
age = 18
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

### Assignment operators

```python
number = 10

number += 5
number -= 2
number *= 2

print(number)
```

---

## 5. Conditions

Conditions allow programs to make decisions.

### `if`, `elif`, and `else`

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

### Nested conditions

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "example":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Unknown username")
```

This is a learning example only. Real applications should never store passwords directly in source code.

---

## 6. Loops

Loops repeat instructions.

### `for` loop

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### `while` loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### `break`

Stops a loop.

```python
for number in range(10):
    if number == 5:
        break

    print(number)
```

### `continue`

Skips the current iteration.

```python
for number in range(5):
    if number == 2:
        continue

    print(number)
```

---

## 7. Strings

Strings represent text.

```python
message = "Learning Python"

print(message)
print(len(message))
print(message.upper())
print(message.lower())
```

### Indexing

```python
language = "Python"

print(language[0])   # P
print(language[1])   # y
print(language[-1])  # n
```

### Slicing

```python
language = "Python"

print(language[0:3])  # Pyt
print(language[2:])   # thon
print(language[::-1]) # nohtyP
```

### Useful string methods

```python
text = "  hello python  "

print(text.strip())
print(text.replace("python", "world"))
print(text.startswith("  hello"))
print(text.find("python"))
```

### F-strings

F-strings make it easy to insert variables into text.

```python
name = "Ali"
age = 18

print(f"My name is {name} and I am {age} years old.")
```

---

## 8. Lists, Tuples, Sets, and Dictionaries

### Lists

Lists store ordered, changeable collections.

```python
languages = ["Python", "C", "Java"]

print(languages[0])

languages.append("JavaScript")
languages.remove("C")

print(languages)
```

Useful list operations:

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
```

### Tuples

Tuples are ordered and immutable.

```python
coordinates = (10, 20)

print(coordinates[0])
```

### Sets

Sets contain unique values.

```python
numbers = {1, 2, 2, 3, 4}

numbers.add(5)

print(numbers)
```

Duplicate values are removed automatically.

### Dictionaries

Dictionaries store key-value pairs.

```python
student = {
    "name": "Ali",
    "age": 18,
    "language": "Python"
}

print(student["name"])
print(student["age"])

student["age"] = 19
student["country"] = "Algeria"

print(student)
```

---

## 9. Functions

Functions group reusable instructions.

### Defining a function

```python
def greet():
    print("Hello!")

greet()
```

### Parameters and arguments

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")
```

### Returning values

```python
def add(a, b):
    return a + b

result = add(10, 5)

print(result)
```

### Default parameters

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ali")
```

### Multiple return values

```python
def calculate(a, b):
    return a + b, a * b

total, product = calculate(4, 5)

print(total)
print(product)
```

---

## 10. Modules and Packages

Modules allow you to reuse existing Python code.

### Importing a module

```python
import math

print(math.sqrt(25))
print(math.pi)
```

### Using the `random` module

```python
import random

number = random.randint(1, 10)

print(number)
```

### Importing specific functions

```python
from math import sqrt

print(sqrt(36))
```

### Installing packages

Python packages can be installed using `pip`.

```bash
python -m pip install requests
```

Use a virtual environment when working on projects.

---

## 11. File Handling

Python can read and write files.

### Reading a file

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

### Writing to a file

```python
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")
```

The `"w"` mode overwrites an existing file.

### Appending to a file

```python
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\nLearning cybersecurity")
```

### Reading line by line

```python
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

---

## 12. Exception Handling

Exceptions are errors that occur while a program runs.

### Using `try` and `except`

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### Using `finally`

```python
try:
    print("Running program")

finally:
    print("Program finished")
```

The `finally` block runs whether an exception occurs or not.

---

## 13. Object-Oriented Programming

Object-oriented programming (OOP) organizes code using classes and objects.

### Creating a class

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age}.")

student = Student("Ali", 18)

student.introduce()
```

Important concepts:

- **Class:** A blueprint for creating objects.
- **Object:** An instance of a class.
- **Attribute:** Data belonging to an object.
- **Method:** A function defined inside a class.
- **Inheritance:** A way for one class to reuse or extend another class.

---

## 14. Virtual Environments and pip

Virtual environments isolate project dependencies.

### Create a project

```bash
mkdir python-project
cd python-project
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate it on Linux

```bash
source .venv/bin/activate
```

### Install a package

```bash
python -m pip install requests
```

### List installed packages

```bash
python -m pip list
```

### Save dependencies

```bash
python -m pip freeze > requirements.txt
```

### Install saved dependencies

```bash
python -m pip install -r requirements.txt
```

### Deactivate the environment

```bash
deactivate
```

On Kali Linux, avoid using `sudo pip install` to force packages into the system Python environment. A virtual environment is usually the right choice for learning projects.

---

## 15. Practice Projects

Complete these projects in order.

### Beginner projects

1. **Personal Information Program**
   - Ask for a name, age, and favorite programming language.
   - Display the information using f-strings.

2. **Simple Calculator**
   - Accept two numbers.
   - Support addition, subtraction, multiplication, and division.
   - Handle division by zero.

3. **Number Guessing Game**
   - Generate a random number.
   - Let the user guess until they find it.
   - Count the number of attempts.

4. **Temperature Converter**
   - Convert Celsius to Fahrenheit.
   - Convert Fahrenheit to Celsius.

### Intermediate projects

5. **Password Strength Checker**
   - Check password length and character variety.
   - Explain the limitations of simple strength checks.
   - Never save real passwords.

6. **File Analyzer**
   - Read a text file.
   - Count lines, words, and characters.
   - Handle missing files.

7. **Contact Book**
   - Store names and contact information in a dictionary.
   - Add, search, update, and delete entries.
   - Save data in JSON format.

8. **To-Do List**
   - Add and remove tasks.
   - Mark tasks as completed.
   - Save tasks to a file.

---


## Recommended Learning Order

- [ ] Python installation and syntax
- [ ] Variables and data types
- [ ] Input and output
- [ ] Operators
- [ ] Conditions
- [ ] Loops
- [ ] Strings
- [ ] Lists, tuples, sets, and dictionaries
- [ ] Functions
- [ ] Modules and packages
- [ ] File handling
- [ ] Exception handling
- [ ] Object-oriented programming
- [ ] Virtual environments and pip
- [ ] Complete at least three practice projects
- [ ] Start Python cybersecurity projects

## Learning Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Official Python Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

**Final advice:** Practice by writing code yourself rather than only reading examples. Build small projects, understand errors, and gradually combine the concepts you learn.
