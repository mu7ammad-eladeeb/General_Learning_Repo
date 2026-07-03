# append: (To add a new value at the end of a list)
colors = []
colors.append("red")
colors.append("blue")
print(colors)
# Project 1
# Add the first color you like:
color = []
first_color = input("Add the first color you like: ")
color.append(first_color)
# Do you want to add more colors? Yes, or No?
more = input("Do you want to add more colors? Yes, or No? ").lower()
if more == "yes":
    add = input("Add another color to the list: ")
    color.append(add)
    print(f"The colors you like are {color}")
elif more == "no":
    print(f"Ok, The color you like is: {color}")
else:
    print("Invalid choice!")
# extend: (To extend a list to include another list)
class_a = ["Tom", "Jack", "Sarah", "Ben"]
class_b = ["Fred", "Tina", "Michael"]
class_a.extend(class_b)
print(class_a)
# Another solution:
Class_a = ["Tom", "Jack", "Sarah", "Ben"] # Notice that I changed the first letter from small to capital.
Class_b = ["Fred", "Tina", "Michael"] # Notice that I changed the first letter from small to capital.
students = Class_a + Class_b
print (students)
print(type(students))
# Another solution:
CLass_a = ["Tom", "Jack", "Sarah", "Ben"] # Notice that L in CLass is capital.
CLass_b = ["Fred", "Tina", "Michael"]  # Notice that L in CLass is capital.
all_students = []
all_students.extend(CLass_a) # extend take only one input not (CLass_a, CLass_b) which is separated by comma.
all_students.extend(CLass_b)
print(all_students)
# remove: (To remove a value)
numbers = [3,5,7,9]
numbers.remove(3) # number is input not the index
print(numbers)
# if variable: (To check or validate if the user entered a value or left the question black)
name = input("What is your name: ")
if name: # If the user write something:
    print(f"Hello, {name}")
else: # If the user left the question blank:
    print("You forgot to enter your name")
# To validate if a value in a list or not:
fruit_basket = ["Apples", "Oranges", "Bananas"]
guess = input("Guess the name of the fruits in the basket: ")
if guess in fruit_basket:
    print("Good guess")
else:
    print("Sorry, better luck next time")
# The homework's project's answer (my answer):
own = []
wishlist = []
# Enter the name of a book you own: (answer: deep work)
own_book = input("Enter the name of a book you own: ")
own.append(own_book)
# Enter the name of anotehr book you own (or press 'Enter' to skip): (answer: scrum)
another_book_own = input("Enter the name of anotehr book you own: (or press 'Enter' to skip): ")
if another_book_own:
   own.append(another_book_own)
else:
    print("Continue!")
# Enter the name of a book you wish to have in the future: (answer: outlive)
wish_future = input("Enter the name of a book you wish to have in the futrue: ")
wishlist.append(wish_future)
# Enter the name of another book you wish to have (or press 'Enter' to skip): (answre: Monday)
another_wish_future = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if another_wish_future:
   wishlist.append(another_wish_future)
   print(f"Your Wishlist: {wishlist}")
else:
    print("Continue!")
# Your Wishlist: ['outlive', 'Monday']
# Enter the name of a book from your wishlist that you've acquired (or press'Enter' to skip:): (answer: Monday)
wishlist_acquired = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if wishlist_acquired:
   own.append(wishlist_acquired)
   wishlist.remove(wishlist_acquired)
# Updated Library: ['deep work', 'scrum', 'Monday']
   print(f"Updated Library: {own}")
# Updated Wishlist: ['outlive']
   print(f"Updated Wishlist: {wishlist}")
else:
    print("Continue!")
# Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): (answer: scrum)
donate_from_own = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donate_from_own:
   own.remove(donate_from_own)
# Final Library after Donations: ['deep work', 'Monday']
   print(f"Final Library after Donations: {own}")
else:
    print(f"Your final Library conatains: {own} \nYour Final Wishlist contains: {wishlist}")
