# The list can contain variant types of variables
# For example: treasure_chest = [12, "gold", 3.14, "ruby"]
basket = [["Apples", "Bananas"],["Milk", "Water"]]
print(basket[0]) # to print the first list.
print(basket[0][0]) # to print the fist value in the first list. (The fist zero for the list, and the other zero is for the value)
print(basket[0][0], basket[1][0]) # to print Apples Milk. Notice there are not quotation marks here and the previous lines.
desert = ["cake", "Candy"]
basket.append(desert) # you can make it directly like this: basket.append(["Cake", "Candy"])
print(basket)
# Insert method is used like this: list.insert(index, element)
books = ["Books2", "Book3", "Book5"]
books.insert(0,"Book1") # it's used to insert a value in any place you want unlike append which insert the value in the end.
print(books)
books.insert(3,"Book4") # to insert Book4 in the place 3
print(books)
# To insert book6: Use append or the index 5 using insert method.
# The homework project (My answer):
# [['Apples', 'Bananas'], ['Milk', 'Water']]
list = [['Apples', 'Bananas'], ['Milk', 'Water']]
# Press enter to change the content.....
Change = input("Press enter to change the content..... \n")
# Here is the updated basket:
# [['Oranges', 'Apples', 'Bananas', 'Kiwis'], ['Coffee', 'Milk', 'Tea'], [1, 2, 3]]
if Change:
    print("Please press enter! ")
else:
    print("Here is the updated basket:")
    list[0].insert(0,'Oranges')
    list[0].append('Kiwis')
    list[1].remove('Water')
    list[1].insert(0, 'Coffee')
    list[1].insert(2, 'Tea')
    list.append([1, 2, 3])
    print(list)