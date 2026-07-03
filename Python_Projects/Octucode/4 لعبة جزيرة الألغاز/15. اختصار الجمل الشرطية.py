# upper() is used to make all letters in text capital.
# lower() is used to make all letters in text small.
# Text = "Hello"
# big_text = text.upper() 
# small_text = text.lower()
area = input("Choose an area: (Cairo), (Alexandria), or (Tanta) \n")
if area.lower() == "cairo":
    print("You Chose Cairo")
elif area.upper() == "TANTA":
    print("Tanta is nice!")
elif area.lower() == "alexandria":
    print("Feels like summer!")
else:
    print(f"Sorry, {area} is not on our list!")
# Another Solution using or
area = input("Chose an area: (Cairo), (Alexandria, or (Tanta) \n")
if area.lower() == "cairo" or area.lower() == "alexandria" or area.lower() == "tanta":
    print(f"{area} is on our list!!")
else:
    print(f"Sorry, {area} is not on our list!")
# another project
name = input("Please enter your name: \n")
password = input("Please enter your password: \n")
if name.lower() == "ibrahim" and password == "hiThere":
    print ("Welcome back!")
else:
    print("Sorry, wrong name or password")
# The challenge solution
age = int(input("How old are you?\n"))
license = input("Do you have a license?\n")
if age >= 18 and license.lower() == "yes":
    print("You can ride")
elif age < 18 or license.lower() == "no":
    print("You can't ride")
else:
    print(f"Your entry of [ {license} ] is not understood")



