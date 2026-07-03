# Ibrahim's Solution:
# Step 1: Setup
library = []
wishlist = []
# Step 2: Adding Individual Books
book_name = input("Enter the name of a book you own: ")
library.append(book_name)
book_name = input("Enter the name of another book you own (or press 'Enter' to skip): ") # Notice that it's the same previous variable (python here with replace the value in it to the new one)
if book_name:
    library.append(book_name)
print("\n Library:", library) # New way to print a variable
# Ex: name = input("What is your name: ")
#     print("Hello,", name," Nice to meet you") # Notice the way to write it
# Ste 3: Managing the Wishlist
book_name = input("\nEnter the name of a book you wish to have in the future: ")
wishlist.append(book_name)
book_name = input("Enter the name of anotehr book you wish to have (or press 'Enter' to skip): ")
if book_name:
    wishlist.append(book_name)
print("\nYour Wishlist: ", wishlist)
# Step 4: Mergin Wishlist into Library
acquired_book = input("\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if acquired_book in wishlist:
    library.append(acquired_book)
    wishlist.remove(acquired_book)
print("Updated Library: ", library)
print("Updated Wishlist: ", wishlist)
# Step 5: Donating books
donated_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donated_book in library:
    library.remove(donated_book)
print("\nFinal Library after Donations: ", library)