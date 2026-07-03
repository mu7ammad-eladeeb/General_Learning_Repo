# The functions upper() and lower() allow you to quickly change the case of a string to all in uppercase or lower case, respectively.
print('SmArTPoNe'.lower())
print('SmArTpHoNe'.upper())
# The upper() and lower() functions can only be used on strings
# Functions that only work on certain objects (strings, lists, etc) are called using dot . notation.
# Remember you can use variables in functions.
brand = "ikea"
print(brand.upper())
# The capitalize() function will save you time when you need to convert the first character of a string to uppercase, while making the remaining characters lowercase.
print("happy birthday".capitalize())
# Strings are immutable and functions won't change them. You'll need to store the modified string in a variable to keep it.
item = "smartwatch"
print(item.upper())
print(item) # original string
item2 = item.upper()
print(item2)
# The find() function checks if a character (or a pattern of characters) is present in a string. The function returns the index (position) of the given value. If the given value is present multiple times, the function will return the first occurrence (the lowest index)
print("Bee".find("e"))
# find() will return an error if you don't include an argument between the parentheses. With nothing to look for in the strings, the function can't do its job.
# This won't happen with upper(), lower() and capitalize(). They don't need any more information to compelete their task.
print('roBot'.upper())
print('roBot'.lower())
print("roBot".capitalize) # will make all characters in the string small except the first one capital
print("roBot".find())
# find() will return -1 if the value can't be fond in the stirng:
print("robot".find("A")) # output is -1 # if you write "robot".find("A") this will return -1 not output -1
# In the next lesson, you'll learn to use functions that work on lists.
