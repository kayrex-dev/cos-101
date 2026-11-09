# Calculate a student's weekly expenses.
student_name = input("Enter student name: ")
daily_transport = float(input("Enter daily transport cost: "))
daily_feeding = float(input("Enter daily feeding cost: "))
days = int(input("Enter number of days on campus: "))
other_expenses = float(input("Enter other weekly expenses: "))

transport_total = daily_transport * days
feeding_total = daily_feeding * days
weekly_total = transport_total + feeding_total + other_expenses

print()
print("WEEKLY EXPENSE SUMMARY")
print(f"Student: {student_name}")
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other_expenses:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")
