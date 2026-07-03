# f-strings, short for formatted strings, allow us to display expressions like addding a string to a number, without any error:
print(f"{2} new messages")
# We can also use expressions like new - read between the curly braces to display their value.
new = 5
read = 2
print(f"{new- read} unread messages")
# To reuse an f-string, we can save it in a variable, like here with status and f"{new} new message:
new = 5
status = f"{new} new messages"
print(status)
