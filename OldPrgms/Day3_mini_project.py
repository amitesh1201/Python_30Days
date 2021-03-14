# Mini Project - Day 3

emp_name = input("Enter employee name: ").strip().title()
hourly_wage = input("Enter the hourly wage: ")
work_hours = input("Enter the working hours: ")

total_earning = float(hourly_wage) * float(work_hours)

print(f"{emp_name} earned ${total_earning:.2f} this week.")