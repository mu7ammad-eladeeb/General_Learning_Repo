# print ("""
#
#
# """)   This is called multiline print statement. In market multi print funciton is used. NOt This new way.
# This is useful in printing ASCII art.
# name = input("""
#
#
# """)   can be used with input function, too.
# The Following is the method by which we enter the code:
#Show welcome message
print("welcome to the show")
#Ask the user to enter his name
name = input("What is your name? \n")
#print welcome, user
print(f"Welcome {name}")
# The Solution of the project:
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