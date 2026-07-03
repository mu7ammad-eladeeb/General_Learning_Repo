import random
random_number = random.random()  # Notice it stayed empty between the parentheses ()  the numbers between 0 - 1 but not 1 (Decimel numbers)
# (0 - 0.1 - 0.2 - 0.3 - 0.4 - 0.5 - 0.6 - 0.7 - 0.8 - 0.9 and until 0.99999999) and between them (0.11213 as an example)
print (random_number)
# It produces TypeError if numbers are put between the parentheses (No input must be used)
# If you want to put numbers between 0 and 5 put * 
# random_number = random.random() * 5 (between 0 and 0.999 * 5 = not reached 5 but reached 4.995)
# So if you want a number between 0 and 1000, multiply by 1000
print("Welcome to the virtual coin toss game لعبة رمي العملة الإفتراضية")
input ("Press Enter to start ....")
random_number2 = random.randint(0,1)
if random_number2 == 0:
    print("Heads ملك")
else:
    print("Tails كتابة")
# Another Solution or methond to write the code:
random_number3 = random.random()
if random_number3 >= 0.5:
    print("Heads")
else:
    print("Tails")
# Challenge Solution:
import random
print("Welcome to the Coin Guessing Game!")
print("""Choose a method to toss the coin:
1. Using random.randint()
2. Using random.random()""")
choice = int(input("1 or 2\n"))
game1 = input("Enter your Guess (Heads or Tails): \n").lower()
if choice == 1:
    game = random.randint(0,1)
    if game == 0 and game1 == "heads" :
        print("Congratulations! you won!")
    elif game == 1 and game1 == "tails":
        print("Congratulatoins! you won!")
    else: 
        print("You lose!")
elif choice == 2:
    game2 = random.random()
    if game2 >= 0.5 and game1 == "heads":
        print("Congratulations! you won!")
    elif game2 < 0.5 and game1 == "tails":
        print("Congratulations! you won!")
    else:
        print("You lose!")
else:
    print("Invalid Choice. Please select either 1 or 2.")
# Another solution (Ibrahim's solution)
import random
print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")
choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    random_number8 = random.random()
    if random_number8 >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
elif choice == "2":
    if random.randint(0,1) == 0:
        computer_result = "Heads"
    else: 
        computer_result = "Tails"
else:
    print("Invalid choice. Please select either 1 or 2.")
user_choice = input("Enter your Guess (Heads or Tails): ")
if user_choice.lower() == computer_result.lower():
    print("Congratulations! You won!")
else:
    print("Sorry, you lost!")
print(f"The computer's coin toss result was: {computer_result}")