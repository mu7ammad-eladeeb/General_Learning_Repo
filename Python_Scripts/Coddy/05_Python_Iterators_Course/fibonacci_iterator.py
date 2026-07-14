"""
Challenge: Fibonacci Iterator (Easy)

Description:
Create a FibonacciIterator class that generates Fibonacci numbers up to a specified limit. 
The class should implement the iterator protocol and have the following methods:
- __init__(self, limit): Initialize the iterator with a limit.
- __iter__(self): Return the iterator object itself.
- __next__(self): Generate the next Fibonacci number or raise StopIteration when the limit is reached.

After implementing the FibonacciIterator class, create an instance of it using the input value as the limit. 
Then, iterate through the Fibonacci numbers and print each number on a new line until the StopIteration exception is raised.

Input:
An integer representing the upper limit for the Fibonacci sequence.
"""

# Step 1: Read the upper limit integer from standard input
limit = int(input())

# Step 2: Define the iterator class that implements the custom sequence logic
class FibonacciIterator:
    def __init__(self, limit):
        # Step 3: Initialize state variables with the limit and initial sequence values
        self.limit = limit
        self.previous = 0
        self.current = 1

    def __iter__(self):
        # Step 4: Return the iterator object itself to support the iteration protocol
        return self

    def __next__(self):
        # Step 5: Terminate the iteration with a StopIteration exception if the sequence exceeds the limit
        if self.previous > self.limit:
            raise StopIteration
        
        # Step 6: Store current state, update sequence calculation, and return the current number
        result = self.previous
        self.previous, self.current = self.current, self.previous + self.current
        return result

# Step 7: Instantiate the FibonacciIterator with the user-provided limit
fib_iterator = FibonacciIterator(limit)

# Step 8: Loop through the iterator and print each Fibonacci number sequentially
for fib_number in fib_iterator:
    print(fib_number)
