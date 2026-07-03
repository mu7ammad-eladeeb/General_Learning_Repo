# Course's Solution of the previous lesson's challenge:
numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if x%2 == 0:
        print(f"\n{x}")
print("\nFinished the loop successfully")
attendees = ["Alice", "Bob","Charile"]
for person in attendees:
    print(person)
    print("Attendence confirmed")
    print("-----")
# ------------------------------------------------
for person in attendees:
    print(person)
    status = input("Is this person attending? (yes/no): ").lower()
    if status == "yes":
        print("Attendance confirmed")
    elif status == "no":
        print("Attendance not confirmed")
    else:
        print("Invalid choice! pls run the code again and choose either yes or no")
print("----------------------------------")
# --------------------------------------------------
attendees_list = []
attendees = input("Enter the names of attendees separated by commas: ")
attendees_list = attendees.split(',')
for person in attendees_list:
    print("\n" + person + "\n")
    status = input("Is this person attending? (Yes/No): ").lower()
    if status == "yes":
        print("Attendance confirmed")
    elif status == "no":
        print("Attendance not confirmed")
print("-----------")
# ----------------------------------------------------
travel_list = input("Please type the names of the countries separated by a comma: ").split(", ")
for country in travel_list:
    print(f"\n{country}\n")
    visited = input(f"Have you ever visited {country} before? (yes,no)\n").lower()
    if visited == "yes":
      print("I hope you had a wonderful time \n")
    else:
      print("I hope you get to visit it soon \n")
    print("-------")
input("Press enter to extit......")
# The challenge:
tasks = input("Enter your tasks for today separated by comma: ").split(", ")
Done = []
Ongoing = []
for task in tasks:
    print(task)
    finish = input(f"Did you finish {task}? ").lower()
    if finish == "yes":
        print("Nice Job")
        Done.append(task)
    else:
        print("Try not to put it off")
        Ongoing.append(task)
    print("------")
progress = input("Do you want to see your today's progress?(yes,no) ").lower()
if progress == "yes":
    print(f"""
         ******* Done Tasks *******
          {Done}
         ******* Ongoing Tasks *******
         {Ongoing}
 """)
else:
    print("Ok, Program finished!")
    