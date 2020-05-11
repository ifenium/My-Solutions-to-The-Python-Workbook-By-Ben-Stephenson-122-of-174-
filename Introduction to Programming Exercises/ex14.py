'''
Exercise 14: Height Units
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
'''

in_per_ft = 12
cm_per_in = 2.54

feet, inch =  input('Enter your height in feet and inches, seperate with a comma(,): ').split(',')

feet = int(feet)
inch = int(inch)
cm = ((feet * in_per_ft) + inch) * cm_per_in

print('Your height in centimerters is {} cm'.format(cm))