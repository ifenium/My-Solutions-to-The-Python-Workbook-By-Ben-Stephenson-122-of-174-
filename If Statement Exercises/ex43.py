'''
Exercise 43: Faces on Money
It is common for images of a country’s previous leaders, or other individuals of historical significance,
to appear on its money. The individuals that appear on banknotes in the United States are listed in Table 2.1.
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
'''

denomination = int(input('Enter the dollar note denomination: '))

if denomination == 1:
    face = 'George Washington' 
elif denomination == 2:
    face = 'Thomas Jefferson'
elif denomination == 5:
    face = 'Abraham Lincoln '
elif denomination == 10:
    face = 'Alexander Hamilton'
elif denomination == 20:
    face = 'Andrew Jackson'
elif denomination == 50:
    face = 'Ulysses S. Grant'
elif denomination == 100:
    face = 'Benjamin Franklin'

print('The face on the ${} bill is {}'. format(denomination, face))