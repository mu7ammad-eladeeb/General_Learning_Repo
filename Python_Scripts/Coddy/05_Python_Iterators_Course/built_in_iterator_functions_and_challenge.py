# ==============================================================================
# Topic: Built-in Iterator Functions in Python
# Source: Coddy Course
# Description:
# Complete notes covering Python's built-in iterator functions:
# enumerate(), zip(), and reversed(), along with a challenge solution
# and a detailed explanation.
# ==============================================================================

"""
📖 CONCEPT OVERVIEW
--------------------------------------------------------------------------------
Python provides several built-in functions that work with iterators, making
it easier to manipulate and process iterable data.

These functions help you write cleaner, more readable, and more Pythonic code.

The three most commonly used iterator-related functions are:

1. enumerate()
2. zip()
3. reversed()
"""

# ==============================================================================
# 1. enumerate()
# ==============================================================================

"""
The enumerate() function adds a counter to an iterable and returns an
enumerate object (an iterator).

It is especially useful whenever you need both the index and the value of
elements while iterating.

Syntax:
    enumerate(iterable, start=0)

Parameters:
    iterable  -> Any iterable object.
    start     -> Optional starting value for the counter (default is 0).
"""

print("=== enumerate() Example ===")

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

"""
Output:
0: apple
1: banana
2: cherry
"""

"""
How enumerate() Works
--------------------------------------------------------------------------------
Internally, enumerate() pairs every element with an index.

It behaves like:

(0, "apple")
(1, "banana")
(2, "cherry")

The for loop automatically unpacks each tuple into:

index
fruit
"""

print("\n=== enumerate(start=1) Example ===")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

"""
Output:
1 apple
2 banana
3 cherry
"""

"""
Common Uses
--------------------------------------------------------------------------------
• Numbering menu items
• Displaying ordered lists
• Tracking positions
• Avoiding manual index variables
"""

# ==============================================================================
# 2. zip()
# ==============================================================================

"""
The zip() function combines two or more iterables into an iterator of tuples.

Each tuple contains the elements from the same position of every iterable.

Syntax:

    zip(iterable1, iterable2, ...)
"""

print("\n=== zip() Example ===")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

"""
Output:
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
"""

"""
How zip() Works
--------------------------------------------------------------------------------
zip(names, ages)

Produces:

("Alice", 25)
("Bob", 30)
("Charlie", 35)

The loop automatically unpacks each tuple.
"""

print("\n=== zip() with Different Length Lists ===")

letters = ["A", "B", "C"]
numbers = [1, 2]

for pair in zip(letters, numbers):
    print(pair)

"""
Output:
('A', 1)
('B', 2)

zip() stops when the shortest iterable ends.
"""

print("\n=== zip() with Three Iterables ===")

countries = ["USA", "Canada", "UK"]

for name, age, country in zip(names, ages, countries):
    print(name, age, country)

"""
Output:
Alice 25 USA
Bob 30 Canada
Charlie 35 UK
"""

print("\n=== Creating a Dictionary with zip() ===")

people = dict(zip(names, ages))
print(people)

"""
Output:
{'Alice': 25, 'Bob': 30, 'Charlie': 35}
"""

"""
Common Uses
--------------------------------------------------------------------------------
• Combining related lists
• Parallel iteration
• Creating dictionaries
• Pairing multiple sequences
"""

# ==============================================================================
# 3. reversed()
# ==============================================================================

"""
The reversed() function returns a reverse iterator that accesses the elements
of a sequence in reverse order.

Unlike slicing ([::-1]), reversed() does not create a copy of the sequence,
making it more memory efficient.

Syntax:

    reversed(sequence)
"""

print("\n=== reversed() Example ===")

numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers):
    print(number)

"""
Output:
5
4
3
2
1
"""

print("\n=== Convert Reverse Iterator to List ===")

print(list(reversed(numbers)))

"""
Output:
[5, 4, 3, 2, 1]
"""

print("\n=== Reverse a String ===")

text = "Python"

print("".join(reversed(text)))

"""
Output:
nohtyP
"""

"""
Common Uses
--------------------------------------------------------------------------------
• Reverse iteration
• Displaying newest items first
• Palindrome checking
• Reverse data processing
"""

# ==============================================================================
# Challenge: Product Listing Formatter
# ==============================================================================

"""
Challenge
---------
Create a program that processes a list of products and their prices by
combining enumerate(), zip(), and reversed().

Requirements:
- Read product names separated by commas.
- Read corresponding prices separated by commas.
- Convert prices to floats.
- Pair products with prices using zip().
- Reverse the paired items using reversed().
- Number each item using enumerate(), starting from 1.
- Print each item in the format:

#<counter>. <product>: $<price>

One item should be printed per line.
"""

# ==============================================================================
# Solution
# ==============================================================================

# Read input
# products = input().split(',')
# prices = input().split(',')

# Convert prices to floats
# prices = [float(price) for price in prices]

# Process the data
# for counter, (product, price) in enumerate(
#         reversed(list(zip(products, prices))), start=1):
#     print(f"#{counter}. {product}: ${price:.2f}")

"""
Example Input

Apple,Banana,Orange
1.5,0.8,2.25

Example Output

#1. Orange: $2.25
#2. Banana: $0.80
#3. Apple: $1.50
"""

"""
Solution Explanation
--------------------------------------------------------------------------------

Step 1
-------
Read the input and split each line by commas.

products = input().split(',')
prices = input().split(',')

Result:

products

['Apple', 'Banana', 'Orange']

prices

['1.5', '0.8', '2.25']


Step 2
-------
Convert price strings into floating-point numbers.

prices = [float(price) for price in prices]

Result:

[1.5, 0.8, 2.25]


Step 3
-------
Pair products with prices using zip().

zip(products, prices)

Produces:

('Apple', 1.5)
('Banana', 0.8)
('Orange', 2.25)


Step 4
-------
Convert the zip iterator into a list.

list(zip(products, prices))

Result:

[
    ('Apple', 1.5),
    ('Banana', 0.8),
    ('Orange', 2.25)
]


Step 5
-------
Reverse the list.

reversed(list(zip(products, prices)))

Produces:

('Orange', 2.25)
('Banana', 0.8)
('Apple', 1.5)


Step 6
-------
Add numbering with enumerate().

enumerate(reversed(...), start=1)

Produces:

(1, ('Orange', 2.25))
(2, ('Banana', 0.8))
(3, ('Apple', 1.5))


Step 7
-------
Unpack the values.

for counter, (product, price) in ...

First iteration:

counter = 1
product = "Orange"
price = 2.25


Step 8
-------
Print the formatted output.

print(f"#{counter}. {product}: ${price:.2f}")

Output:

#1. Orange: $2.25
"""

# ==============================================================================
# QUICK SUMMARY
# ==============================================================================
#
# enumerate() -> Adds an index while iterating.
#
# zip() -> Combines multiple iterables into tuples.
#
# reversed() -> Iterates through a sequence in reverse order.
#
# enumerate(..., start=1) -> Starts counting from 1.
#
# zip() stops when the shortest iterable ends.
#
# reversed() returns an iterator instead of copying the sequence.
#
# These built-in iterator functions simplify iteration and improve code
# readability in Python.
# ==============================================================================
