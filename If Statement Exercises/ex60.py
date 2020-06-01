'''
Exercise 60: Roulette Payouts
A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
• Single number (1 to 36, 0, or 00)
• Red versus Black
• Odd versus Even (Note that 0 and 00 do not pay out for even)
• 1 to 18 versus 19 to 36
Write a program that simulates a spin of a roulette wheel by using Python’s random
number generator. Display the number that was selected and all of the bets that must
be payed. For example, if 13 is selected then your program should display:
The spin resulted in 13...
Pay 13
Pay Black
Pay Odd
Pay 1 to 18
If the simulation results in 0 or 00 then your program should display Pay 0 or
Pay 00 without any further output.
'''

from random import randrange

value = randrange(0,38)
if value == 37:
    print('The spin resulted in 00..')
else:
    print('The spin resulted in {}'. format(value))

if value == 37:
    print('Pay 00')
else:
    print('Pay', value)

if value % 2 == 1 and value >= 1 and value <= 9 or\
    value % 2 == 0 and value >= 12 and value <= 18 or\
    value % 2 == 1 and value >= 19 and value <= 27 or\
    value % 2 == 0 and value >= 30 and value <= 36:
    print('Pay Red')
elif value == 0 or value == 37:
    pass
else:
    print('Pay Black')

if value >= 1 and value <= 36:
    if value % 2 == 1:
        print('Pay Odd')
    else:
        print('Pay Even')

if value >= 1 and value <= 18:
    print('Pay 1 to 18')
elif value >= 19 and value <= 36:
    print('Pay 19 to 36')    