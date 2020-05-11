'''
Exercise 15: Distance Units
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
'''

feet = float(input('Enter your distance in feet: '))

print('The equivalent distance in inches is', feet * 12)
print('The equivalent distance in yards is', feet * 0.333333)
print('The equivalent distance in miles is', feet * 0.000189394)