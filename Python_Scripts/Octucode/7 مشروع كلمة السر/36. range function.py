# Challenge Solution (Ibrahim's Solution):
tasks_list = input("Enter your tasks for today separated by a comma: ").split(", ")
done_tasks = []
ongoing_tasks = []
for task in tasks_list:
    print(f"\n{task}\n")
    done = input("fDid you finish {task} already? \n").lower()
    if done == "yes":
        print("Nice Job")
        done_tasks.append(task)
    else:
        print("Try not to put it off")
        ongoing_tasks.append(task)
    print("-----------------------")
see_progress = input("Do you want to see your today's progress? (yes, no)").lower()
if see_progress == "yes":
    input("Please hit Enter to exit")
else:
    print("""
          ******** Done Tasks ****
          """)
    print(done_tasks)

    print("""
          ****** Ongoing Tasks *****
          """)
    print(ongoing_tasks)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# Range
# here the syntax is range(stop)
for i in range(10): # 10 here is called exclusive which means the interpreter don't print it.  
    print(i) # it will print from 0 to 9 (not 10 which is exclusive)
# Another syntax is range(start, stop)
for i in range(1,10):
    print(i) # will print from 1 to 9, if you want 10 to be printed write range(1,11)
# Another syntax is range(start,stop,step)
for i in range(0,20,2): # start at 0, end at 19 not 20 which is exlusive and step 2 steps for each turn. (Notice that the two steps here make it ends at 18 not 19)
    print(i)
# ---------------------------------
print("Welcome to the Multiplication table")
number = int(input("Enter a number: "))
print(f"\n Multiplication table for {number}: \n")
for i in range(1,11):
    result = number * i
    print(f"{number} x {i} = {result}")
# Challenge:
basket = []
numbers = []
print("***** Welcome to iShop calculator *****")
number_items = int(input("How many items are there in your basket today? "))
print("Let's get to counting them ....")
for number_item in range (1, number_items+1):
    item = input(f"Please tell me the name of the item number {number_item}: ")
    price =float(input(f"What is the price of the item number {number_item}:\n$"))
    basket.append(item)
    numbers.append(price)
basket_items_choice = input(f"Would you like to see your entire basket items? ").lower()
if basket_items_choice == "yes":
    print(basket)
basket_items_price = input("Would you like to see how much it'll cost? ").lower()
if basket_items_price == "yes":
    print(f"Buying these items will cost: {sum(numbers)}$")


