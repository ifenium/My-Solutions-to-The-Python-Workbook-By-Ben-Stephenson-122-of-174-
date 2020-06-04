'''
Exercise 66: Compute a Grade Point Average
Exercise 51 included a table that shows the conversion from letter grades to grade
points at a particular academic institution. In this exercise you will compute the
grade point average of an arbitrary number of letter grades entered by the user. The
user will enter a blank line to indicate that all of the grades have been provided. For
example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 51 helpful when completing this exercise.
Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line
'''

grade = input('Enter your grade (press enter to quit): ').upper()

cgp = []

while grade != "":   
    if grade == 'A+' or grade == 'A':
        gp = 4.0
    elif grade == 'A-':
        gp = 3.7
    elif grade =='B+':
        gp = 3.3
    elif grade == 'B':
        gp = 3.0
    elif grade == 'B-':
        gp = 2.7
    elif grade == 'C+':
        gp = 2.3
    elif grade == 'C':
        gp = 2.0
    elif grade == 'C-':
        gp = 1.7
    elif grade == 'D+':
        gp = 1.3
    elif grade == 'D':
        gp = 1.0
    elif grade == 'F':
        gp = 0 
    else:
        gp = 'null'

    cgp.append(gp)
    grade = input('Enter your grade (press enter to quit): ').upper()   

cgpa = sum(cgp) / len(cgp)
print('Your CGPA is {}'. format(cgpa))