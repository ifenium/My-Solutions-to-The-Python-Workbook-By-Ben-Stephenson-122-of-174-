'''
Exercise 114: Random Lottery Numbers
In order to win the top prize in a particular lottery, one must match all 6 numbers
on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
organizer. Write a program that generates a random selection of 6 numbers for 
lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
Display the numbers in ascending order.
'''

from random import randrange

ticket_numbers = []
rand = randrange(1,50)

for i in range(6):
    rand = randrange(1, 50)
    while rand in ticket_numbers:
        rand = randrange(1, 50)
    
    ticket_numbers.append(rand)

ticket_numbers.sort()

print('Your Ticket numbers are:')
for i in ticket_numbers:
    print(i)