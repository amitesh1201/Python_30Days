# String interpolation with the format method
# String interpolation is the act of inserting some new content into an existing string.
# "John is 24 years old!"

# Method: 1 

print("{} is {} years old!".format("John", 24))


# Alternative ways of using format
#For example, let’s say we have a string like this:
#"{} is {} years old, and {} works as a {}."

#The intention here is for our output to look something like this:
#"John is 24 years old, and John works as a web developer"

output = "{} is {} years old, and {} works as a {}."

print(output.format("John", 24, "John", "web developer"))

# Optionally we can number our placeholders, which will let us reuse values. Always start with 0.

output = "{0} is {1} years old, and {0} works as a {2}."

print(output.format("John", 24, "web developer"))


# Use some name inside each placeholder like so:

output = "{name} is {age} years old, and {name} works as a {job}."

# Now we can call the format method like this:

print(output.format(name="John", age=24, job="web developer"))


# Optional method
#name = input("Please enter your name: ")
#age = input("Please enter your age: ")

#print("{} is {} years old!".format(name, age))
