'''
Exercise 13: Making Change
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
'''

cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5

cents = int(input('Enter the number of cents:  '))

print(' ', cents // cents_per_toonie, 'toonies')
cents = cents % cents_per_toonie

print(' ', cents // cents_per_loonie, 'loonies')
cents = cents % cents_per_loonie

print(' ', cents // cents_per_quarter, 'quarter')
cents = cents % cents_per_quarter

print(' ', cents // cents_per_dime, 'dime')
cents = cents % cents_per_dime

print(' ', cents // cents_per_nickel, 'nickel')
cents = cents % cents_per_nickel	

print('', cents, 'pennies')