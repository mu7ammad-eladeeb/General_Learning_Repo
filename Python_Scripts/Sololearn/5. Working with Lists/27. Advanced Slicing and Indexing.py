# Indexing and silcing are incredibly useful, allowing you to fully control the data you extract from sequences.
# You can use indexing and slicing on lists and strings, because they are ordered sequences.
# You can combine positive with negative indexing when slicing. ex:
c = ['$', '%', '^', '*']
print(c[1:-1])  # the result is ['%','^']
# Remeber lists are mutable. You can change the values in a list after it has been created. ex:
c = ['$', '%', '^', '*']
c[:2] = ['f', 'B']
print(c) # the output will be ['f','B','^','*']
# Remember that string is not mutable.
# You did it! You learned that: Python supports "indexing from the end" (negative indexing), The last value of a sequence has an index of -1
