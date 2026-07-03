# While loops are power ful because they can be used even wehn you don't know how many iterations will be needed
# While loops repeat code whilst a condition holds true. For example, a ticket seller at a theater will repeatedly sell tickets until all seats have been occupied.
seats = 500 # initial number of seats.
while seats > 0: # seat available?
    print ("Sell ticket") # ticket sold.
    seats = seats - 1 # number of seats updated.
# While loops begin with the keyword while.
# The while keyword is followed by the condition under which the code is repeated.
# When the condition no longer holds true, we exit the while loop
# If the code that gets repeated inside the loop is not indented, the code will result in a error.
# As with for loops, the initial while loop statement must be followed by a colon: symbol.
# Loops usually include counters, A counter is a variable that keeps track of the number of iterations.
# Counter variables are updated inside the loop, so they change with every iteration. An initial value is set outside the loop, as the starting point.
# With while loops you can run into what is known as an infinite loop. This is when the condition holds true forever, and the code never stops repeating.
seats = 300
while seats > 0:
    print("Sell ticket")
    #seats = seats - 1
# In the next lesson, you'll put your iteration skills into practice to solve real problems.