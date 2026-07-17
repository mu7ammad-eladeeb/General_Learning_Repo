# Filtered Iterator Challenge
# Medium
# Create a PrimeNumberFilter class that implements a filtered iterator to generate prime numbers up to a specified limit.

# Read input
limit = int(input())

class PrimeNumberFilter:
    def __init__(self, limit):
        # Sets the upper bound for prime generation and initializes the starting number to 2.
        self.limit = limit
        self.current = 2

    def __iter__(self):
        # Makes the class compatible with the iterator protocol.
        return self

    def __next__(self):
        # Iterates through numbers up to the limit, calling is_prime to verify each one;
        # it returns the next prime or signals the end of iteration via StopIteration.
        while self.current <= self.limit:
            if self.is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration

    def is_prime(self, n):
        # Determines primality by checking if n is divisible by any integer from 2 up to the square root of n.
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Create an instance of PrimeNumberFilter using the input value as the upper limit.
prime_filter = PrimeNumberFilter(limit)

# Iterate through the prime numbers and print each number on a new line until the StopIteration exception is raised.
try:
    for prime in prime_filter:
        print(prime)
except StopIteration:
    pass
