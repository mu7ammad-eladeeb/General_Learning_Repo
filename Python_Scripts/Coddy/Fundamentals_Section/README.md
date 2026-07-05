# Python Learning Notes

## Table of Contents
- [Basics](#basics)
- [Variables & Data Types](#variables--data-types)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Loops](#loops)
- [Functions](#functions)
- [Lists](#lists)
- [Tuples](#tuples)
- [Strings](#strings)

---

## Basics

### Printing
```python
print("Hello World!")
```
> Text inside quotation marks is case-sensitive.

### Comments
```python
# Single-line comment

"""
Multi-line comment
"""
```

### User Input
```python
var = input()  # Always stored as a string
name = input()
print("Hello, " + name)
```

### F-Strings
```python
age = 10
print(f"His age is: {age}")
# Output: His age is: 10
```

### Casting
```python
var = int(input())    # String to int
var = float(input())  # String to float
var = bool(input())   # To boolean
var = str(input())    # To string
```
> Adding strings concatenates them: `"5" + "5" = "55"`  
> Adding numbers performs arithmetic: `5 + 5 = 10`

---

## Variables & Data Types

### Variable Initialization
```python
variable_name = value
```

### Number Types
```python
a = 3      # int (integer)
b = 13.2   # float (real number)
```

### Boolean
```python
variable_true = True
variable_false = False
```
> Boolean values are case-sensitive — must start with capital letter.

### String / Char
```python
s1 = 'This is a string'
s2 = "This is also a string"
```
> A **char** is a single character. A **str** is a sequence of multiple characters.

### None
```python
empty_box = None  # Represents "no value"
```

### Naming Conventions
```python
# Good — snake_case, descriptive
age = 10
is_active = True

# Bad
isActive = False  # not snake_case
a = 10            # not descriptive
```

---

## Operators

### Arithmetic Operators
| Operator | Operation      | Example     |
|----------|----------------|-------------|
| `+`      | Addition       | `3 + 2 = 5` |
| `-`      | Subtraction    | `3 - 2 = 1` |
| `*`      | Multiplication | `3 * 2 = 6` |
| `/`      | Division       | `4 / 2 = 2` |
| `%`      | Modulo         | `10 % 3 = 1`|

#### Modulo Use Cases
```python
# Even number
number % 2 == 0

# Odd number
number % 2 == 1
```

### Augmented Assignment Operators
| Operation      | Shortcut | Example              |
|----------------|----------|----------------------|
| Addition       | `+=`     | `a += 3` → `a = a + 3` |
| Subtraction    | `-=`     | `a -= 3`             |
| Multiplication | `*=`     | `a *= 3`             |
| Division       | `/=`     | `a /= 3`             |
| Modulus        | `%=`     | `a %= 3`             |

### Comparison Operators
| Operator | Meaning                | Example          |
|----------|------------------------|------------------|
| `==`     | Equal                  | `1 == 2` → False |
| `!=`     | Not Equal              | `1 != 2` → True  |
| `>`      | Greater Than           | `1 > 2`  → False |
| `<`      | Less Than              | `1 < 2`  → True  |
| `>=`     | Greater Than or Equal  | `1 >= 2` → False |
| `<=`     | Less Than or Equal     | `1 <= 2` → True  |

### Logical Operators
| Operator | Meaning                        | Example   |
|----------|--------------------------------|-----------|
| `and`    | True if all operands are True  | `a and b` |
| `or`     | True if any operand is True    | `a or b`  |
| `not`    | True if operand is False       | `not a`   |

#### Truth Tables

**AND**
| a     | b     | a and b |
|-------|-------|---------|
| False | False | False   |
| False | True  | False   |
| True  | False | False   |
| True  | True  | True    |

**OR**
| a     | b     | a or b |
|-------|-------|--------|
| False | False | False  |
| False | True  | True   |
| True  | False | True   |
| True  | True  | True   |

**NOT**
| a     | not a |
|-------|-------|
| False | True  |
| True  | False |

#### Logical Simplification
```python
not (A and B)  ==  (not A) or (not B)
not (A or B)   ==  (not A) and (not B)
```

---

## Control Flow

### If / Elif / Else
```python
if condition:
    code
elif another_condition:
    code
else:
    code
```

**Example:**
```python
age = 68
status = "None"
if age < 18:
    status = "Young"
elif age >= 18 and age <= 65:
    status = "Adult"
else:
    status = "Old"
```

### Nested If Statements
```python
if age > 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")
```

---

## Loops

### While Loop
```python
while condition:
    code
```

**Example:**
```python
number = 27
power_of_two = 1

while power_of_two <= number:
    power_of_two *= 2

print(power_of_two)  # 32
```

### For Loop
```python
for i in range(start, end):
    # code
```

#### range() Variations
```python
range(stop)         # 0 to stop (exclusive)
range(start, stop)  # start to stop (exclusive)
range(start, stop, step)  # with step

# Examples
for i in range(5):       # 0, 1, 2, 3, 4
for i in range(2, 6):    # 2, 3, 4, 5
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
for i in range(10, 0, -2): # 10, 8, 6, 4, 2
```

### Nested Loops
```python
for x in range(2):
    for y in range(2):
        print(x, y)
# Output: 0 0 / 0 1 / 1 0 / 1 1
```

### Loop Control

#### break — Exit the loop immediately
```python
for i in range(10):
    if i == 6:
        break
    print(i)
# Prints 0 to 5
```

#### continue — Skip current iteration
```python
for i in range(3, 9):
    if i == 5:
        continue
    print(i)
# Output: 3, 4, 6, 7, 8
```

---

## Functions

### Basic Function
```python
def function_name():
    # function body
    return value

number = function_name()  # Capture return value
```

### Function Arguments
```python
def function_name(arg1, arg2):
    # function code

function_name(value1, value2)
```

### Default Arguments
```python
def greet(name, greeting="Hello"):
    print(name, greeting)

greet("John")           # John Hello
greet("John", "Welcome") # John Welcome
```

**Multiple default arguments:**
```python
def describe_person(name, age=25, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}")
```

> **Important:** Default arguments must come AFTER non-default arguments.
```python
# Correct
def greet(name, greeting="Hello"):

# Incorrect
def greet(greeting="Hello", name):
```

---

## Lists

### Creating & Accessing
```python
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
element = my_list[2]   # Access by index (starts at 0)
length = len(my_list)  # Get length
```

### Modifying Elements
```python
my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
# ["apple", "orange", "cherry"]
```

### Basic List Methods
```python
my_list = [1, 9, 2, 3]
my_list.append(5)   # Add to end → [1, 9, 2, 3, 5]
my_list.sort()      # Sort ascending → [1, 2, 3, 5, 9]
my_list.reverse()   # Reverse order
my_list.pop(index)  # Remove & return element at index
my_list.clear()     # Remove all elements → []
```

### Iterating Over a List
```python
# Simple iteration
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# With range and len
for i in range(len(my_list)):
    print(my_list[i])
```

### Checking Membership
```python
element in list      # True if element is in the list
element not in list  # True if element is not in the list
```

### List Operators
```python
# Combine lists
combined = list1 + list2
# [1,2,3] + [4,5,6] = [1, 2, 3, 4, 5, 6]

# Repeat list
repeated = list * n
# [1, 2] * 3 = [1, 2, 1, 2, 1, 2]
```

### Slicing
Syntax: `lst[start:stop:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:6]    # [2, 3, 4, 5]       — basic slice
numbers[:5]     # [0, 1, 2, 3, 4]    — from start
numbers[5:]     # [5, 6, 7, 8, 9]    — to end
numbers[1:8:2]  # [1, 3, 5, 7]       — every 2nd element
numbers[2::3]   # [2, 5, 8]          — every 3rd from index 2
numbers[-3:]    # [7, 8, 9]          — last 3 elements
numbers[:-2]    # [0,1,2,3,4,5,6,7]  — all except last 2
numbers[::-1]   # [9,8,7,6,5,4,3,2,1,0] — reversed
```

> - Negative indices count from the end
> - Empty start = beginning of list
> - Empty stop = end of list
> - Negative step = reverse order

---

## Tuples

```python
# Creating a tuple (immutable — read-only)
coordinates = (4, 5)

# Accessing elements (indexing works same as lists)
x = coordinates[0]   # 4
y = coordinates[1]   # 5
y = coordinates[-1]  # 5 (negative indexing)
```

> Tuples are **immutable** — cannot be modified after creation.

---

## Strings

### Iterating Over Strings
```python
text = "Hey"

# Using for loop
for char in text:
    print(char)

# Using index
for i in range(len(text)):
    print(f"position {i}: {text[i]}")

# Convert to lowercase
char.lower()
```

### Splitting & Joining
```python
# Split string into list
text = "apple banana cherry"
fruits = text.split()         # Split by whitespace → ['apple', 'banana', 'cherry']

data = "john,25,new york"
info = data.split(',')        # Split by comma → ['john', '25', 'new york']

# Join list into string
words = ['Hello', 'World', 'Python']
text = ' '.join(words)        # "Hello World Python"

fruits = ['apple', 'banana', 'cherry']
line = ','.join(fruits)       # "apple,banana,cherry"
```
