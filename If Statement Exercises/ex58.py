'''
Exercise 58: Next Day
Write a program that reads a date from the user and computes its immediates uccessor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.
'''

date = input('Enter a date in the format (Year-Month-Day): ' )

date = date.split('-')
year, month, day = int(date[0]), int(date[1]), int(date[2])
days_30  = [9,4,6,11]
days_31 = [1,3,5,7,8,10]

if year % 400 == 0 or year % 4 == 0:
    leap = True
    feb = 29 
elif year % 100 == 0:
    leap = False
    feb = 28
else:
    leap = False


if month == 2 and leap:
    if 1 <= day <= 28:
        day += 1
        month = month 
        year = year 
    elif day == 29:
        day = 1
        month += 1
        year = year 
elif month == 2 and not leap:
    if 1 <= day < 28:
        day += 1
        month = month 
        year = year
    elif day == 28:
        day = 1
        month += 1
        year = year 
elif month == 12:
    if 1 <= day < 31:
        day += 1
        month = month
        year = year 
    elif day == 31:
        day = 1
        month = 1
        year += 1 
elif month in days_30:
    if 1 <= day < 30:
        day += 1 
        month = month 
        year = year
    elif day == 30:
        day = 1
        month += 1
        year = year 
elif month in days_31:
    if 1 <= day < 31:
        day += 1 
        month = month 
        year = year 
    elif day == 31:
        day = 1
        month += 1
        year = year 

print('{}-{:0>2d}-{:0>2d}'. format(year, month, day))