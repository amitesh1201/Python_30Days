# 2) Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.

username = input("Please enter your name: ").strip().title()

print(f"Hello, {username}!")

# or 

# name = input("Please enter your name: ")
# name = name.strip().title()