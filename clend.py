import calendar
year=int(input("Enter Year: "))
month=int(input("Enter month: "))
if(month>12):
    print("Enter valid month...!")
else:
    print(calendar.month(year,month))