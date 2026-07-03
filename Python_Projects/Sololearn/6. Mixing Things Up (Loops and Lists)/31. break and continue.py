# While developing applications, you'll often work with functions that handle various data types.
# In this lesson, you'll learn how to use functions with lists to enhance your code's efficiency.
# Python has two main types of loops: for loop, while loop
# We use for loop in executing an action a specific number of times
# We use while loop for executing an action while a condition remains true.
# The break statement is used to stop the loop when some condition is met.
# This is very useful when searching for a specific item or condition, and there's no need to continue once it's found.
songs = ["Hello", "Yesterday", "Happy", "Hallelujah"]
for song in songs:
    print("Searching")
    if song == "Happy":
        print("Playing" + song)
        break
# The break statement must be placed within the if statement where the condition is defined, ensuring proper indentation.
# The break statement... Stops a loop when a condition is met.
# The break statement can be used with while loops as well.
# The loop in the following code will stop when the value of x is 5. Run the code to see it in action:
x = 1
while x < 10:
    print(x)
    if x==5:
        print("Stop")
        break 
    x+=1
# The break statement is particularly handy with while loops when you're unsure when a specific condition will be satisfied.
# For instance, the following code will keep asking the user for input and display it until they enter 'Stop':
while True:
    text = input()
    print(text)
    if text == "Stop":
        break
# while True means the while loop's condition is always true, causing it to run indefinitely. It will only stop when the condition for the break statement is met.
# The continue statement allows you to skip the current iteration of a loop when a certain condition is true.
# In the code below, all ages from the list will be printed except those below 18:
ages = [13, 19, 22, 8, 75, 34, 26, 41]
for age in ages:
    if age<18:
        continue
    print(age)
# You can use the continue statement with while loops.
# The code below will skip the iteration when the day number is 4.
day_number = 1
while day_number <=7:
    if day_number == 4:
        day_number += 1
        continue
    print(day_number, "Turn on the lights!")
    day_number += 1
# Both statements (break and continue) are used in conjunctionwith an if statement inside the loop
