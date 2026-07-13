# ==============================================================================
# Topic: Custom Range Iterator - StepRange Challenge
# Source: Coddy Course
# Description:
# Learn how to create a custom iterator that behaves similarly to Python's
# built-in range() function while supporting custom positive and negative
# step sizes.
# ==============================================================================

"""
===============================================================================
OVERVIEW
===============================================================================

In this challenge, you will create a custom iterator class named StepRange.

The StepRange iterator behaves similarly to Python's built-in range()
function. It generates numbers beginning at a starting value, moving by a
specified step, and stopping before reaching the stop value.

Unlike a normal range, this challenge focuses on implementing the iterator
protocol yourself using the __iter__() and __next__() methods.

By completing this challenge, you will learn:

• How custom iterators work.
• How __iter__() and __next__() interact.
• How StopIteration ends an iteration.
• How to support both positive and negative step sizes.
"""

# ==============================================================================
# CHALLENGE
# ==============================================================================

"""
Problem
-------
Create a custom iterator class called StepRange.

Input
-----
Three space-separated integers:

start stop step

Requirements
------------
Your StepRange class should:

• Accept start, stop, and step in its constructor.
• Implement the __iter__() method.
• Implement the __next__() method.
• Support positive and negative step sizes.
• Raise StopIteration when the sequence ends.

After creating the iterator, print every generated number on its own line.

Example

Input

2 12 2

Output

2
4
6
8
10
"""

# ==============================================================================
# THEORY
# ==============================================================================

"""
Python's built-in range() object is an iterator-like object that generates
numbers one at a time.

This challenge recreates that behavior using a custom class.

To become an iterator, a class must implement:

• __iter__()
• __next__()

The iterator remembers its current position and returns one value each time
next() is called.

When no values remain, __next__() raises StopIteration.

A for loop automatically handles this exception.
"""

# ==============================================================================
# SOLUTION
# ==============================================================================

class StepRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if (
            (self.step > 0 and self.current >= self.stop)
            or
            (self.step < 0 and self.current <= self.stop)
        ):
            raise StopIteration

        result = self.current
        self.current += self.step
        return result


def main():
    start, stop, step = map(int, input().split())

    step_range = StepRange(start, stop, step)

    for value in step_range:
        print(value)


if __name__ == "__main__":
    main()

# ==============================================================================
# DETAILED SOLUTION EXPLANATION
# ==============================================================================

"""
Step 1 — Read the Input
-----------------------

start, stop, step = map(int, input().split())

Example

Input

2 12 2

After reading the input

start = 2
stop = 12
step = 2

--------------------------------------------------------------------------

Step 2 — Create the Iterator

class StepRange:

This class stores everything needed to generate numbers one at a time.

--------------------------------------------------------------------------

Step 3 — Initialize the Iterator

def __init__(self, start, stop, step):

The constructor stores

self.start

The starting value.

----------------------------

self.stop

The stopping value.

----------------------------

self.step

The amount added (or subtracted) after every iteration.

----------------------------

self.current

Keeps track of the next number to return.

Initially,

current = start

--------------------------------------------------------------------------

Step 4 — Implement __iter__()

def __iter__(self):
    return self

The __iter__() method returns the iterator object itself.

This allows Python to use the object inside a for loop.

Internally,

for value in step_range

first calls

iter(step_range)

which executes

step_range.__iter__()

--------------------------------------------------------------------------

Step 5 — Implement __next__()

def __next__(self):

This method returns one value every time Python requests it.

Before returning a value, it checks whether iteration should stop.

Positive step

if self.current >= self.stop

Iteration ends.

Negative step

if self.current <= self.stop

Iteration ends.

If either condition is true,

StopIteration

is raised.

--------------------------------------------------------------------------

Step 6 — Save the Current Value

result = self.current

The current value is stored before updating it.

--------------------------------------------------------------------------

Step 7 — Move to the Next Value

self.current += self.step

If

step = 2

the sequence becomes

2

↓

4

↓

6

↓

8

↓

10

If

step = -2

the sequence becomes

10

↓

8

↓

6

↓

4

↓

2

--------------------------------------------------------------------------

Step 8 — Return the Value

return result

The stored value is returned to the caller.

Python then requests another value until StopIteration occurs.

--------------------------------------------------------------------------

Program Flow

Input

2 12 2

↓

Create StepRange

↓

current = 2

↓

Return 2

↓

current = 4

↓

Return 4

↓

current = 6

↓

Return 6

↓

current = 8

↓

Return 8

↓

current = 10

↓

Return 10

↓

current = 12

↓

StopIteration
"""

# ==============================================================================
# EXAMPLE EXECUTION
# ==============================================================================

"""
Example 1

Input

2 12 2

Output

2
4
6
8
10

------------------------------------------------------------

Example 2

Input

10 0 -3

Output

10
7
4
1
"""

# ==============================================================================
# KEY CONCEPTS
# ==============================================================================

"""
Custom Iterator
---------------
A class that implements the iterator protocol.

------------------------------------------------------------

__iter__()
----------
Returns the iterator object.

Usually

return self

------------------------------------------------------------

__next__()
----------
Returns one value at a time.

Raises StopIteration when finished.

------------------------------------------------------------

Positive Step
-------------
Numbers increase.

Example

StepRange(1, 6, 1)

Produces

1
2
3
4
5

------------------------------------------------------------

Negative Step
-------------
Numbers decrease.

Example

StepRange(5, 0, -1)

Produces

5
4
3
2
1

------------------------------------------------------------

StopIteration
-------------
Signals the end of iteration.

A for loop automatically catches this exception and stops.
"""

# ==============================================================================
# TIME AND SPACE COMPLEXITY
# ==============================================================================

"""
Time Complexity
---------------
O(n)

Each generated value is produced exactly once.

------------------------------------------------------------

Space Complexity
----------------
O(1)

Only a few instance variables are stored regardless of how many numbers
are generated.
"""

# ==============================================================================
# COMMON MISTAKES
# ==============================================================================

"""
Mistake 1
---------
Forgetting to return self inside __iter__().

Without this, the object is not a valid iterator.

------------------------------------------------------------

Mistake 2
---------
Returning self.current before checking the stopping condition.

This may generate one extra value.

------------------------------------------------------------

Mistake 3
---------
Using only one stopping condition.

Positive and negative steps require different comparisons.

------------------------------------------------------------

Mistake 4
---------
Forgetting to update current.

Without

self.current += self.step

the iterator loops forever.
"""

# ==============================================================================
# QUICK SUMMARY
# ==============================================================================

"""
• StepRange behaves similarly to Python's built-in range().

• __iter__() returns the iterator object.

• __next__() returns one value at a time.

• StopIteration ends the iteration.

• Positive and negative step sizes require different stopping conditions.

• The iterator generates values lazily, making it memory efficient.
"""
