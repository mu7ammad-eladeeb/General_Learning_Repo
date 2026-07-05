# ==============================================================================
# Topic: Python Module Aliasing (Using the 'as' Keyword)
# Source: Mimo Core Curriculum Progress Notes
# Description: Cheat sheet covering how and why we rename modules in Python.
# ==============================================================================

"""
📖 CONCEPT OVERVIEW: WHAT IS ALIASING?
--------------------------------------------------------------------------------
Aliasing means giving a temporary new name to a module that you are importing.
Instead of using its full, long name throughout your code, you use a shorter, 
custom nickname (an alias).

The primary tool for this is the `as` keyword.
"""

# ==============================================================================
# 🔥 REASON 1: MAKING LONG NAMES SHORTER (Readability & Speed)
# ==============================================================================
# Standard modules like 'statistics' can feel repetitive and clutter your code.
# Aliasing lets you write cleaner syntax.

import statistics as stats  # Re-assigns 'statistics' to 'stats'

ids = [33, 123, 22, 798, 23, 33]
sales = [23, 43, 26, 26, 29, 18, 24]

# Instead of statistics.mode() or statistics.median(), we use the alias:
calculated_mode = stats.mode(ids)
calculated_median = stats.median(sales)

print("--- Reason 1: Shorter Names ---")
print(f"Dataset Mode: {calculated_mode}")      # Expected Output: 33
print(f"Dataset Median: {calculated_median}")  # Expected Output: 26
print()


# ==============================================================================
# 🛡️ REASON 2: PREVENTING NAME CLASHES (Namespace Protection)
# ==============================================================================
# If you create a variable that shares the exact same name as an imported module,
# Python will get confused, overwrite the module link, and throw errors. 
# Aliasing protects your imports from being overwritten.

import math as math_constants  # Renamed so 'math' remains free for variables

# We can now safely name a local variable 'math' without breaking our math module!
math = "Grade 12 constants" 

print("--- Reason 2: Preventing Overwrite Errors ---")
print(f"Local String Variable: {math}")
print(f"Safe Module Constant Pi: {math_constants.pi}")  # Expected: 3.14159...
print(f"Safe Module Constant e:  {math_constants.e}")   # Expected: 2.71828...
print()


# ==============================================================================
# 🧮 PRACTICAL APPLICATION: COMBINING ALIASING WITH FUNCTIONS
# ==============================================================================
import math as m  # Aliasing the math library to a single letter 'm'

# floor rounding always drops down to the nearest whole integer value
floored_value = m.floor(44.32)

print("--- Practical Application: math as m ---")
print(f"Value 44.32 floor-rounded is: {floored_value}")  # Expected Output: 44


# ==============================================================================
# 💡 QUICK REFRESHER SUMMARY (FOR FUTURE REVIEW)
# ==============================================================================
# Q: What is using the 'as' keyword with a module known as?
# A: Aliasing.
#
# Q: Why do we use it?
# A: 1. To make code shorter and faster to write.
#    2. To prevent imported modules from interfering with our local variables.
#
# Syntax Pattern:
# `import [original_module_name] as [short_alias]`
# ==============================================================================
