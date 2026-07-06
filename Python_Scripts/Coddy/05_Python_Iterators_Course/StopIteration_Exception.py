# Challenge: Prime Number Iterator (Difficulty: Easy)

## Problem Statement

Create a custom iterator (custom iterator = an iterator you build yourself, not a built-in one) that generates a sequence of prime numbers (prime number = a number greater than 1 divisible only by 1 and itself) up to a given limit. The iterator should use the `StopIteration` exception to signal the end of the sequence when it reaches or exceeds the limit.

**Input:** An integer `limit` (provided as a string representing an integer).

**Requirements:**
- Generate prime numbers starting from 2.
- Raise a `StopIteration` exception when the next prime number would exceed the given limit.
- Implement the iterator as a class with `__iter__()` and `__next__()` methods (dunder methods = "double underscore" methods that let a class plug into Python's built-in behaviors, like iteration).
- Print each generated prime number on a new line.

## Solution

```python
# Read input
limit = int(input())

class PrimeIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        while self.current <= self.limit:
            if is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        
        raise StopIteration

# Create an instance of PrimeIterator
prime_iter = PrimeIterator(limit)

# Iterate through the prime numbers and print each one
try:
    for prime in prime_iter:
        print(prime)
except StopIteration:
    pass  # End of iteration
```

## Explanation of the Solution

1. **`__init__(self, limit)`** (constructor = the method that runs automatically when an object is created): Stores the `limit` and sets `self.current = 2`, since 2 is the first prime number and the starting point of the search.

2. **`__iter__(self)`**: Returns `self`, which is what makes this class officially "iterable" (iterable = an object capable of being looped over) — Python calls this once at the start of a `for` loop to get the iterator object.

3. **`__next__(self)`**: This is the core logic (core logic = the main working part of the code), called once per loop iteration:
   - It defines a nested helper function (nested function = a function defined inside another function) `is_prime(n)` that checks divisibility (divisibility = whether one number divides evenly into another) from 2 up to the square root of `n` — a common optimization (optimization = a way to make code run faster/more efficiently), since a factor larger than the square root would always pair with one smaller than it.
   - It then loops through numbers starting at `self.current`, testing each with `is_prime()`.
   - If a prime is found, it's returned immediately, and `self.current` is advanced by 1 for the next call.
   - If `self.current` exceeds `self.limit` without finding a prime, the loop ends and `raise StopIteration` is triggered, telling Python (and the `for` loop) that iteration is complete.

4. **The `try/except` block at the bottom**: Technically redundant here (redundant = unnecessary because it duplicates existing protection), since a `for` loop already catches `StopIteration` automatically. It's included mainly for clarity/demonstration purposes.

**Key takeaway:** This challenge demonstrates the full iterator protocol in practice — pairing state tracking (`self.current`) with a manual `StopIteration` raise, rather than relying on Python's automatic version (like the one seen with `iter()` on a list).
