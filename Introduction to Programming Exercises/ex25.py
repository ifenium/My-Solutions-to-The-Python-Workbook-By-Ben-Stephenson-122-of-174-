'''
Exercise 25: Units of Time (Again)
In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. 
The hours, minutes and seconds should all be formatted so that
they occupy exactly two digits, with a leading 0 displayed if necessary.
'''

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

input_seconds = int(input('How many seconds are there: '))

days = input_seconds // seconds_per_day
input_seconds %= seconds_per_day

hours = input_seconds // seconds_per_hour
input_seconds %= seconds_per_hour

minutes = input_seconds // seconds_per_minute
input_seconds % seconds_per_minute

print('The equivalent duration is, {:d}:{:02d}:{:02d}:{:02d}'. format(days,hours,minutes,input_seconds) )