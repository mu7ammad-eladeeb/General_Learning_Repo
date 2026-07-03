import random
my_random_number = random.randint(0,10) # randint = random integer رقم عشوائي صحيح Notice that there is , not .
# 0 and 10 are included
print (my_random_number) # randint takes two numbers
import Imported
print (Imported.course) # prints python     (Name_of_the_file.function)
print (Imported.level) # prints Beginner    (Name_of_the_file.function)
print (Imported.teacher) # prints Ibrahim   (Name_of_the_file.function)
# The project:
import random
computer_input = random.randint(1000,9999)
user_input = int(input("Enter a 4-digit PIN code:\n"))
if user_input < 9999 and user_input > 1000:
    if user_input == computer_input:
        print ("Congratulations!")
    else: 
        print ("Failure! PIN code did not match.")
        print (f"The Computer generated this PIN: {computer_input}")
else:
    print("Please enter 4 digits")






