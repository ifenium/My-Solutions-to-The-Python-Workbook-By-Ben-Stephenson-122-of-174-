'''
Exercise 11: Fuel Efficiency
In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). 
In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units.
'''

import math

a = float(input('Enter your vehicle efficiency in miles-per-gallon(MPG): '))

km_l = 0.42514 * a
l_100km = (km_l ** -1) * 0.01

print('Your vehicle efficiency in L/100KM is {}L_100KM'. format(l_100km))