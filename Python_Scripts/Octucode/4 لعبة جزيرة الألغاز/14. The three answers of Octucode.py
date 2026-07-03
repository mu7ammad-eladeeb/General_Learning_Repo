# Project 1:
password = input("Please ener your password: \n")
correct_password = "abc"
if password == correct_password:
    print("welcome to the app")
else: 
    print("Sorry, you can't use the app")
# Project 2:
typed = input("Please type (Yes), (No), or (Maybe) \n")
if typed == "Yes":
    print (f"You typed {typed}")
elif typed == "No":
    print(f"You typed {typed}")
elif typed == "Maybe":
    print(f"You typed {typed}")
else:
    print (f"You typed {typed}, which is not an option \nplease stick to the options")
# Project 3:
guessed = int(input("Please guess a number: \n"))
correct_number = 7
if guessed == correct_number:
    print ("Good guess")
else: 
    print (f"You guessed {guessed}, but the corrct number is {correct_number}")