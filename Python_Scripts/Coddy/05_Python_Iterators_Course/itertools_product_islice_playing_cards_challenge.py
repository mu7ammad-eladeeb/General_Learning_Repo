# ==============================================================================
# Topic: Challenge - Playing Cards Generator Using itertools.product() and
#        itertools.islice()
# Source: Coddy Course
# Description:
# Complete notes covering the Playing Cards challenge, including the
# problem statement, complete solution, and a detailed step-by-step
# explanation of how itertools.product() and itertools.islice() work.
# ==============================================================================

import itertools

"""
📖 CHALLENGE OVERVIEW
--------------------------------------------------------------------------------
In this challenge, you will use two functions from Python's itertools module:

• itertools.product()
• itertools.islice()

The goal is to generate every possible playing card from a list of ranks
and suits, then display only a selected portion of those cards.

This challenge demonstrates how iterators can efficiently generate and
process data without storing unnecessary values in memory.
"""

# ==============================================================================
# Challenge
# ==============================================================================

"""
Problem
-------
Create a program that generates playing cards.

Input
-----
Line 1:
    Card ranks separated by commas.

Line 2:
    Card suits separated by commas.

Line 3:
    Two integers representing the starting and stopping positions.

Requirements
------------
• Generate every possible combination of ranks and suits.
• Use itertools.product().
• Use itertools.islice() to extract only part of the generated cards.
• Print each selected card in the following format:

Rank of Suit

Example:

Ace of Spades
"""

# ==============================================================================
# Solution
# ==============================================================================

# Read input
# ranks = input().split(',')
# suits = input().split(',')
# start, stop = map(int, input().split())

# Generate every possible playing card
# cards = itertools.product(ranks, suits)

# Select only the requested cards
# selected_cards = itertools.islice(cards, start, stop)

# Print each selected card
# for rank, suit in selected_cards:
#     print(f"{rank} of {suit}")

# ==============================================================================
# Detailed Solution Explanation
# ==============================================================================

"""
Step 1
------
Import the itertools module.

import itertools

The itertools module provides efficient tools for creating and processing
iterators.

In this challenge we use:

• product()
• islice()

--------------------------------------------------------------------------

Step 2
------
Read the input.

ranks = input().split(',')

Suppose the user enters

Ace,King,Queen

After split(',')

ranks becomes

['Ace', 'King', 'Queen']


Now read the suits.

suits = input().split(',')

Suppose the input is

Spades,Hearts

After splitting

suits becomes

['Spades', 'Hearts']


Finally,

start, stop = map(int, input().split())

Suppose the user enters

2 5

Then

start = 2
stop = 5

--------------------------------------------------------------------------

Step 3
------
Generate every possible playing card.

cards = itertools.product(ranks, suits)

product() computes the Cartesian product.

This means:

Every rank is paired with every suit.

For

Ranks

Ace
King
Queen

and

Suits

Spades
Hearts

product() generates

(Ace, Spades)

(Ace, Hearts)

(King, Spades)

(King, Hearts)

(Queen, Spades)

(Queen, Hearts)

Notice that product() returns an iterator,
not a list.

Nothing is actually stored until values are requested.

Internally, it behaves similarly to

for rank in ranks:
    for suit in suits:
        yield (rank, suit)

The advantage is that product() is much more memory efficient.

--------------------------------------------------------------------------

Step 4
------
Slice the iterator.

selected_cards = itertools.islice(cards, start, stop)

Suppose

start = 2
stop = 5

The generated iterator looks like

Index 0

(Ace, Spades)

↓

Index 1

(Ace, Hearts)

↓

Index 2

(King, Spades)

↓

Index 3

(King, Hearts)

↓

Index 4

(Queen, Spades)

↓

Index 5

(Queen, Hearts)

Calling

itertools.islice(cards, 2, 5)

returns only

(King, Spades)

(King, Hearts)

(Queen, Spades)

Notice that

stop = 5

is NOT included.

This works exactly like list slicing:

my_list[2:5]

which includes

2
3
4

but not

5.

Unlike list slicing, however,

islice()

works directly on an iterator without converting it into a list.

--------------------------------------------------------------------------

Step 5
------
Iterate over the selected cards.

for rank, suit in selected_cards:

Each element produced by selected_cards
is a tuple.

Example

("King", "Spades")

Python automatically unpacks this tuple into

rank

and

suit

So

rank = "King"

suit = "Spades"

--------------------------------------------------------------------------

Step 6
------
Format the output.

print(f"{rank} of {suit}")

If

rank = "King"

and

suit = "Spades"

the output becomes

King of Spades

The loop repeats until every selected card has been printed.

--------------------------------------------------------------------------

Program Flow

Input

Ace,King,Queen

↓

Split

↓

["Ace", "King", "Queen"]

↓

Input

Spades,Hearts

↓

Split

↓

["Spades", "Hearts"]

↓

product()

↓

(Ace, Spades)

↓

(Ace, Hearts)

↓

(King, Spades)

↓

(King, Hearts)

↓

(Queen, Spades)

↓

(Queen, Hearts)

↓

islice(..., 2, 5)

↓

(King, Spades)

↓

(King, Hearts)

↓

(Queen, Spades)

↓

Print

King of Spades

King of Hearts

Queen of Spades
"""

# ==============================================================================
# Example Run
# ==============================================================================

"""
Input

Ace,King,Queen
Spades,Hearts
2 5

Output

King of Spades
King of Hearts
Queen of Spades
"""

# ==============================================================================
# Key Concepts
# ==============================================================================

"""
itertools.product()
-------------------
Generates the Cartesian product of two or more iterables.

Every element from one iterable is paired with every element from the
other iterable.

Returns an iterator.

------------------------------------------------------------

itertools.islice()
------------------
Returns only a specified portion of an iterator.

Works like list slicing:

[start:stop]

without creating a list.

Returns another iterator.

------------------------------------------------------------

Tuple Unpacking
---------------

Each value produced by product() is a tuple.

Example

("Ace", "Spades")

Using

for rank, suit in cards

Python automatically assigns

rank = "Ace"

suit = "Spades"

------------------------------------------------------------

Cartesian Product
-----------------

If

A = [1, 2]

B = ['X', 'Y']

product(A, B)

produces

(1, X)

(1, Y)

(2, X)

(2, Y)

Every possible combination is generated.

------------------------------------------------------------

Lazy Evaluation
---------------

Both

product()

and

islice()

produce values only when requested.

This is called **lazy evaluation**.

Because values are generated one at a time,
very little memory is required, even when working with large datasets.
"""

# ==============================================================================
# QUICK SUMMARY
# ==============================================================================
#
# product() generates every possible combination of multiple iterables.
#
# islice() extracts only part of an iterator.
#
# product() and islice() both return iterators.
#
# They generate values lazily, making them memory efficient.
#
# product() computes a Cartesian product.
#
# islice() behaves like normal list slicing but works directly on iterators.
#
# Tuple unpacking allows
#
#     for rank, suit in cards
#
# to automatically separate each generated tuple into two variables.
#
# Together, product() and islice() provide an efficient way to generate,
# filter, and process combinations without creating unnecessary lists.
# ==============================================================================
