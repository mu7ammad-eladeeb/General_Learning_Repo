# Python Learning Notes — Part 2

## Table of Contents
- [Constants & Variables](#constants--variables)
- [Operators & Identity](#operators--identity)
- [Dictionaries](#dictionaries)
- [Sets](#sets)
- [List Comprehensions](#list-comprehensions)
- [Sorting & Aggregation](#sorting--aggregation)
- [Lambda Functions](#lambda-functions)
- [Recursion](#recursion)
- [Error Handling](#error-handling)
- [Higher-Order Functions](#higher-order-functions)

---

## Constants & Variables

### Constants
```python
PI = 3.14159
HOURS_IN_A_DAY = 24
MAX_USERS = 100
```
> Constants are written in **ALL_UPPERCASE** by convention (اتفاقية — عرف غير مُلزم) — Python doesn't enforce (يُطبّق — يُلزم) immutability (الثبات — عدم القابلية للتغيير), but signals these values should remain unchanged.

### Multiple Assignment (التعيين المتعدد)
```python
a, b, c = 1, 2, 3          # Assign different values
x = y = z = 10             # Assign same value
numbers = [4, 5, 6]
a, b, c = numbers          # Assign from list
```

### Variable Swapping (تبادل قيم المتغيرات)
```python
# Traditional method (الطريقة التقليدية)
temp = a
a = b
b = temp

# Pythonic way (الطريقة المختصرة في بايثون)
a, b = b, a
```

### Placeholder Variables (متغيرات العنصر النائب — تُستخدم لتجاهل قيم غير مطلوبة)
```python
# Ignore loop variable
for _ in range(5):
    print("Looping")

# Ignore values during unpacking (تفريغ — استخراج القيم)
data = (1, 2, 3, 4, 5)
first, _, _, _, last = data
print(first)  # Output: 1
print(last)   # Output: 5
```

### Rounding Numbers
```python
round(number, ndigits)
```

```python
print(round(4.567))    # 5
print(round(4.567, 2)) # 4.57
print(round(456.78, -1)) # 460
```

> Python uses **banker's rounding** (تقريب المصرفيين — يُقرّب إلى أقرب عدد زوجي عند التساوي):
```python
print(round(2.5))  # 2 (rounds down — 2 is even)
print(round(3.5))  # 4 (rounds up — 4 is even)
```

### Casting Iterables (تحويل نوع البيانات) to List
```python
# Tuple to list
my_tuple = (1, 2, 3)
my_list = list(my_tuple)     # [1, 2, 3]

# String to list (splits into characters)
my_list = list("hello")      # ['h', 'e', 'l', 'l', 'o']

# Range to list
my_list = list(range(5))     # [0, 1, 2, 3, 4]
```

---

## Operators & Identity

### Ternary Operator (المعامل الثلاثي — طريقة مختصرة للتعبير عن if-else في سطر واحد)
```python
value_if_true if condition else value_if_false

# Example
age = 20
status = "Eligible" if age >= 18 else "Not Eligible"
```

### Membership Operators (معاملات العضوية — للتحقق من وجود عنصر)
```python
# Check if value exists
print("apple" in fruits)    # True

# Check if value does not exist
print(4 not in numbers)     # True

# In dictionaries — checks keys by default
print("name" in my_dict)    # True
print("Alice" in my_dict)   # False
```

### Identity Operators (معاملات الهوية — للتحقق من أن متغيرين يشيران لنفس الكائن في الذاكرة)
```python
a = [1, 2, 3]
b = a           # b points to same object
c = [1, 2, 3]   # c is a different object with same values

print(a is b)   # True  — same object in memory
print(a is c)   # False — different objects, same values

print(x is not y)  # False — same object
print(x is not z)  # True  — different objects
```

> `is` checks **object identity** (هوية الكائن — موقعه في الذاكرة), while `==` checks **value equality** (تساوي القيم فقط).

### Indentation (المسافة البادئة — ضرورية لتحديد الكتل البرمجية)
```python
# Correct
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Incorrect — causes IndentationError
if x > 5:
print("x is greater than 5")  # IndentationError
```

---

## Dictionaries

### Creating a Dictionary (قاموس — هيكل بيانات يخزن البيانات في أزواج مفتاح-قيمة)
```python
# With key-value pairs
country_capitals = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Empty dictionary
empty_dict = {}
```

### Accessing Values
```python
print(country_capitals["USA"])   # Washington, D.C.
```
> Accessing a key that doesn't exist raises a `KeyError` (خطأ المفتاح — يحدث عند البحث عن مفتاح غير موجود).

### Modifying a Dictionary
```python
my_dict = {}
my_dict["name"] = "Alice"   # Add new key-value pair
my_dict["age"] = 31         # Update existing value
del my_dict["age"]          # Delete key-value pair
```

### Dictionary Methods
```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

my_dict.keys()              # dict_keys(['name', 'age', 'city'])
my_dict.values()            # dict_values(['Alice', 30, 'New York'])
my_dict.items()             # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

my_dict.get('age')          # 30
my_dict.get('country', 'USA')  # 'USA' (default if key not found)

my_dict.pop('city')         # Removes and returns 'New York'
```

### Checking Key Existence (التحقق من وجود مفتاح)
```python
if 'name' in my_dict:
    print('Name exists')

if 'city' not in my_dict:
    print('City does not exist')

if 'age' in my_dict.keys():
    print('Age exists')
```

### Looping Through a Dictionary
```python
for key in my_dict:                    # Keys only
    print(key)

for value in my_dict.values():         # Values only
    print(value)

for key, value in my_dict.items():     # Key-value pairs
    print(f'{key}: {value}')
```

### Nested Dictionary (قاموس متداخل — قاموس داخل قاموس)
```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob":   {"age": 22, "grade": "B"}
}

print(students["Alice"]["age"])   # Output: 20
students["Alice"]["major"] = "Math"
```

---

## Sets

### Creating a Set (مجموعة — تخزن عناصر فريدة غير مكررة وغير مرتبة)
```python
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}
empty_set = set()   # NOT {} — that creates an empty dictionary!
```

### Set Operations
```python
my_set = {1, 2, 3}

my_set.add(4)       # Add element → {1, 2, 3, 4}
my_set.remove(2)    # Remove element (raises KeyError if not found)
my_set.discard(4)   # Remove if exists (no error if missing)
my_set.pop()        # Remove & return arbitrary (عشوائي) element
my_set.clear()      # Remove all elements → set()

print(2 in my_set)  # True — check membership (العضوية — وجود العنصر)
```

### Set Mathematical Operations (العمليات الرياضية على المجموعات)
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (الاتحاد — جميع العناصر من المجموعتين بدون تكرار)
set1 | set2               # {1, 2, 3, 4, 5}
set1.union(set2)

# Intersection (التقاطع — العناصر المشتركة فقط)
set1 & set2               # {3}
set1.intersection(set2)

# Difference (الفرق — عناصر المجموعة الأولى غير الموجودة في الثانية)
set1 - set2               # {1, 2}
set1.difference(set2)

# Symmetric Difference (الفرق المتماثل — العناصر الموجودة في إحداهما فقط)
set1 ^ set2               # {1, 2, 4, 5}
set1.symmetric_difference(set2)
```

### Multiple Set Operations
```python
# Intersection of multiple sets
set1 & set2 & set3
set1.intersection(set2, set3)

# Difference from multiple sets
set1 - set2 - set3
set1.difference(set2, set3)
```

### Subset & Superset (المجموعة الجزئية والمجموعة العظمى)
```python
set1 = {1, 2}
set2 = {1, 2, 3}

set1 <= set2   # True  — subset (مجموعة جزئية — جميع عناصرها موجودة في set2)
set1 < set2    # True  — proper subset (مجموعة جزئية حقيقية — جزئية وغير مساوية)
set2 >= set1   # True  — superset (مجموعة عظمى — تحتوي على جميع عناصر set1)
set2 > set1    # True  — proper superset (مجموعة عظمى حقيقية)
```

### Iterating Over a Set
```python
for element in my_set:
    print(element)

# Iterate in sorted order
for element in sorted(list(my_set)):
    print(element)
```

---

## List Comprehensions

### Basic Comprehension (التعبير القائمي المختصر — طريقة مختصرة لإنشاء قوائم)
```python
new_list = [expression for item in iterable]

# Examples
squares = [n * n for n in numbers]        # [1, 4, 9, 16, 25]
cubes   = [x**3 for x in range(1, 6)]     # [1, 8, 27, 64, 125]
chars   = [char for char in "hello"]      # ['h', 'e', 'l', 'l', 'o']
evens   = [x for x in range(2, 11, 2)]    # [2, 4, 6, 8, 10]
upper   = [word.upper() for word in words] # ['APPLE', 'BANANA', 'CHERRY']
```

### Comprehension with Condition
```python
new_list = [expression for item in iterable if condition]

# Filter even numbers
evens = [n for n in numbers if n % 2 == 0]   # [2, 4, 6]
```

### Comprehension with Aggregation (التجميع — تطبيق دوال على القائمة الناتجة)
```python
numbers = [1, 2, 3, 4, 5, 6]

sum_of_squares = sum([n * n for n in numbers])          # 55
min_absolute   = min([abs(n) for n in [-3,-1,0,1,3]])   # 0
max_even       = max([n for n in numbers if n % 2 == 0]) # 6
```

---

## Sorting & Aggregation

### sorted() Function
```python
# Ascending (تصاعدي)
sorted_numbers = sorted([3,1,4,1,5,9,2,6])   # [1, 1, 2, 3, 4, 5, 6, 9]

# Descending (تنازلي)
sorted_desc = sorted(numbers, reverse=True)   # [9, 6, 5, 4, 3, 2, 1, 1]

# Alphabetically (أبجدياً)
sorted_words = sorted(["apple","banana","cherry"])

# By custom key (مفتاح مخصص للترتيب)
sorted_by_length = sorted(words, key=len)
```

### Advanced Sorting Examples
```python
# Sort strings by length
sorted(names, key=lambda x: len(x))

# Sort dictionary by values
sorted(grades.items(), key=lambda x: x[1])

# Sort by absolute value (القيمة المطلقة)
sorted(numbers, key=lambda x: abs(x))

# Sort tuples by multiple criteria (معايير متعددة)
sorted(data, key=lambda x: (x[1], x[0]))
```

### min(), max(), sum()
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

min(numbers)          # 1
max(numbers)          # 9
sum(numbers)          # 31
sum(numbers, 10)      # 41 (with starting value)

# Works with strings (lexicographical order — الترتيب المعجمي/الأبجدي)
min(["apple","banana","cherry"])  # apple
max(["apple","banana","cherry"])  # cherry
```

---

## Lambda Functions

### Basic Lambda (دالة لامدا — دالة مجهولة الاسم صغيرة الحجم)
```python
# Syntax
lambda arguments: expression

# Example
add = lambda x, y: x + y
result = add(5, 3)   # Output: 8
```

### Lambda with Conditions
```python
# Basic if-else
is_adult = lambda age: "Adult" if age >= 18 else "Minor"

# Multiple conditions (chained — متسلسلة)
grade_status = lambda score: "Amazing!" if score == 100 else "Pass" if score >= 60 else "Fail"
```

### Functions Returning Multiple Values
```python
def get_name_and_age():
    name = "Alice"
    age = 30
    return name, age   # Returns a tuple (صف — بنية بيانات غير قابلة للتغيير)

person_name, person_age = get_name_and_age()   # Unpacking (تفريغ)
```

---

## Recursion

### What Is Recursion? (التكرار الذاتي — دالة تستدعي نفسها)
A recursive function (دالة تكرارية — تستدعي نفسها لحل مسائل أصغر) has two essential parts:
1. **Base case** (الحالة الأساسية — شرط الإيقاف): stops the recursion
2. **Recursive step** (الخطوة التكرارية — الاستدعاء الذاتي): calls the function with smaller input

```python
def recursive_function(parameter):
    if base_case_condition:   # Stop here
        return base_value
    return recursive_step     # Call itself
```

### Factorial Example (المضروب — حاصل ضرب الأعداد من 1 حتى n)
```python
def factorial(n):
    if n == 1:               # Base case
        return 1
    return n * factorial(n - 1)  # Recursive step

print(factorial(5))   # Output: 120
```

### Sum to N
```python
def sum_to_n(n):
    if n == 0:               # Base case
        return 0
    return n + sum_to_n(n - 1)

print(sum_to_n(5))    # Output: 15
```

### String Reversal (عكس السلسلة النصية)
```python
def recursive_reverse(s):
    if len(s) <= 1:          # Base case
        return s
    return recursive_reverse(s[1:]) + s[0]

print(recursive_reverse("hello"))  # Output: olleh
```

---

## Error Handling

### Common Exception Types (أنواع الاستثناءات الشائعة — الأخطاء التي تحدث أثناء تشغيل البرنامج)
| Exception | Cause |
|-----------|-------|
| `TypeError` | Wrong data type used |
| `ValueError` | Correct type, wrong value |
| `IOError` | Input/Output (إدخال/إخراج) failure |
| `ZeroDivisionError` | Division by zero |
| `KeyError` | Dictionary key not found |
| `IndentationError` | Wrong indentation |

### Try-Except Block (كتلة المحاولة والاستثناء — لمنع تعطل البرنامج عند حدوث خطأ)
```python
try:
    risky_code()           # Code that might fail
except ExceptionType:
    handle_error()         # What to do if it fails
```

**Example:**
```python
try:
    num = int("abc")       # Raises ValueError
except ValueError:
    print("Invalid input! Please enter a number.")
```

### Multiple Except Blocks
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Catch Multiple Exceptions in One Block
```python
try:
    pass
except (ValueError, TypeError):
    print("Invalid input type!")
```

> Always place **more specific** exceptions before **more general** ones.

---

## Higher-Order Functions

### map() — Apply Function to Each Element
```python
# With regular function
def square(n):
    return n * n

squared = map(square, [1,2,3,4,5])
print(list(squared))   # [1, 4, 9, 16, 25]

# With lambda
squared = map(lambda n: n * n, [1,2,3,4,5])
print(list(squared))   # [1, 4, 9, 16, 25]
```

> `map()` works with any data type — not just numbers.

### filter() — Keep Elements Where Function Returns True
```python
# With regular function
def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even, [1,2,3,4,5,6])
print(list(even_numbers))   # [2, 4, 6]

# With lambda
even_numbers = filter(lambda n: n % 2 == 0, [1,2,3,4,5,6])
print(list(even_numbers))   # [2, 4, 6]

# Filter strings by length
long_words = filter(lambda word: len(word) > 5, ["apple","banana","cherry","date"])
print(list(long_words))     # ["banana", "cherry"]
```

> `filter()` takes: (1) a function returning True/False, (2) a sequence to filter.
