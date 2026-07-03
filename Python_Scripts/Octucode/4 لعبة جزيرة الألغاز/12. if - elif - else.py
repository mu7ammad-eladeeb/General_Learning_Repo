print("Welcome to my application")
age = int(input("Enter your age \n"))
if age >= 12:
    print("You can use the app")
else:
    print("You can't use the app")
# Python use indentation
# The if statement with its lines is called a code block مجموعة الأوامر اللي بتتنفذ مع بعض 
# Python is an indent language.
# JavaScript, C++, Java, and C# use Curly brackets { } to identify the start and the end.
number = float(input("Enter a number \n"))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is 0")
mark = float(input("Enter your mark \n"))
if mark >= 90:
    print("امتياز")
elif mark >= 75 and mark < 90:
    print("جيد جدًا")
elif mark >= 50 and mark < 75:
    print("جيد")
else:
    print("ضعيف")
# Another Solution:
score = float(input("Enter your test score: "))
if score >= 90:
    print("You got an A grade!")
elif score >= 75:
    print("You got a B grade!")
elif score >= 50:
    print("You got a C grade!")
else:
    print("You got an F grade")

