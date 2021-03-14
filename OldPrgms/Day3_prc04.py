# String interpolation with f-strings
# The format method is really useful, but in Python 3.6 we got a new piece of syntax called f-strings which makes string interpolation a lot easier in many cases.

# Let’s look at an example first. Here is one of our earlier examples using format:

name = "John"
age = 24

output = "{} is {} years old!".format(name, age)
print(output)

# And here is the same example using the newer f-string syntax:

name = "John"
age = 24

output = f"{name} is {age} years old!"
print(output)

# We can actually write any expression we want here. For example, let’s calculate John’s age in months right here in the string:

name = "John"
age = 24

output = f"{name} is {age * 12} months old!"
print(output)