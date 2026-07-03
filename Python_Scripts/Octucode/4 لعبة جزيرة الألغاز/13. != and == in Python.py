# ==
chair_number = int(input("Enter your chair number\n"))
if chair_number == 21:
    print ("You win")
else:
    print("sorry")
# !=
chair_number2 = int(input("Enter your chair number\n"))
if chair_number2 != 13:
    print("You win")
else:
    print("sorry")
# Another Solution:
chair_number3 = int(input("Enter your chair number\n"))
if chair_number3 > 13:
    print("You win")
elif chair_number3 < 13:
    print("You win")
else:
    print("sorry")
# project 1
password = "abc"
pass_input = input("Enter your password\n")
if pass_input == password:
    print ("welcome")
else:
    print("not correct")
# project 2
word = input("Enter yes, no, or maybe\n")
if word == "yes":
    print("Your typed yes")
elif word == "no":
    print("You typed no")
elif word == "maybe":
    print("You typed maybe")
else:
    print("Stick to the guidlines")
# project 3
num = 7
guess_num = int(input("Enter a number"))
if guess_num == num:
    print ("You entered the right number")
else:
    print("not correct")


