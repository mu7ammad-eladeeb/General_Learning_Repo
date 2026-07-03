print("""
       @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@
      """)
print ("Welcome to the island 🏝️ \n")
print ("There are two doors in front of you. a red door 🚪 and a blue door 🚪")
door_choice = input("which door do you want to open? \n") # you can use here .lower() or .upper() istead of repeating them after this line.
if door_choice.lower() == "red":
    print("Great! now you entered a room.")
    print("you found three boxes: White 📦, Black 📦, Green 📦")
    box_choice = input("Which box do you open?\n")
    if box_choice.lower() == "white":
        print("Oops! YOu opened a box filled with snakes 🐍🐍🐍")
    elif box_choice.lower() == "black":
        print("Oops! You opened a box filled with spiders 🕷️🕷️🕷️")
    elif box_choice.lower() == "green":
        print("Congratulations! You found the treasure! 🪙🪙🪙")
    else:
        print("Invalid Choice! 🤷🤷🤷 Please enter from the given choices ")
elif door_choice.lower() == "blue":
    print("""Oops! You entered the crocodile door 🐊🐊🐊"
    Game over!""")
else:
    print("Invalid choice! 🤷🤷🤷 Please choose from the given choices")
# The solution of the second project:
print ("Welcome in the test of if you are from Tanta or not")
vehicle = input ("You want to take taxi, microbus, or Ober?\n").lower()
if vehicle == "microbus":
    print("Difficult")
elif vehicle == "ober":
    print("Sorry! our service is not available in Tanta")
elif vehicle == "taxi":
    print("Your choice is correct (taxi)")
    taxi_choice = input =("There are 3 taxies in front of you: White, Red, and Green. Choose one").lower()
    if taxi_choice == "green":
        print("Not used in Tanta")
    elif taxi_choice == "red":
        print("Sorry! we are not in Damietta")
    elif taxi_choice == "white":
        credit = input("You want to pay Cash or Visa").lower()
        if credit == "visa":
            print("No Vias is used in Tanta's taxies")
        elif credit == "cash":
            print("Ok")
        else:
            print("Sorry! choose from between the choices 3")

    else:
        print("Sorry! Choose from between the choices 2")
else:
    print("Sorry! Choose from between the choices 1")


