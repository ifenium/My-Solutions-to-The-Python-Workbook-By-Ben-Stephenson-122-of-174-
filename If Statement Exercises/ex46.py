'''
Exercise 46: Season from Month and Day
The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise:
Season  First day
Spring  March 20
Summer  June 21
Fall    September 22
Winter  December 21
Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.
'''

month = input('Enter a month of the year: ').lower()
day = int(input('Enter a day of the month: '))

if month == 'december' and 21 <= day <= 31 or month == 'march' and  1 <= day < 20 or month in ['januray','february']:
    print('You\'re currently in Winter')
elif month == 'march' and 20 <= day <= 31 or month == 'june' and 1 <= day < 21 or month in ['april','may']:
    print('You\'re currently in Spring')
elif month == 'june' and 21 <= day <= 30 or month == 'september' and 1 <= day < 22 or month in ['july','august']:
    print('You\'re currently in Summer')
elif month == 'september' and 22 <= day >= 30 or month == 'december' and 1 <= day < 21 or month in ['october','november']:
    print('You\'re currently in Fall')