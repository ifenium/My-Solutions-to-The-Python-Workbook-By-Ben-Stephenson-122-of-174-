'''
Exercise 4: Area of a Field
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
'''

Square_Feet_Per_Acre = 43560

length = float(input('Enter the length of the field in feet: '))
width =  float(input('Enter the width of the field in feet: '))

area = round((length * width) / Square_Feet_Per_Acre,5)

print('The area of the field is {} acres.'. format(area))