'''
Exercise 19: Free Fall
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known
'''

import math 

height = float(input('Enter the height from which the object drops in meters: '))
g = 9.8
vf = math.sqrt(2 * g * height)

print('The final velocity when the objects hits the ground is  {} m/s^2'. format(vf))