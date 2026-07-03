import random
pin_code = random.randint(1000,9999)
user_input = int(input("Enter a 4_digit PIN code:\n"))
if len(str(user_input)) > 4 or len(str(user_input)) < 4: # another method:  if len(str(user_input)) != 4:   
    print("Please enter 4 digits")
elif user_input == pin_code:
    print ("Success! PIN code matched")
else:
    print("Failure! PIN code did not matched")
    print(f"The computer generated this PIN: {pin_code}" )