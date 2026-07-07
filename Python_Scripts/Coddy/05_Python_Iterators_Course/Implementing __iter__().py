# ==============================================================================
# Topic: Implementing __iter__() in Python
# Source: Coddy Course
# Description:
# Complete notes covering the __iter__() method, the iterator protocol,
# a CountDown iterator example, and two complete solutions for the
# AlphabetIterator challenge.
# ==============================================================================

"""
📖 CONCEPT OVERVIEW
--------------------------------------------------------------------------------
Creating a custom iterator in Python involves implementing the __iter__() method
in a class. This method is a crucial part of the iterator protocol and allows
you to define how your custom object behaves as an iterator.

THE __iter__() METHOD
--------------------------------------------------------------------------------
The __iter__() method has two main purposes:

1. It makes an object iterable.
2. It returns the iterator object itself.

Basic structure:
"""

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

"""
IMPLEMENTING __iter__()
--------------------------------------------------------------------------------
To implement __iter__() in your custom class:

1. Define the __iter__() method within your class.
2. The method should return the iterator object itself (usually self).

Example:
"""

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
print("=== CountDown Example ===")
countdown = CountDown(5)
for num in countdown:
    print(num)

"""
Explanation:
In this example, the __iter__() method returns self, making the CountDown
object both an iterable and its own iterator.

KEY POINTS
--------------------------------------------------------------------------------
• __iter__() is called when you use iter() on an object or when the object
  is used in a for loop.

• Returning self in __iter__() is common when the class implements both
  __iter__() and __next__().

• If your class only implements __iter__(), it should return a separate
  iterator object that has a __next__() method.

• By implementing __iter__(), you make your custom objects iterable,
  allowing them to be used in for loops and with other iterator-based
  operations in Python.
"""

# ==============================================================================
# Challenge: AlphabetIterator
# ==============================================================================

"""
Challenge
---------
Create a custom iterator class called AlphabetIterator that generates
uppercase letters of the English alphabet.

Requirements:
- Read a single uppercase letter as input.
- Start from 'A'.
- Continue until the specified letter (inclusive).
- Implement __iter__().
- Print one letter per line.
"""

# ==============================================================================
# Solution 1 (Using ord() and chr())
# ==============================================================================

# Read input
# end_letter = input().strip()

class AlphabetIterator:
    def __init__(self, end_letter):
        self.end_letter = end_letter
        self.current_letter = 'A'

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_letter > self.end_letter:
            raise StopIteration
        result = self.current_letter
        self.current_letter = chr(ord(self.current_letter) + 1)
        return result

  
    alphabet_iter = AlphabetIterator(end_letter)
    for letter in alphabet_iter:
       print(letter)

# ==============================================================================
# Solution 2 (Using a List)
# ==============================================================================

# Read input
# end_letter = input().strip()

class AlphabetIteratorList:
    def __init__(self, end_letter):
        self.end_letter = end_letter
        self.current_letter = 'A'
        self.letters = [
            "A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        ]
        self.current_index = 0
        self.end_index = self.letters.index(self.end_letter)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration

        letter_to_return = self.letters[self.current_index]
        self.current_index += 1
        return letter_to_return

 
    alphabet_iter = AlphabetIteratorList(end_letter)
    for letter in alphabet_iter:
       print(letter)

# ==============================================================================
# QUICK SUMMARY
# ==============================================================================
#
# __iter__()  -> Makes an object iterable and returns the iterator.
# __next__()  -> Returns the next value.
# iter(obj)   -> Calls obj.__iter__().
# StopIteration -> Ends the iteration.
#
# A for loop automatically calls both __iter__() and __next__().
# ==============================================================================
