'''
Exercise 12: Distance Between Two Points on Earth
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is: distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
'''

import math
print('Please input each value in degrees not radians: ')

t1, g1 = input('Enter the longitude and latitude of Point A separated by a comma(,): ').split(',')
t2, g2 =  input('Enter the longitude and latitude of Point B separated by a comma(,): ').split(',')


t1 = math.radians(int(t1))
g1 = math.radians(int(g1))
t2 = math.radians(int(t2))
g2 = math.radians(int(g2))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print('The distance between points {},{} and {},{} following the surface of the Earth, in kilometers is: {}'. format(t1,g1,t2,g2,distance))