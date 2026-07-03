# Answer to previous lesson's project: (1)
import random
print("Welcome to 'whose wallet?' ")
print("You will give me a list of names, and I will pick a person to pay")
names_string = input ("If you're ready, enter the names separated by a comma ")
names = names_string.split(", ")
length = len(names) -1
random_number = random.randint(0,length) 
random_person = names[random_number]
print(f"Please ask ' {random_person} ' to take his wallet out. Dinner is on him")
# Answer to previous lesson's project: (2)
import random
print ("Welcome to 'whose wallet?' ")
print ("You will give me a list of names, and I will pick a person to pay")
names = input ("If you're ready, enter the names separated by a comma ").split(", ")
print(f"Please ask{random.choice(names)} to take out his wallet, dinner is on him.") # .choice here is a method for the module random (أمر له علاقة بأمر آخر)
# fruits.append()   "append is a method"
# fruits.remove() fruits.extend()   "remove and extend are methods, too"
# random.choice()  random.randint()  random.random()   "choice, randint, random are methods, too"
# Answer to previous lesson's project: (3)
import random
print("Welcome to 'whose wallet?' \n You will give me a list of names, and I'll pick randomly ")
print(f"Please ask {random.choice(input('Enter the names separated by a comma: ').split(', '))} to take out his wallet. Dinner is on him! ")
# أهم أربع حاجات بنمشي عليهم في كتابة الكود
# 1. الصيانة (الكود اللي أسهل في القراءة أسهل في الصيانة)
# 2. التعاون (الناس اللي هتشتغل على نفس الكود)
# 3. إصلاح الأخطاء (الكود الأكثر تنظيمًا أسهل في اكتشاف الأخطاء)
# 4. الأداء (مش لازم يكون الكود الأقل في الأسطر هو الأكثر كفاءة)