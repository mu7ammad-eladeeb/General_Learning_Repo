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
