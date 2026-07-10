# ==============================================================================
# Topic: Challenge - Even Number Iterator Using iter() and next()
# Source: Coddy Course
# Description:
# Complete notes covering the EvenNumberIterator challenge, including the
# problem statement, complete solution, and a detailed step-by-step explanation
# of how iter() and next() work together with the iterator protocol.
# ==============================================================================

"""
📖 CHALLENGE OVERVIEW
--------------------------------------------------------------------------------
Create a custom iterator that generates a sequence of even numbers up to a
given limit.

The challenge demonstrates the use of:

• iter()
• next()
• __iter__()
• __next__()
• StopIteration

Instead of using a for loop, the iterator is manually controlled using
iter() and next().
"""

# ==============================================================================
# Challenge
# ==============================================================================

"""
Problem
-------
Create an iterator that generates a sequence of even numbers up to a given
limit.

Input
-----
A single integer representing the maximum limit.

Requirements
------------
Your iterator should:

• Generate even numbers beginning with 2.
• Continue generating even numbers.
• Stop once the generated number exceeds the given limit.
• Print each generated number on its own line.

Example

Input:
10

Output:
2
4
6
8
10
"""

# ==============================================================================
# Solution
# ==============================================================================

# Read input
# limit = int(input())


class EvenNumberIterator:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2

        if self.current > self.limit:
            raise StopIteration

        return self.current


# Create the iterator
# even_iterator = iter(EvenNumberIterator(limit))

# Print every even number
# try:
#     while True:
#         print(next(even_iterator))
# except StopIteration:
#     pass

# ==============================================================================
# Solution Explanation
# ==============================================================================

"""
Step 1
------
Read the input.

limit = int(input())

Example input:

10

The value is converted into an integer.

limit = 10

--------------------------------------------------------------------------------

Step 2
------
Create the iterator object.

class EvenNumberIterator:

This class follows Python's iterator protocol by implementing both:

• __iter__()
• __next__()

--------------------------------------------------------------------------------

Step 3
------
Initialize the iterator.

def __init__(self, limit):
    self.current = 0
    self.limit = limit

Initially:

current = 0
limit = 10

The iterator begins at zero because the first call to __next__()
will immediately increase it to 2.

--------------------------------------------------------------------------------

Step 4
------
Implement __iter__().

def __iter__(self):
    return self

This makes the object iterable.

Calling:

iter(EvenNumberIterator(limit))

simply returns the iterator itself.

--------------------------------------------------------------------------------

Step 5
------
Implement __next__().

def __next__(self):
    self.current += 2

Every call increases the current number by two.

Example:

First call

current = 2

Second call

current = 4

Third call

current = 6

Fourth call

current = 8

Fifth call

current = 10

--------------------------------------------------------------------------------

Step 6
------
Check whether iteration should stop.

if self.current > self.limit:
    raise StopIteration

Suppose:

limit = 10

The next generated value would be:

12

Since:

12 > 10

Python executes:

raise StopIteration

which tells Python that there are no more values.

--------------------------------------------------------------------------------

Step 7
------
Return the current number.

return self.current

The generated numbers become:

2
4
6
8
10

--------------------------------------------------------------------------------

Step 8
------
Create the iterator.

even_iterator = iter(EvenNumberIterator(limit))

This is equivalent to:

iterator = EvenNumberIterator(limit)
even_iterator = iterator.__iter__()

Since __iter__() returns self,
even_iterator refers to the same iterator object.

--------------------------------------------------------------------------------

Step 9
------
Manually retrieve values using next().

while True:
    print(next(even_iterator))

Each call to next() automatically executes:

even_iterator.__next__()

The returned values are:

2
4
6
8
10

--------------------------------------------------------------------------------

Step 10
-------
Handle StopIteration.

try:
    while True:
        print(next(even_iterator))
except StopIteration:
    pass

When __next__() raises StopIteration,
execution jumps to the except block,
ending the loop gracefully.

Without the try-except block,
Python would display an exception message.

--------------------------------------------------------------------------------

Execution Flow

Input

10

↓

Create iterator

↓

current = 0

↓

next()

↓

2

↓

next()

↓

4

↓

next()

↓

6

↓

next()

↓

8

↓

next()

↓

10

↓

next()

↓

12

↓

12 > 10

↓

raise StopIteration

↓

Loop ends
"""

# ==============================================================================
# Example Run
# ==============================================================================

"""
Input

10

Output

2
4
6
8
10
"""

# ==============================================================================
# Key Concepts Used
# ==============================================================================

"""
iter(object)
-------------
Returns an iterator object by calling:

object.__iter__()

next(iterator)
--------------
Returns the next value by calling:

iterator.__next__()

__iter__()
----------
Returns the iterator object itself.

__next__()
----------
Produces the next value.

StopIteration
-------------
Signals that there are no more values to generate.

try-except
----------
Used to catch StopIteration and terminate iteration without producing an error.

Manual Iteration
----------------
Instead of using a for loop,
this challenge demonstrates explicit iteration using:

iter()

and

next()
"""

# ==============================================================================
# QUICK SUMMARY
# ==============================================================================
#
# iter(obj) -> Calls obj.__iter__().
#
# next(iterator) -> Calls iterator.__next__().
#
# __iter__() -> Returns the iterator object.
#
# __next__() -> Generates the next value.
#
# StopIteration -> Ends the iteration.
#
# This challenge demonstrates manual iteration using iter() and next()
# instead of relying on a for loop.
# ==============================================================================
