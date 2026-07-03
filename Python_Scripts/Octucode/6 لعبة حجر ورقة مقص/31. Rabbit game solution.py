# Ibrahim's solution
print("Welcome to place the rabbit\n")
field = [["🌲", "🌲", "🌲"], ["🌲", "🌲", "🌲"], ["🌲", "🌲", "🌲"]]
print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere should the rabbit go? 🐇 ")
position = input("Please choose a row and a column \n")
row = int(position[0])
column = int(position[1])
field[row-1][column-1] = "🐇" # the human will enter for example 2 which corresponds to 1 in python
print("\n Success ....\n")
print(f"{field[0]}, \n{field[1]}, \n{field[2]}")