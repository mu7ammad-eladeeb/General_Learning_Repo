age = input ("How old are you? \n")
int_age = int(age)
year = 2025
born_in = year - int_age
str_born_in = str(born_in)
print ("You were born in the year: " + str_born_in)
# Other Solution: 
int_age = int(input("How old are you? \n"))
year = 2025
str_born_in = str(year - int_age)
print("You were born in the year: " + str_born_in)
# f-string = format-string
# using f-string in the following code:
int_age = int(input("how old are you? \n"))
print (f"You were born in the year: {2025 - int_age}")
