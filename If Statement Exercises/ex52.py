'''
Exercise 52: Grade Points to Letter Grade
In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average.
'''

gp = round( float(input('Enter your grade point: ')), 2)

if gp == 4.0:
    grade = 'A+'
elif 3.7 <= gp < 4.0:
    grade = 'A-'
elif 3.3 <= gp < 3.7:
    grade = 'B+'
elif 3.0 <= gp < 3.3:
    grade = 'B'
elif 2.7 <= gp < 3.0:
    grade = 'B-'
elif 2.3 <= gp < 2.7:
    grade = 'C+'
elif 2.0 <= gp < 2.3:
    grade = 'C'
elif 1.7 <= gp < 2.0:
    grade = 'C-'
elif 1.3 <= gp < 1.7:
    grade = 'D+'
elif 1.0 <= gp < 1.3:
    grade = 'D'
elif 0 <= gp < 1.0:
    grade = 'F'
else:
    grade = 'null'

if grade == 'null':
    print('Please enter a valid grade point')
else:
    print('Grade = {}'. format(grade))