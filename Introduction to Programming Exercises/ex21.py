'''
Exercise 21: Area of a Triangle
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = b × h / 2
Write a program that allows the user to enter values for b and h. The program
should then compute and display the area of a triangle with base length b and height h.
'''

a = float(input('Enter the bredth of the triangle in meteres: '))
b = float(input('Enter the height of the triangle in meteres: '))  

area = a * b * 0.5
print('The area of the triangle is {} meters squared'.format(area))