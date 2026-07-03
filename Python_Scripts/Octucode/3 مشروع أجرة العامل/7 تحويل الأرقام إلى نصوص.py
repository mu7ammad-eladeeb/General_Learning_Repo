PIN = input("Enter your PIN number\n")
print (len(PIN))
print(len(str(12345)))
# len doesn't receive except string and you can turn number into string using the function str or using " "
# type() is used to know the type of the variable
print (type(3)) # integer
print (type(3.0)) # float
print (type("3")) # string
print (type(PIN)) # remember that input doesn't receive except string
print (type(True)) # boolean