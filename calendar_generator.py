import calendar

print("📅 Calendar Generator")

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print("\n")
print(calendar.month(year, month))
