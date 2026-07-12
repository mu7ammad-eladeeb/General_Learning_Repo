# ==============================================================================
# Topic: Generator Expressions - Squaring Even Numbers
# Source: Coddy Course
# Description:
# Demonstrates how to create and use a generator expression to filter even
# numbers from a range and generate their squares using lazy evaluation.
# ==============================================================================

"""
===============================================================================
OVERVIEW
===============================================================================

Generator expressions provide a concise and memory-efficient way to create
iterators in Python.

In this challenge, you will create a generator expression that:

• Iterates through a range of numbers.
• Filters out odd numbers.
• Squares the remaining even numbers.
• Prints each generated value.

This challenge demonstrates lazy evaluation and how generator expressions
can process data efficiently without storing every value in memory.
"""

# ==============================================================================
# CHALLENGE
# ==============================================================================

"""
Problem
-------
Create a generator expression that filters and transforms a sequence of
numbers.

Input
-----
Two space-separated integers representing:

• start
• end (inclusive)

Requirements
------------
The generator expression should:

1. Iterate through every number from start to end.
2. Filter out odd numbers.
3. Square every even number.
4. Print each squared value on its own line.

Example

Input

1 10

Output

4
16
36
64
100
"""

# ==============================================================================
# THEORY
# ==============================================================================

"""
A generator expression creates an iterator using a compact syntax.

Syntax

(expression for item in iterable if condition)

Unlike list comprehensions, generator expressions do not generate every value
immediately. Instead, values are produced only when requested.

This behavior is called lazy evaluation.

Benefits

• Uses very little memory.
• Ideal for processing large datasets.
• Produces values one at a time.
"""

# ==============================================================================
# SOLUTION
# ==============================================================================

def main():
    # Read the input
    start, end = map(int, input().split())

    # Create a generator expression that squares only even numbers
    generator_exp = (
        x ** 2
        for x in range(start, end + 1)
        if x % 2 == 0
    )

    # Print each generated value
    for value in generator_exp:
        print(value)


# Execute the program only when this file is run directly.
if __name__ == "__main__":
    main()

# ==============================================================================
# DETAILED SOLUTION EXPLANATION
# ==============================================================================

"""
Step 1 — Read the Input
-----------------------

start, end = map(int, input().split())

The user enters two integers.

Example

1 10

After reading the input

start = 1
end = 10

These values define the range of numbers to process.

--------------------------------------------------------------------------

Step 2 — Create the Generator Expression
----------------------------------------

generator_exp = (
    x ** 2
    for x in range(start, end + 1)
    if x % 2 == 0
)

This generator expression has three parts.

Expression

x ** 2

Squares every accepted number.

------------------------------------------------

Iteration

for x in range(start, end + 1)

Iterates through every number from start to end.

Notice the use of

end + 1

because range() excludes its ending value.

------------------------------------------------

Condition

if x % 2 == 0

Only even numbers satisfy this condition.

Odd numbers are skipped automatically.

--------------------------------------------------------------------------

Step 3 — Iterate Through the Generator
--------------------------------------

for value in generator_exp:

Each iteration requests one value from the generator.

Unlike a list, all values are not created at once.

Python generates each square only when needed.

--------------------------------------------------------------------------

Step 4 — Print the Result
-------------------------

print(value)

Each squared even number is printed on its own line.

For the input

1 10

the output becomes

4
16
36
64
100

--------------------------------------------------------------------------

Program Flow

Input

1 10

↓

Generate Numbers

1 2 3 4 5 6 7 8 9 10

↓

Filter

2 4 6 8 10

↓

Square

4 16 36 64 100

↓

Print
"""

# ==============================================================================
# EXAMPLE EXECUTION
# ==============================================================================

"""
Example

Input

1 10

Output

4
16
36
64
100
"""

# ==============================================================================
# KEY CONCEPTS
# ==============================================================================

"""
Generator Expression
--------------------
Creates an iterator using the syntax

(expression for item in iterable if condition)

------------------------------------------------------------

Lazy Evaluation
---------------
Values are generated only when requested instead of all at once.

------------------------------------------------------------

Filtering
---------
The condition

if x % 2 == 0

keeps only even numbers.

------------------------------------------------------------

Transformation
--------------
The expression

x ** 2

transforms each even number into its square.

------------------------------------------------------------

Iteration
---------
The for loop repeatedly calls next() on the generator until all values have
been produced.
"""

# ==============================================================================
# TIME AND SPACE COMPLEXITY
# ==============================================================================

"""
Time Complexity
---------------
O(n)

Every number in the range is visited exactly once.

------------------------------------------------------------

Space Complexity
----------------
O(1)

The generator produces one value at a time and does not store all generated
values in memory.
"""

# ==============================================================================
# COMMON MISTAKES
# ==============================================================================

"""
Mistake 1
---------
Using square brackets [] instead of parentheses ().

Wrong

[x ** 2 for x in range(10)]

This creates a list instead of a generator.

------------------------------------------------------------

Mistake 2
---------
Using

range(start, end)

instead of

range(start, end + 1)

The ending value would not be included.

------------------------------------------------------------

Mistake 3
---------
Forgetting the filtering condition.

Without

if x % 2 == 0

both even and odd numbers would be squared.

------------------------------------------------------------

Mistake 4
---------
Trying to reuse an exhausted generator.

Generators can only be iterated once.

Create a new generator if you need to iterate again.
"""

# ==============================================================================
# QUICK SUMMARY
# ==============================================================================

"""
• Generator expressions create iterators.

• They use parentheses () instead of square brackets [].

• Values are generated lazily.

• The condition filters unwanted values.

• The expression transforms accepted values.

• They are more memory efficient than list comprehensions.

• They are ideal for processing large datasets.
"""
