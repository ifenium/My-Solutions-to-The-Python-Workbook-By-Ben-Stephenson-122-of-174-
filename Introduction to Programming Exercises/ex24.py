'''
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.
'''

m =  60
h = m * 60 
d = h * 24

days = float(input('Enter the number of days: '))    
hour = float(input('Enter the number of hours: '))
minutes = float(input('Enter the number of minutes: '))
seconds = float(input('Enter the numebr of seconds: '))

total = int(d * days + h * hour + m * minutes + seconds)

print('The amount of time in seconds is {}'. format(total))