# Previous lesson's homework (Ibrahim's solution):
basket = [["Apples", "Bananas"], ["Milk", "Water"]]
print(basket)
input("Press enter to change the content")
basket[0].insert(0,"Oranges")
basket[0].append("Kiwis")
basket[1].remove("Water")
basket[1].insert(0,"Coffee")
basket[1].append("Tea")
basket.append([1,2,3])
print(f"Here is the updated basket {basket}")
# Challenge:
# Welcome to place the rabbit
# ['🌲', '🌲', '🌲']
# ['🌲', '🌲', '🌲']
# ['🌲', '🌲', '🌲']
# Where should the rabbit go? 🐇
# Please choose a row and a column 23
# Success ....
# ['🌲', '🌲', '🌲']
# ['🌲', '🌲', '🐇']
# ['🌲', '🌲', '🌲']
# My answer:
print("Welcome to place the rabbit")
list = [['🌲', '🌲', '🌲'], 
        ['🌲', '🌲', '🌲'], 
        ['🌲', '🌲', '🌲']
        ]
print(f"{list[0]}, \n{list[1]}, \n{list[2]}")
print("Where should the rabbit go?")
row = int(input("Please choose a row "))
column = int(input("Please choose a column "))
list[row-1][column-1] = '🐇'
print(list)