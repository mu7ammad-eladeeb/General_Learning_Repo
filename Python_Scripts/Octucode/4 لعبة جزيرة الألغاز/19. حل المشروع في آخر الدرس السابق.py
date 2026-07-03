# The solution of the second project:
print ("Welcome in the test of if you are from Tanta or not")
vehicle = input ("You want to take taxi, microbus, or Ober?\n").lower()
if vehicle == "microbus":
    print("Difficult")
elif vehicle == "ober":
    print("Sorry! our service is not available in Tanta")
elif vehicle == "taxi":
    print("Your choice is correct (taxi)")
    taxi_choice = input("There are 3 taxies in front of you: White, Red, and Green. Choose one \n").lower()
    if taxi_choice == "green":
        print("Not used in Tanta")
    elif taxi_choice == "red":
        print("Sorry! we are not in Damietta")
    elif taxi_choice == "white":
        credit = input("You want to pay Cash or Visa \n").lower()
        if credit == "visa":
            print("No Vias is used in Tanta's taxies")
        elif credit == "cash":
            print("Ok")
        else:
            print("Sorry! choose from between the choices")

    else:
        print("Sorry! Choose from between the choices")
else:
    print("Sorry! Choose from between the choices")