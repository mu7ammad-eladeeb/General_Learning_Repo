guests = ["Ramy", "Taha", "Sameh", "Janna"]
name = input("Please enter your name: ").capitalize() # .capitalize() is used to make the first letter only capital when entering any shape of letters like rAmy
if name in guests:
    print(f"Good to see you, {name} \nWelcome to the party")
else:
    print(f"Sorry, couldn't find the name {name} on our list")
# Rock Paper Scissors challenge (My Answer):
# Welcome to the Rock, Paper, Scissors game:
import random
computer_list = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(computer_list)
print("Welcome to the Rock, Paper, Scissors game: ")
# Press Enter to continue or type (Help) for the rules
user_input = input("Press Enter to continue or type (Help) for the rules: ").lower()
if user_input == "help":
     print("""*****RULES*****
          1) You choose and the computer chooses
          2) Rock smashes Scissors -> Rock wins
          3) Scissors cut Paper -> Scissors win
          4) Paper covers Rock -> Paper wins""")
# Enter your choice (rock, paper, scissors): paper (for example) # You chose: paper ##    Computer chose: scissors ##  You lost scissors beats paper.
your_choice = input("Enter your choice (rock, paper, scissors): ").capitalize()
# after this line, I put if statement أسطر كثيرة