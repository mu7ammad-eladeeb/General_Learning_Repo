# Python Iterators: A Comprehensive Guide

This repository covers the core concepts of Python iterators, how they differ from iterables, how to use built-in iteration functions, and how to build custom iterators.

---

## What are Iterators?

Iterators are a fundamental concept in Python that allow you to traverse through a collection of elements, one at a time. They provide a way to access the elements of a container object sequentially without needing to know the underlying structure of the container.

An **iterator** in Python is an object that implements the **Iterator Protocol**, which consists of two special methods:
* `__iter__()`: Returns the iterator object itself.
* `__next__()`: Returns the next value in the iteration. If there are no more elements, it raises a `StopIteration` exception.

When you use a `for` loop in Python, the interpreter automatically manages an iterator behind the scenes.

---

## Iterable vs Iterator

It is crucial to understand the distinction between an iterable and an iterator:

| Feature | Iterable | Iterator |
| :--- | :--- | :--- |
| **Definition** | An object capable of returning its elements one at a time. | An object representing a stream of data. |
| **Methods** | Implements the `__iter__()` method. | Implements both `__iter__()` and `__next__()` methods. |
| **Examples** | lists, tuples, strings, dictionaries. | Created from an iterable using the `iter()` function. |

---

## Coding Challenge: Even Number Iterator

### Problem Statement
Create an iterator that generates a sequence of even numbers up to a given limit.
* Generate even numbers starting from 2.
* Stop when it reaches or exceeds the given limit.
* Print each generated even number on a new line.

### How to Run the Solution
The solution code is provided in the `even_iterator.py` file. Run it using:
```bash
python even_iterator.py
```
## StopIteration Exception

The `StopIteration` exception is a crucial component (an essential, built-in part) in Python's iterator protocol (protocol = the set of rules an object must follow). It signals the end of an iteration sequence and plays a vital role in controlling iterator behavior.

### What is StopIteration?

`StopIteration` is a built-in exception (exception = an error-like signal Python raises during execution) in Python that is raised when an iterator is exhausted (exhausted = has no more items left to give), meaning there are no more items to be returned.

### When is StopIteration Raised?

The `StopIteration` exception is automatically raised by Python in two main scenarios:

1. When the `next()` function is called on an iterator that has no more items.
2. When a custom iterator's `__next__()` method is implemented (implemented = written/coded) to raise `StopIteration` at the end of the iteration.

### Example of StopIteration

```python
my_list = [1, 2, 3]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Raises StopIteration
```

In this example, after we've iterated through all elements of `my_list`, the next call to `next()` raises a `StopIteration` exception.

### Importance in Iterator Behavior

The `StopIteration` exception is crucial for several reasons:

1. **Signaling the End**: It provides a clear signal that the iteration has reached its end.
2. **For Loop Termination** (termination = stopping point): Python's `for` loops rely on `StopIteration` to know when to terminate.
3. **Custom Iterator Control**: When creating custom iterators, raising `StopIteration` allows you to define when the iteration should end.

### Handling StopIteration

While `for` loops handle `StopIteration` automatically, when using `next()` directly, you might want to handle this exception explicitly (explicitly = directly and clearly stated, not left implied):

```python
my_iterator = iter([1, 2, 3])

try:
    while True:
        item = next(my_iterator)
        print(item)
except StopIteration:
    print("Iteration finished")
```

This code will print the numbers 1, 2, and 3, followed by "Iteration finished" when the `StopIteration` exception is caught (caught = intercepted and handled instead of crashing the program).

Understanding the `StopIteration` exception is essential for working with iterators in Python, as it provides the mechanism (mechanism = the internal method/system by which something works) for controlling and ending iterations in a standardized (standardized = following one consistent, agreed-upon way) way.

# Implementing `__iter__()` in Python

> **Source:** Python Iterator Protocol Notes

---

# 📖 Overview

Creating a custom iterator in Python involves implementing the `__iter__()` method in a class.

This method is a crucial part of the **iterator protocol** and defines how a custom object behaves as an iterator.

---

# 🔹 The `__iter__()` Method

The `__iter__()` method has **two main purposes**:

1. Makes an object **iterable**.
2. Returns the **iterator object** itself.

---

## Basic Structure

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
```

---

# 🛠️ How to Implement `__iter__()`

To implement `__iter__()` in your custom class:

1. Define the `__iter__()` method inside your class.
2. Return the iterator object itself (usually `self`).

---

# 💻 Complete Example

```python
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # Return the iterator object (self)
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# Using the custom iterator
countdown = CountDown(5)

for num in countdown:
    print(num)
```

---

## Expected Output

```text
5
4
3
2
1
```

---

# ⚙️ Step-by-Step Execution

When the code runs:

1. A `CountDown` object is created with the value `5`.
2. The `for` loop automatically calls:

```python
iter(countdown)
```

3. Python executes:

```python
countdown.__iter__()
```

4. Since `__iter__()` returns `self`, the object becomes its own iterator.

5. The `for` loop repeatedly calls:

```python
countdown.__next__()
```

6. Each call returns:

```
5
4
3
2
1
```

7. When `start` reaches `0`, `__next__()` raises:

```python
StopIteration
```

which tells the `for` loop that iteration is finished.

---

# 🔑 Key Points

- `__iter__()` is called whenever:
  - `iter(object)` is used.
  - The object is used in a `for` loop.

- Returning `self` from `__iter__()` is common when the class implements **both**:
  - `__iter__()`
  - `__next__()`

- If a class **only** implements `__iter__()`, it should return a **different iterator object** that implements `__next__()`.

- By implementing `__iter__()`, your custom objects become compatible with:
  - `for` loops
  - `iter()`
  - Iterator-based functions
  - Python's iterator protocol

---

# 📋 Quick Summary

| Concept | Description |
|----------|-------------|
| `__iter__()` | Makes an object iterable and returns an iterator. |
| `__next__()` | Returns the next value in the sequence. |
| `iter(obj)` | Calls `obj.__iter__()`. |
| `StopIteration` | Signals that there are no more values. |
| Returning `self` | Used when the object is both the iterable and the iterator. |

---

# 🧠 Memory Tips

### Think of it this way:

- **`__iter__()`** → "Start iterating."
- **`__next__()`** → "Give me the next item."

A `for` loop automatically calls **both** methods behind the scenes.

---

# 💡 Important Note

A class can be:

1. **Both an iterable and an iterator**
   - Implements both `__iter__()` and `__next__()`.
   - `__iter__()` returns `self`.

2. **Only an iterable**
   - Implements `__iter__()`.
   - Returns a separate iterator object that implements `__next__()`.

This distinction is an important part of Python's iterator protocol.

# Implementing `__next__()` in Python

> **Source:** Python Iterator Protocol Notes

---

# 📖 CONCEPT OVERVIEW

The `__next__()` method is a crucial part of creating custom iterators in Python. It defines how to retrieve the next item in the iteration sequence.

When implementing `__next__()`, you control the behavior of your iterator, determining what values it produces and when it should stop.

---

# 🎯 Purpose of `__next__()`

The `__next__()` method serves **two main purposes**:

1. Return the next item in the sequence.
2. Raise a `StopIteration` exception when there are no more items.

---

# 🛠️ Implementing `__next__()`

Here is the basic structure for implementing `__next__()`:

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        result = self.data[self.index]
        self.index += 1
        return result
```

---

# 🔑 Key Aspects of `__next__()`

## 1. State Management

Keep track of the current state of iteration (for example, using an index).

## 2. Return Next Item

Determine and return the next item in the sequence.

## 3. StopIteration

Raise `StopIteration` when there are no more items.

## 4. Side Effects

Update any necessary internal state for the next iteration.

---

# 💻 Example: Custom Range Iterator

Here's an example of a custom iterator that mimics a simplified version of Python's `range()`:

```python
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current
        self.current += 1
        return result

# Using the custom range iterator
for num in CustomRange(1, 5):
    print(num)
```

## Expected Output

```text
1
2
3
4
```

---

# 📝 Explanation of the Example

In this example:

- `__next__()` returns the current number.
- It increments the number for the next iteration.
- When it reaches the ending value, it raises `StopIteration`.
- The exception tells the `for` loop that there are no more values to iterate over.

---

# ⚙️ Step-by-Step Execution

1. `CustomRange(1, 5)` creates a new iterator.
2. The `for` loop automatically calls:

```python
iter(custom_range)
```

which invokes:

```python
custom_range.__iter__()
```

3. Since `__iter__()` returns `self`, the object acts as its own iterator.

4. The `for` loop repeatedly calls:

```python
custom_range.__next__()
```

5. Each call:

- Checks whether the end has been reached.
- Returns the current value.
- Increments the current value.

6. Once `current >= end`, Python raises:

```python
StopIteration
```

7. The `for` loop ends automatically.

---

# 📌 Original Conclusion

By implementing `__next__()`, you define the core behavior of your iterator, allowing it to work seamlessly with Python's iteration mechanisms like `for` loops and the `next()` function.

---

# 📋 Quick Summary

| Concept | Description |
|---------|-------------|
| `__next__()` | Returns the next item in the iterator. |
| `StopIteration` | Signals that there are no more items. |
| State Management | Keeps track of the iterator's current position. |
| Return Next Item | Produces the next value. |
| Side Effects | Updates internal state for future iterations. |
| `iter(obj)` | Calls `obj.__iter__()`. |
| `next(obj)` | Calls `obj.__next__()`. |

---

# 🧠 Memory Tips

- `__iter__()` → "Start iterating."
- `__next__()` → "Give me the next item."
- `StopIteration` → "Iteration is finished."

A `for` loop automatically calls `__iter__()` once and `__next__()` repeatedly until `StopIteration` is raised.

---

# ✅ Complete Checklist

This document preserves:

- Every concept from the original lesson.
- Every purpose.
- Every key aspect.
- The complete code example.
- The expected output.
- The original concluding explanation.

It also adds:

- Better organization.
- Step-by-step execution.
- Summary table.
- Memory tips.

# Infinite Iterators in Python

## What Are Infinite Iterators?

**Infinite iterators** are a special type of iterator in Python that can potentially generate an endless sequence of values.

Unlike **finite iterators**, which eventually raise a `StopIteration` exception when all values have been produced, infinite iterators continue generating values indefinitely.

Infinite iterators are useful when a program needs a continuous stream of data without a predefined endpoint.

---

# Characteristics of Infinite Iterators

Infinite iterators have several defining characteristics:

- They **never raise a `StopIteration` exception**.
- They continuously generate values without ending.
- They are useful for generating continuous sequences or simulating endless streams of data.
- They must be used carefully to avoid creating infinite loops.

Because they never stop automatically, programmers usually include a condition that explicitly ends the loop.

---

# Creating an Infinite Iterator

An infinite iterator can be created by implementing Python's iterator protocol.

The iterator must define:

- `__iter__()` — returns the iterator object itself.
- `__next__()` — returns the next value each time it is called.

Unlike a finite iterator, `__next__()` never raises `StopIteration`.

## Example

```python
class InfiniteCounter:
    def __init__(self, start=0):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        current = self.count
        self.count += 1
        return current

# Usage
counter = InfiniteCounter()

for i in counter:
    print(i)
    if i >= 5:
        break  # Prevent infinite loop
```

### Output

```text
0
1
2
3
4
5
```

---

# How the Example Works

When the object is created:

```python
counter = InfiniteCounter()
```

the constructor initializes:

```python
self.count = 0
```

The `for` loop begins by calling:

```python
iter(counter)
```

which executes:

```python
__iter__()
```

This method simply returns the iterator itself:

```python
return self
```

Next, the loop repeatedly calls:

```python
next(counter)
```

Each call to `__next__()` performs the following steps:

1. Stores the current value.
2. Increments the counter.
3. Returns the stored value.

For example:

First call:

```python
current = 0
self.count = 1
return 0
```

Second call:

```python
current = 1
self.count = 2
return 1
```

Third call:

```python
current = 2
self.count = 3
return 2
```

This process continues forever because `__next__()` never raises `StopIteration`.

The loop only stops because of:

```python
if i >= 5:
    break
```

Without this `break` statement, the program would continue printing numbers indefinitely.

---

# Why Doesn't an Infinite Iterator Stop?

A normal iterator eventually executes something similar to:

```python
raise StopIteration
```

An infinite iterator never reaches this point.

Instead, it always computes and returns another value.

For example:

```python
def __next__(self):
    current = self.count
    self.count += 1
    return current
```

Every call to `next()` produces another number, allowing the iterator to continue forever.

---

# Built-in Infinite Iterators

Python's `itertools` module provides several ready-made infinite iterators.

---

## `itertools.count()`

Creates an iterator that counts upward forever.

### Syntax

```python
itertools.count(start=0, step=1)
```

### Parameters

- **start** — The value where counting begins.
- **step** — The amount added after each iteration.

### Example

```python
from itertools import count

for i in count(10):
    print(i)
    if i >= 15:
        break
```

### Output

```text
10
11
12
13
14
15
```

### Explanation

The iterator begins at **10**.

Each iteration increases the value by **1**.

Without the `break` statement, the output would continue forever:

```text
10
11
12
13
14
15
16
17
18
...
```

---

## `itertools.cycle()`

Cycles through an iterable indefinitely.

### Syntax

```python
itertools.cycle(iterable)
```

### Example

```python
from itertools import cycle

colors = cycle(["Red", "Green", "Blue"])

for i, color in enumerate(colors):
    print(color)

    if i == 8:
        break
```

### Output

```text
Red
Green
Blue
Red
Green
Blue
Red
Green
Blue
```

### Explanation

After reaching the last element:

```text
Blue
```

the iterator automatically starts again from the beginning:

```text
Red
```

This process repeats indefinitely.

---

## `itertools.repeat()`

Repeats the same element indefinitely or a specified number of times.

### Syntax

```python
itertools.repeat(element)
```

or

```python
itertools.repeat(element, n)
```

### Example (Infinite)

```python
from itertools import repeat

for i, value in enumerate(repeat("Python")):
    print(value)

    if i == 4:
        break
```

### Output

```text
Python
Python
Python
Python
Python
```

### Example (Finite)

```python
from itertools import repeat

for value in repeat("Python", 3):
    print(value)
```

### Output

```text
Python
Python
Python
```

### Explanation

If the second argument (`n`) is omitted, the iterator repeats the element forever.

If `n` is provided, the element is repeated exactly `n` times.

---

# Common Uses of Infinite Iterators

Infinite iterators are useful in situations where data needs to be generated continuously.

Examples include:

- Generating sequential IDs.
- Producing timestamps.
- Simulating sensor readings.
- Cycling through playlists.
- Creating endless game loops.
- Repeating animations.
- Processing streaming data.
- Continuously generating values for testing.

---

# Potential Problems

Since infinite iterators never stop automatically, they can easily create unintended infinite loops.

For example:

```python
counter = InfiniteCounter()

for number in counter:
    print(number)
```

This program will never terminate because the iterator never raises `StopIteration`.

The output continues indefinitely:

```text
0
1
2
3
4
5
6
7
8
9
...
```

---

# Cautions and Best Practices

When working with infinite iterators:

- Always include a stopping condition when iterating over them.
- Use `break` statements whenever appropriate.
- Avoid accidentally creating infinite loops.
- Use infinite iterators only when an endless sequence is actually required.
- Consider using **generator functions** for creating memory-efficient infinite sequences.

Following these practices ensures that your program remains responsive and behaves as expected.

---

# Summary

Infinite iterators are iterators that never end because they never raise the `StopIteration` exception. They continuously generate values, making them ideal for applications that require endless data streams or repeating sequences.

Python's `itertools` module provides three commonly used infinite iterators:

- `itertools.count()` — Counts upward indefinitely.
- `itertools.cycle()` — Repeats an iterable forever.
- `itertools.repeat()` — Repeats a single element indefinitely or a specified number of times.

Although powerful, infinite iterators should always be used with care. Always include a mechanism—such as a `break` statement or another stopping condition—to prevent unintended infinite loops.

# Built-in Iterator Functions in Python

## Introduction

Python provides several built-in functions that work with iterators, making it easier to manipulate and process iterable data. These functions help write cleaner, more readable, and more Pythonic code.

In this guide, we will explore three commonly used iterator-related functions:

- `enumerate()`
- `zip()`
- `reversed()`

---

# 1. `enumerate()`

## What is `enumerate()`?

The `enumerate()` function adds a counter to an iterable and returns an **enumerate object** (an iterator). It is useful whenever you need both the index and the value while iterating.

## Syntax

```python
enumerate(iterable, start=0)
```

### Parameters

- **iterable** – Any iterable object.
- **start** *(optional)* – Starting index (default: `0`).

## Example

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### Output

```text
0: apple
1: banana
2: cherry
```

### Starting from a Different Index

```python
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Output:

```text
1 apple
2 banana
3 cherry
```

### Common Uses

- Numbering items
- Displaying menus
- Tracking positions
- Avoiding manual index variables

---

# 2. `zip()`

## What is `zip()`?

The `zip()` function combines two or more iterables into an iterator of tuples.

## Syntax

```python
zip(iterable1, iterable2, ...)
```

## Example

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### Output

```text
Alice is 25 years old
Bob is 30 years old
Charlie is 35 years old
```

### Different Length Iterables

```python
letters = ['A', 'B', 'C']
numbers = [1, 2]

for pair in zip(letters, numbers):
    print(pair)
```

Output:

```text
('A', 1)
('B', 2)
```

### Combining More Than Two Iterables

```python
names = ["Alice", "Bob"]
ages = [25, 30]
countries = ["USA", "Canada"]

for name, age, country in zip(names, ages, countries):
    print(name, age, country)
```

### Creating a Dictionary

```python
people = dict(zip(names, ages))
print(people)
```

Output:

```python
{'Alice': 25, 'Bob': 30}
```

---

# 3. `reversed()`

## What is `reversed()`?

The `reversed()` function returns a reverse iterator that accesses a sequence from the last element to the first without copying it.

## Syntax

```python
reversed(sequence)
```

## Example

```python
numbers = [1, 2, 3, 4, 5]

for num in reversed(numbers):
    print(num)
```

### Output

```text
5
4
3
2
1
```

### Converting to a List

```python
print(list(reversed(numbers)))
```

Output:

```text
[5, 4, 3, 2, 1]
```

### Reversing a String

```python
text = "Python"
print("".join(reversed(text)))
```

Output:

```text
nohtyP
```

---

# Summary

Python provides three commonly used built-in iterator functions:

- **`enumerate()`** adds an index while iterating.
- **`zip()`** combines multiple iterables into tuples.
- **`reversed()`** iterates through a sequence in reverse order.

These functions simplify iteration, improve readability, and are widely used in Python programming.

# Itertools Module in Python

## Introduction

The **`itertools`** module is a built-in Python module that provides a collection of **fast**, **memory-efficient**, and **powerful** tools for working with iterators.

Instead of storing all values in memory at once, most `itertools` functions generate values **lazily** (one at a time). This makes them ideal for working with large datasets, infinite sequences, and complex iteration tasks.

The module contains functions for:

- Creating infinite iterators
- Combining multiple iterables
- Slicing iterators
- Generating Cartesian products
- Creating permutations and combinations
- Many other iterator-based operations

To use the module:

```python
import itertools
```

---

# Why Use `itertools`?

The `itertools` module offers many advantages:

- Faster than many manual implementations.
- Uses less memory because it generates values only when needed.
- Produces cleaner and shorter code.
- Eliminates the need to write many custom loops.
- Highly optimized because it is implemented in C.

---

# Categories of Functions

The functions in `itertools` are divided into three major groups:

1. Infinite Iterators
2. Iterators Terminating on the Shortest Input Sequence
3. Combinatoric Iterators

---

# 1. Infinite Iterators

Infinite iterators continue generating values forever unless you explicitly stop them.

These include:

- `count()`
- `cycle()`
- `repeat()`

---

## `itertools.count()`

### Purpose

`count()` creates an iterator that continuously counts upward (or downward if using a negative step).

It never stops unless your program stops it.

### Syntax

```python
itertools.count(start=0, step=1)
```

### Parameters

- **start** — The first value.
- **step** — The amount added after each iteration.

### Example

```python
import itertools

for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)
```

### Output

```text
10
12
14
16
18
20
```

### How It Works

The iterator starts at:

```text
10
```

Every iteration adds:

```text
2
```

Sequence:

```text
10
↓
12
↓
14
↓
16
↓
18
↓
20
↓
22
...
```

Since the program contains:

```python
if i > 20:
    break
```

the loop ends before printing 22.

### Common Uses

- Number generators
- Infinite counters
- ID generation
- Time simulations

---

## `itertools.cycle()`

### Purpose

`cycle()` repeatedly loops over an iterable forever.

Once it reaches the last element, it automatically starts again from the beginning.

### Syntax

```python
itertools.cycle(iterable)
```

### Example

```python
import itertools

colors = itertools.cycle(["red", "green", "blue"])

for _ in range(6):
    print(next(colors))
```

### Output

```text
red
green
blue
red
green
blue
```

### How It Works

The iterator remembers every item.

It cycles through them repeatedly:

```text
red
↓
green
↓
blue
↓
red
↓
green
↓
blue
...
```

It never raises `StopIteration`.

### Common Uses

- Rotating turns in games
- Infinite playlists
- Round-robin scheduling
- Repeating patterns

---

## `itertools.repeat()`

### Purpose

`repeat()` repeatedly returns the same object.

It can repeat:

- Forever
- A specified number of times

### Syntax

```python
itertools.repeat(element)
```

or

```python
itertools.repeat(element, times)
```

### Example

```python
import itertools

for word in itertools.repeat("Python", 3):
    print(word)
```

### Output

```text
Python
Python
Python
```

### Infinite Example

```python
import itertools

iterator = itertools.repeat("Hello")

for _ in range(5):
    print(next(iterator))
```

Output

```text
Hello
Hello
Hello
Hello
Hello
```

Without limiting the loop, it would continue forever.

### Common Uses

- Filling data
- Supplying constant arguments
- Creating repeated values

---

# 2. Iterators Terminating on the Shortest Input Sequence

Unlike infinite iterators, these eventually stop.

They generally terminate when one or more input iterables become exhausted.

These include:

- `chain()`
- `islice()`
- `zip_longest()`

---

## `itertools.chain()`

### Purpose

`chain()` combines multiple iterables into one continuous iterator.

Instead of nested loops, everything behaves like a single sequence.

### Syntax

```python
itertools.chain(*iterables)
```

### Example

```python
import itertools

numbers = itertools.chain(
    [1, 2, 3],
    [4, 5, 6]
)

print(list(numbers))
```

### Output

```text
[1, 2, 3, 4, 5, 6]
```

### How It Works

Instead of:

```text
List 1

1
2
3

List 2

4
5
6
```

`chain()` presents them as one iterator:

```text
1
2
3
4
5
6
```

### Common Uses

- Joining multiple datasets
- Reading several files
- Combining lists
- Combining generators

---

## `itertools.islice()`

### Purpose

`islice()` extracts selected elements from an iterator without converting it into a list.

It behaves similarly to list slicing.

### Syntax

```python
itertools.islice(iterable, start, stop[, step])
```

### Parameters

- **iterable**
- **start**
- **stop**
- **step** (optional)

### Example

```python
import itertools

numbers = itertools.count()

print(list(itertools.islice(numbers, 5, 10)))
```

### Output

```text
[5, 6, 7, 8, 9]
```

### How It Works

`count()` generates:

```text
0
1
2
3
4
5
6
7
8
9
10
...
```

`islice(numbers, 5, 10)` skips:

```text
0
1
2
3
4
```

and returns:

```text
5
6
7
8
9
```

### Common Uses

- Reading part of an iterator
- Sampling data
- Pagination

---

## `itertools.zip_longest()`

### Purpose

`zip_longest()` works like Python's `zip()`, but it continues until the **longest iterable** is exhausted.

Missing values are replaced with a fill value.

### Syntax

```python
itertools.zip_longest(*iterables, fillvalue=None)
```

### Example

```python
import itertools

letters = ["A", "B"]
numbers = [1, 2, 3]

result = itertools.zip_longest(
    letters,
    numbers,
    fillvalue="-"
)

print(list(result))
```

### Output

```text
[
    ('A', 1),
    ('B', 2),
    ('-', 3)
]
```

### How It Works

Normal `zip()` would produce:

```text
('A',1)
('B',2)
```

because it stops when the shortest iterable ends.

`zip_longest()` continues:

```text
('A',1)
('B',2)
('-',3)
```

### Common Uses

- Merging unequal datasets
- Comparing sequences
- Handling missing values

---

# 3. Combinatoric Iterators

These functions generate mathematical arrangements of data.

They include:

- `product()`
- `permutations()`
- `combinations()`

---

## `itertools.product()`

### Purpose

Produces the **Cartesian product** of multiple iterables.

Every element from one iterable is paired with every element from another.

### Syntax

```python
itertools.product(*iterables, repeat=1)
```

### Example

```python
import itertools

print(list(itertools.product([1,2],["A","B"])))
```

### Output

```text
[
(1,'A'),
(1,'B'),
(2,'A'),
(2,'B')
]
```

### How It Works

```
1 pairs with A
1 pairs with B
2 pairs with A
2 pairs with B
```

Every possible pairing is generated.

### Common Uses

- Grid generation
- Password brute force
- Game combinations
- Mathematical products

---

## `itertools.permutations()`

### Purpose

Generates every possible **ordered arrangement**.

Order matters.

### Syntax

```python
itertools.permutations(iterable, r=None)
```

### Example

```python
import itertools

letters = "ABC"

print(list(itertools.permutations(letters,2)))
```

### Output

```text
[
('A','B'),
('A','C'),
('B','A'),
('B','C'),
('C','A'),
('C','B')
]
```

### How It Works

```
AB

BA
```

are considered different because order changes.

### Common Uses

- Arranging objects
- Scheduling
- Password generation
- Search algorithms

---

## `itertools.combinations()`

### Purpose

Generates every possible selection of elements.

Unlike permutations, **order does not matter**.

### Syntax

```python
itertools.combinations(iterable,r)
```

### Example

```python
import itertools

letters = "ABCD"

print(list(itertools.combinations(letters,2)))
```

### Output

```text
[
('A','B'),
('A','C'),
('A','D'),
('B','C'),
('B','D'),
('C','D')
]
```

### How It Works

```
AB
```

and

```
BA
```

are treated as the same combination.

Therefore only one appears.

### Common Uses

- Team selection
- Lottery numbers
- Choosing subsets
- Statistical sampling

---

# Complete Example

```python
import itertools

# count()
for i in itertools.count(10,2):
    if i > 20:
        break
    print(i)

# cycle()
colors = itertools.cycle(["red","green","blue"])

for _ in range(6):
    print(next(colors))

# chain()
numbers = itertools.chain([1,2,3],[4,5,6])
print(list(numbers))

# combinations()
letters = "ABCD"
print(list(itertools.combinations(letters,2)))
```

---

# Advantages of `itertools`

- Built into Python
- Very fast
- Memory efficient
- Produces values lazily
- Simplifies complex loops
- Excellent for data processing
- Commonly used in data science and competitive programming

---

# Summary

The **`itertools`** module provides efficient tools for working with iterators.

Its functions are divided into three categories:

## Infinite Iterators

- `count()` → Infinite counting
- `cycle()` → Infinite repetition of an iterable
- `repeat()` → Infinite or fixed repetition of one object

## Iterators Terminating on the Shortest Input Sequence

- `chain()` → Joins multiple iterables
- `islice()` → Slices iterators
- `zip_longest()` → Combines iterables until the longest one finishes

## Combinatoric Iterators

- `product()` → Cartesian product
- `permutations()` → Ordered arrangements
- `combinations()` → Unordered selections

Using these tools allows you to write cleaner, faster, and more memory-efficient Python code while avoiding unnecessary loops and temporary lists.

# Generator Expressions in Python

## Introduction

**Generator expressions** are a concise way to create **iterators** in Python. They provide a **memory-efficient** alternative to list comprehensions because they generate values **one at a time** instead of creating an entire list in memory.

Generator expressions are especially useful when working with:

- Large datasets
- Infinite sequences
- Streams of data
- Data processing pipelines

---

# Syntax of Generator Expressions

A generator expression has a syntax very similar to a list comprehension.

The only difference is that it uses **parentheses `()`** instead of **square brackets `[]`**.

## Syntax

```python
(expression for item in iterable if condition)
```

### Components

- **expression** – The value to generate.
- **item** – The current element from the iterable.
- **iterable** – Any iterable object (such as a list, tuple, string, or range).
- **if condition** *(optional)* – Filters which elements are generated.

---

# How Generator Expressions Work

Unlike list comprehensions, generator expressions **do not calculate every value immediately**.

Instead, they generate values **only when they are requested**.

This process is called **lazy evaluation**.

For example:

```python
numbers = (x for x in range(5))
```

At this point, **no numbers have been generated yet**.

The values are produced only when you iterate over the generator.

---

# Example Usage

Suppose you want to generate square numbers.

```python
squares = (x ** 2 for x in range(5))

for square in squares:
    print(square)
```

### Output

```text
0
1
4
9
16
```

### Explanation

The generator expression

```python
(x ** 2 for x in range(5))
```

does not immediately calculate all five square numbers.

Instead, each iteration performs the following steps:

```
x = 0 → 0² = 0

↓

x = 1 → 1² = 1

↓

x = 2 → 2² = 4

↓

x = 3 → 3² = 9

↓

x = 4 → 4² = 16
```

Each value is produced only when the `for` loop requests it.

---

# Lazy Evaluation

One of the most important characteristics of generator expressions is **lazy evaluation**.

Lazy evaluation means:

- Values are generated one at a time.
- Nothing is computed until it is needed.
- Memory usage stays low.

Example:

```python
generator = (x for x in range(1000000))
```

Although the range contains one million numbers, Python does **not** store one million values in memory.

Instead, only one value exists at any given time.

---

# Single-Use Iterators

A generator expression creates a **generator object**, which is an iterator.

Like all iterators, it can only be used once.

Example

```python
numbers = (x for x in range(5))

for num in numbers:
    print(num)

print("Again:")

for num in numbers:
    print(num)
```

### Output

```text
0
1
2
3
4

Again:
```

Nothing is printed the second time.

### Why?

The generator has already produced all of its values.

Once exhausted, it raises `StopIteration`.

To iterate again, you must create a new generator.

```python
numbers = (x for x in range(5))
```

---

# Concise Syntax

Generator expressions provide a compact alternative to writing generator functions.

Instead of writing several lines of code, a generator expression can often accomplish the same task in a single line.

Example

```python
(x * 2 for x in range(10))
```

This creates a generator that produces doubled numbers.

---

# Comparison with List Comprehensions

Generator expressions look almost identical to list comprehensions.

## List Comprehension

```python
squares_list = [x ** 2 for x in range(1000000)]
```

This creates **one million values immediately**.

The entire list is stored in memory.

Memory usage:

```
High
```

---

## Generator Expression

```python
squares_gen = (x ** 2 for x in range(1000000))
```

This creates only a generator object.

Values are produced one at a time.

Memory usage:

```
Very Low
```

---

# List Comprehension vs Generator Expression

## List Comprehension

```python
numbers = [x for x in range(5)]
```

Immediately creates

```python
[0, 1, 2, 3, 4]
```

Everything already exists in memory.

---

## Generator Expression

```python
numbers = (x for x in range(5))
```

Initially

```
Generator Object
```

The values are generated only when requested.

---

# Memory Efficiency

Consider

```python
range(1000000)
```

A list comprehension creates

```
1,000,000 integers
```

and stores all of them in memory.

A generator expression creates

```
One integer

↓

Next integer

↓

Next integer

↓

...
```

Only one value exists at a time.

This makes generator expressions ideal for processing large amounts of data.

---

# Using next()

Since a generator is an iterator, it can be used with `next()`.

Example

```python
numbers = (x for x in range(5))

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

### Output

```text
0
1
2
```

Each call to `next()` requests the next value.

---

# Generator Exhaustion

Eventually, every generator runs out of values.

Example

```python
numbers = (x for x in range(2))

print(next(numbers))
print(next(numbers))
print(next(numbers))
```

The final call raises

```python
StopIteration
```

because there are no more values.

---

# Filtering Values

Generator expressions can include conditions.

Example

```python
even_numbers = (
    x
    for x in range(10)
    if x % 2 == 0
)

for number in even_numbers:
    print(number)
```

### Output

```text
0
2
4
6
8
```

The condition

```python
if x % 2 == 0
```

filters out odd numbers.

---

# Use Cases

Generator expressions are especially useful when:

- Working with large datasets.
- Reading large files.
- Processing streams of data.
- Creating data-processing pipelines.
- Performing calculations without storing intermediate results.
- Saving memory.

---

# Advantages

Generator expressions provide several benefits:

- Memory efficient.
- Fast startup because values are generated only when needed.
- Cleaner and shorter code.
- Easy to combine with iterator functions.
- Ideal for large collections of data.

---

# Limitations

Generator expressions also have some limitations:

- They can only be iterated once.
- They do not support indexing.

For example,

```python
generator = (x for x in range(5))

generator[0]
```

raises an error because generators are not sequences.

---

# Summary

Generator expressions provide a concise and memory-efficient way to create iterators in Python.

Their syntax is

```python
(expression for item in iterable if condition)
```

Key characteristics include:

- Lazy evaluation
- Memory efficiency
- Single-use iterators
- Concise syntax

Compared with list comprehensions, generator expressions do **not** store all values in memory at once. Instead, they generate values only when requested, making them an excellent choice for processing large datasets and building efficient data pipelines.
