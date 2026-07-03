print(9//3)
print(9%2)
print (10//3)
print (10%3)
# // is called Floor division القسمة
# % is called Modulo operator باقي القسمة
num_seconds = input("Enter the number of seconds \n")
total_seconds = int(num_seconds)
num_hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
num_minutes = remaining_seconds // 60
num_seconds = remaining_seconds % 60
print ("hours " + str(num_hours) + " minutes " + str(num_minutes) + " seconds " + str(num_seconds))
# Other Solution
seconds = int (input("Enter the duration in seconds: \n"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60 
print(f"The duration is: {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
# Other Solution using two statements only.
int_num_seconds = int(input("Enter the number of seconds \n"))
print (f"hours: {int_num_seconds // 3600}  mintes: {int_num_seconds % 3600 // 60} seconds: {int_num_seconds % 3600 % 60}")