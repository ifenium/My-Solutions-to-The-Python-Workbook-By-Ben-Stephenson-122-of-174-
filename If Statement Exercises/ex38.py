'''
Exercise 38: Month Name to Number of Days
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
'''

month = input('Enter the current month: ').lower()

days_30  = ['september','april','june','november']
days_31 = ['january','march','may','july','august','october','december']

if month in days_30:
    print('You have 30 days in', month)
elif month in days_31:
    print('You have 31 days in', month)
elif month == 'february':
    print('You have 28 or 29 days in', month)