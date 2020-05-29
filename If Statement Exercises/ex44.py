'''
Exercise 44: Date to Holiday Name
Canada has three national holidays which fall on the same dates each year.
Holiday             Date
New year’s day      January 1
Canada day          July 1
Christmas day       December 25
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
'''

month = input('Enter a month of the year: ').lower()
day = int(input('Enter a day of the month: '))

if month == 'january' and day == 1:
    holiday = 'New year’s day'
    print('The fixed date holiday which corresponds to the day and month you entered is {}'. format(holiday))
elif month == 'july' and day == 1:
    holiday = 'Canada day'
    print('The fixed date holiday which corresponds to the day and month you entered is {}'. format(holiday))
elif month == 'december' and day == 25:
    holiday = 'Christmas day'
    print('The fixed date holiday which corresponds to the day and month you entered is {}'. format(holiday))
else:
    print('Enter a valid fixed-date holiday')