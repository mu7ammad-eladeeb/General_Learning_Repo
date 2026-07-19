try:
    a = int(input())
    b = int(input())
    div = a / b
    print("Division is:", div)
except ValueError:
    print("Not a Number")
