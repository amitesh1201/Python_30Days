# Ask the user for their name, and then greet the user, using their name as part of the greeting.
# The name should be in title case, and shouldn't be surrounded by any excess white space.
# For example, if the user enters "lewis ", your output should be something like this:
#   Hello, Lewis!

name = input("Enter your name: ").strip().title()
print("Hello, " + name + "!")

print(f"Hello, {name}!")
