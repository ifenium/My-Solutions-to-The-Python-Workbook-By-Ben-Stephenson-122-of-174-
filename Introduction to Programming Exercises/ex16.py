'''
Exercise 16: Area and Volume
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
'''

import math

radius = float(input('Enter your radius: '))

circle = math.pi * (radius) ** 2
sphere = math.pi * 4/3 * (radius) ** 3

print('The Area of the circle with radius {} is {} meter squared'.format(radius,circle))
print('The Volume of the sphere with radius {} is {} meter cube'.format(radius,sphere))