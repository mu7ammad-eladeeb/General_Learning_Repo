# Conditional statements allow you to program machines that make decisions.
# In this lesson, you'll learn to program more complex scenarios.
# There will be situations where you don't need the else statement.
# This program only applies a discount when the age is under 18. the program does nothing else if the condition is not met, so the else statement can be skipped.
age = 16
if age < 18:
    print("Apply Discount")
print("Proceed to payment")
# When the else statement is not needed, you can simplify and have the code for the selection block in 1 line.
age = 16
if age < 18: print("Apply Discount")
print("Proceed to Payment")
# You can use the elif statement (short for 'else if') to check for more conditions if the first condition is not met.
# if, elif, and else statements need to be in the correct order.
# You can nest if-else statements withi each other.
# In the next lesson, you'll learn to work with collections of values in Python.