str_length = input("Enter the length: \n")
str_width = input("Enter the width: \n")
length = float(str_length)
width = float(str_width)
area = length * width
str_area = str(area)
cost_per_meter = input("How much for 1 meter? \n")
cost_per_1 = float(cost_per_meter)
print("The total area = " + str_area)
guy_money = cost_per_1 * area
str_guy_money = str(guy_money)
print("Give the guy: $" + str_guy_money)