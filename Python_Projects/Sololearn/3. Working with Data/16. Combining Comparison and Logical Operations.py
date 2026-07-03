# In this lesson, you'll mix comparison and logical operators to make even faster, more accurate programs.
# The result of comparison operation is always a Boolean.
# The code inside a smartwatch stores the user's heart rate into a variable.
# You can store boolean values in variables just like you do with other data types. # The smart watch can detect when the user is sleeping. 
# Complete the code to store the boolean into the variable. 
sleep = True
# You can store the result of a comparison operation as a variable:
# # heart_rate = 165 # peak_rate = heart_rate > 160
heart_rate = 165
peak_rate = heart_rate > 160
print(peak_rate)
# You can store the result of a logical operation in a variable:
a = True and False 
print(a)
# The code inside a smart home stores the state of the lights in a variable. Complete the code:
light_on = True
light_on = True
door_locked = False
print(light_on or door_locked)
# Python is a case sensitive language.
# Both "True" and "False" start with an uppercase letter.
# Both "and" and "or" operators are lowercase in Python.
light_on = True
door_locked = False
print(light_on or door_locked)
print(light_on and door_locked)
# The smart home stores the temperature in degrees Celsius (C) in a variable.
# The temperature control system turns on the air-conditioning when the temperature is greater than 30 C:
temp = 35
ac_on = temp > 30
print(ac_on)
# You can put parentheses around the operations that should be done first. It makes the code easier to read:
a = (3 > 2) or False
# The smart home can detect the presence of people in the house:
# (temp > 30) or presence
# The temperature control system should only turn on the air-conditioning when the temperature is greater than 30 C and there are people in the house:
# presence and (temp > 30)
# The air-conditioning is turned on when temperature is greater than 30 and there are people in the house:
# ac-on = (temp> 30) and presence
# You learned that: 
# 1. You can store boolean values in variables.
# 2. You cna store the result of logical comparison operations in variables.
# 3. You can combine operations with logical and comparison operators.
# In the next lesson, you'll learn to control the order in which computers execute instructions.
