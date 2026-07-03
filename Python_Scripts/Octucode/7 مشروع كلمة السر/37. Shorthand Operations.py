# Challenge's Ibrahim's Solution:
items = []
prices = []
print("\n**** Welcome to iShop calculator **** \n")
number_of_items = int(input("How many items are there in your basket today? "))
if number_of_items > 0:
    print("\nLet's get to counting them .... ")
    for i in range(0, number_of_items):
        name = input(f"Please tell me the name of the item number {i+1} ")
        items.append(name)
        price = float(input((f"What is the price of {name}\n$")))
        prices.append(price)
    choice = input("Would you like to see your entire basket items? ").lower()
    if choice == "yes":
        print(items)
        see_price = input("Would you like to see how much it'll cost? ").lower()
        if see_price == "yes":
          print("\nBuying these items will cost: ")
          print(sum(prices))
        else:
          input("Press enter to exit")
    
else:
    print("Seems like you're not in the mood for shopping today")
# Shorthand Operations:
x = 5
x = x + 1
print(x)
x += 3 # Here it will make x + what equals to 3 (= x + 3)
print(x)
message = "Hello"
message += " world\n"
message *= 3
print(message)  # Notice that - and /  are not used with text as they will make problems
# Another Answer (My Answer) to sum the numbers:
total = 0
print("Let's add each number to the next")
for y in range(1,6):
   total += y
   print(f"-> {total}")
   print (total)