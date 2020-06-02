'''
Exercise 65: Compute the Perimeter of a Polygon
Write a program that computes the perimeter of a polygon. Begin by reading the x
and y values for the first point on the perimeter of the polygon from the user. Then
continue reading pairs of x and y values until the user enters a blank line for the
x-coordinate. Each time you read an additional coordinate you should compute the
distance to the previous point and add it to the perimeter. When a blank line is entered
for the x-coordinate your program should add the distance from the last point back
to the first point to the perimeter. Then it should display the total perimeter. Sample
input and output is shown below, with user input shown in bold:
Enter the x part of the coordinate: 0
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 1
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 0
Enter the y part of the coordinate: 1
Enter the x part of the coordinate: (blank to quit):
The perimeter of that polygon is 3.414213562373095
'''

from math import sqrt

perimeter = 0 

originx = float(input('Enter the X cordinate: '))
originy = float(input('Enter the Y cordinate: '))

lastx = originx
lasty = originy

current = float(input('Enter the X cordinate (Press enter to end): '))
while current != '':
    currentx = float(current)
    currenty = float(input('Enter the Y cordinate: '))
    distance = sqrt((lastx - currentx) **2  + (lasty - currenty ) ** 2)
    perimeter += distance

    lastx = currentx
    lasty = currenty

    current = input('Enter the X cordinate (Press enter to end): ')
    
distance = sqrt((originx - currentx) ** 2 + (originy - currenty) ** 2)
perimeter += distance

print('The perimeter of the polygon is {}'. format(perimeter))