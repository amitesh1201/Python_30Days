# The user should be given three prompts where they'll be asked to provide different information about an employee.
# One prompt should ask for the employee's name, another should ask for their hourly wage, and the final one should
# ask how many hours the employee worked this week.

# The employee name should be processed to ensure that it's in a particular format. All employee names should be stripped
# of any excess white space, and should be in title case. This means that each word is capitalised with all other letters
# being lowercase. For example, if the employer accidentally has caps lock on and they write "rEGINA gEORGE", the name will
# still be correctly stored as "Regina George".

# The employee's total earnings for the week should be calculated by multiplying the hours worked by their hourly wage.
# Remember that any user input we receive is going to be a string. While we can multiply strings, it won't quite do what
# you want in this case. It's also worth keeping in mind that the employee's wage, or the numbers of hours they worked,
# might not be a whole number.

name = input("Enter the employee name: ").strip().title()
hourly_wage = float(input("Enter their hourly wage: "))
hours_worked = float(input("How many hours have they worked this week? "))

earnings = hourly_wage * hours_worked

# After processing the employee's name and calculating their earnings for the week, the program should output this information
# as a single string. For example, output like this would be appropriate:
#     Regina George earned $800 this week.

print(f"{name} earned ${earnings} this week.")

print(f"{name} earned ${earnings:.2f} this week.")
