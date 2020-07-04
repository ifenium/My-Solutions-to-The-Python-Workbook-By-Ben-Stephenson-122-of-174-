'''
Exercise 117: Line of Best Fit
A line of best fit is a straight line that best approximates a collection of n data points.
In this exercise, we will assume that each point in the collection has an x coordinate
and a y coordinate. The symbols x¯ and y¯ are used to represent the average x value in
the collection and the average y value in the collection respectively. The line of best
fit is represented by the equation y = mx + b where m and b are calculated using
the following formulas:

Write a program that reads a collection of points from the user. The user will enter
the x part of the first coordinate on its own line, followed by the y part of the first
coordinate on its own line. Allow the user to continue entering coordinates, with the
x and y parts each entered on their own line, until your program reads a blank line for
the x coordinate. Display the formula for the line of best fit in the form y = mx + b
by replacing m and b with the values you calculated using the preceding formulas.
For example, if the user inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your
program should display y = 0.95x + 0.1.
'''

x = []
y = []
xy = []
x_squared = []

originx = float(input('Enter the X part: '))
originy = float(input('Enter the Y part: '))

x.append(originx)
y.append(originy)
xy.append(originx * originy) 
x_squared.append(originx ** 2)

current = float(input('Enter the X part (Enter to end): '))
while current != '':
    currentx = float(current)
    currenty = float(input('Enter the Y part: '))

    x.append(currentx)
    y.append(currenty)
    xy.append(currentx * currenty)
    x_squared.append(currentx ** 2)
    current = input('Enter the X part (Enter to end): ')

sumx = sum(x)
sumy = sum(y)

meanx = sumx / len(x)
meany = sumy / len(y)

m = sum(xy) - (sumx * sumy / len(x)) / sum(x_squared) - (sumx ** 2 / len(x))

b = meany - m * meanx

print('y = {:.1f}x + ({:.1f})'. format(m, b))
