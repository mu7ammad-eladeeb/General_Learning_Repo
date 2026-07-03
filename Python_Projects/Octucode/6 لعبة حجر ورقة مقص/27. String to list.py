names_string = input("Enter names separated by a comma ..")
names = names_string.split(", ") # Separate items by , and space.
print(type(names))
print(names)
# refresh:
name = "Ibrahim"
print(len(name)) # To print the length of a variable (here the result is 7) 0, 1, 2, 3, 4, 5, 6 
# Continue
names = ["Ibrahim", "Aly", "Taha", "Mohsen"]
print(len(names)) # 0, 1, 2, 3 (Here the result is 4)
# Project (Homework):
import random
# Welcome to 'Whose wallet?'
print("Welcome to 'Whose wallet?'")
# You will give me a list of names, and I will pick a person to pay
print("You will give me a list of names, and I will pick a person to pay")
# If you're ready, enter the names separated by a comma
names_homework = input("Enter the names separated by a comma\n")
names_homework_list = names_homework.split(", ")
length = len(names_homework_list) -1 # Notice that -1 here is used as the length for example = 5 and the last index is 4
# Please ask 'Aly' to take his wallet out. Dinner is on them
who_will_pay_index = random.randint(0,length) # You can put the -1 here instead of above.
person_will_pay = names_homework_list [who_will_pay_index]
print(f"Please ask {person_will_pay} to take his wallet out. Dinner is on them")