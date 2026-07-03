# Ibrahim's Answer to the last challenge (replace sum):
numbers = [1,2,3,4,5]
total = 0
print("Let's add each number to the next")
for i in numbers:
    total += i
    print(f"-> {total}")
    print(f"\nThe total number is: {total} \n")
# ------------------------------------------------------
# join is a method: is used to separate a string by anything like , or emoji:
name1 = "Ibrahim"
print( ", ".join(name1)) # Remember the it's a method so that't the syntax. # I, b, r, a, h, i, m
print("\n".join(name1))
names = ["Abbie", "Ben", "Cherry", "Decken", "Emily"]
print("➡️  ".join(names)) # will print the written inside the list names with separation of them by ➡️  .
separator = ", "
print(separator.join(names))
# slice: is used to take part of the list like a cake
names2 = ["Abbie", "Ben", "Cherry", "Decken", "Emily"]
print(names2[0]) # This is an example of slicing
# Remember the following:
for num in range(0,100,5):
    print(num)
# Then see this: (slicing)
names3 = ["Abbie", "Ben", "Cherry", "Decken", "Emily", "Farid", "Geral", "Henry", "Isaac"]
print (names3[0:4]) # It is like range here (it will print the indexes 0, 1, 2, 3 and stop)
# to put steps like range:
names4 = ["Abbie", "Ben", "Cherry", "Decken", "Emily", "Farid", "Geral", "Henry", "Isaac"]
print (names4[0:4:2]) # It will print a name and not the following to it. To print all print(names[0:9]) # if you make it names[0:100:2], it will negelct the increased range without error and print only until end of the list.
# you should write it accurately until end of the list so as not to distract another one in the team.
# Remember split syntax:
names5 = input("Write the names separated by a comma: ")
names_list = names5.split(", ")
print(names_list)
# The challege (My answer):
friends_names_list = input("Enter the first and last name of your friends separated by a comma: ").split(", ")
length1 = len(friends_names_list)
for i in range(0, length1):
  values = friends_names_list[i].split()
  print(values)
print("Abbreviated Names:")
for n in range(0, length1):
  values2 = friends_names_list[n].split(" ")
  print(".".join(values2[0:2]))
# Challenge 2:
# Get input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words back into a sentence
reversed_sentence = " ".join(reversed_words)

# Print the reversed sentence
print("Reversed sentence:", reversed_sentence)

  