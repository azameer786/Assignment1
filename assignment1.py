#!/usr/bin/env python3

import sys

'Authur: azameer@myseneca.ca'
'Date: 8/02/2024'

def day_of_week(date: str) -> str:
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return 31

def after(date: str) -> str: 
    day, month, year = (int(x) for x in date.split('/'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return f"{day:02}/{month:02}/{year}"

def before(date: str) -> str:
    day, month, year = (int(x) for x in date.split('/'))
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)
    return f"{day:02}/{month:02}/{year}"

def usage():
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    try:
        day, month, year = (int(x) for x in date.split('/'))
        if 1 <= month <= 12 and 1 <= day <= mon_max(month, year):
            return True
    except ValueError:
        return False
    return False

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    current_date = start_date
    if num >= 0:
        for _ in range(num):
            current_date = after(current_date)
    else:
        for _ in range(-num):
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    
    start_date = sys.argv[1]
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()

    if not valid_date(start_date):
        usage()

    end_date = day_iter(start_date, num_days)
    weekday = day_of_week(end_date)
    
    print(f'The end date is {weekday}, {end_date}.')


