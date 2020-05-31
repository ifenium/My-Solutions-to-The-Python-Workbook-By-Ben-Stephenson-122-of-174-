'''
Exercise 51: Letter Grade to Grade Points
At a particular university, letter grades are mapped to grade points in the followingmanner:
Letter Grade points
A+      4.0
A       4.0
A−      3.7
B+      3.3
B       3.0
B−      2.7
C+      2.3
C       2.0
C−      1.7
D+      1.3
D       1.0
F       0
Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
'''

grade = input('Enter your letter grade: ').upper()

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

if gp == 'null':
    print('Please enter a valid grade letter')
else:
    print('GP = {}'. format(gp))