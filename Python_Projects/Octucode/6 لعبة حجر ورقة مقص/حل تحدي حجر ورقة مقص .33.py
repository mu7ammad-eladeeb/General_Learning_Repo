import random
# Save Ascii in variables
rock_ascii = """ 
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
"""
paper_ascii = """
---'    ____)____
           ______)
          _______)
         _______)
---.__________) 
"""
scissors_ascii = """ 
---'   ____)
          ______)
       __________)
      (____)
---.__(___)
"""
print("\nWelcome to the Rock, Paper, Scissors game:")
confirm = input ("Press Enter to continue or type Help for the rules ").lower()
if confirm == "help":
    print("""
          ******** RULES ********
          1) You choose and computer chooses
          2) Rock smashes Scissors -> Rock wins
          3) Scissors cut Paper -> Scissors win
          4) Paper covers Rock -> Paper wins
          """)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
if user_choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
else:
    # Display user choice in ASCII
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nYouchose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")
    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if computer_choice == "rock":
        print(f"\nComputer chose:\n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"\nComputer chose:\n{paper_ascii}")
    else:
        print(f"\nComputer chose:\n{scissors_ascii}")
        #Scissors|Paper|Rock|
        # Win    |Lose |Tie |Rock
        # Lose   |Tie  |Win |Paper
        # Tie    |Win  |Lose|Scissors
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"You Won! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")