import datetime as y
x=y.datetime.now()
print(x.year)
print(x.strftime("%A"))#day
print(x.strftime("%B"))#m
x=y.datetime(2021,6,1) #returns specified month,day
print(x.strftime("%B"))

# Get the current date and time
current_datetime = y.datetime.now()
print("Current date and time:", current_datetime)
# Create a specific date
specific_date = y.date(2023, 12, 28)
print("Specific date:", specific_date)
# Create a specific time
specific_time = y.time(12, 30, 45)
print("Specific time:", specific_time)
# Perform date arithmetic
date1 = y.date(2023, 12, 28)
date2 = y.date(2023, 12, 31)
difference = date2 - date1
print("Difference in days:", difference.days)
