day = int(input())
month = int(input())
year = int(input())
next_day = day + 1

if ((not year % 100 == 0) and year % 4 == 0) or year % 400 == 0:
    if month == 2 and next_day > 28:
        next_day = 1
        month = 3

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if next_day > 31:
     next_day = 1
     month += 1
    if month > 12:
        month = 1
        year += 1
else:
   if next_day > 30:
      next_day = 1
      month += 1
print(f"{next_day},{month},{year}")