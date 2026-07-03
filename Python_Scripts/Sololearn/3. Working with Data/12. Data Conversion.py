# Data can come in the incorrect format. Data from surveys and web forms can come to you with quality issues.
# In this lesson, you'll learn to convert data to get it into the correct format.
# The input() instruction always turns the user input into a string, no matter what the user enters.
# Numerical values should not be stored as strings.
# You can convert data from one type to another to fix data quality issues.
# The int() instruction converts any type of value into an integer.
# You can use the int() instruction to convert the user input into an integer. For example: height = int(input())
# age = int(input()) here The order of instructions as follows: It asks the user for an input, The input from the user is converted into an integer, then the integer is stored in a variable.
# There are situations when you need values to be treated as floats.
# The float() instruction convert the value into a float.
# In a similar way, you can ensure that values are converted into strings with the str() instruction.
# The int(), str(), and float() instructions are examples of explicit conversion, which means they are performed by an instruction given by a programmer(like you).
# On the other hand, examples of implicit (automatic) data type conversions as follows:
# Examples of automatic data type conversions.
x = 5 # integer.
y = 2 # integer.
z = x/y # float (implicit conversion)
print (z)
# In the next lesson, you'll fix more issues with data types.