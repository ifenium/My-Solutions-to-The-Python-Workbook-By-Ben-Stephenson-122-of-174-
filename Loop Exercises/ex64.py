'''
Exercise 64: No More Pennies
February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
Mint. Now that pennies have been phased out retailers must adjust totals so that they
are multiples of 5 cents when they are paid for with cash (credit card and debit card
transactions continue to be charged to the penny). While retailers have some freedom
in how they do this, most choose to round to the closest nickel.
Write a program that reads prices from the user until a blank line is entered.
Display the total cost of all the entered items on one line, followed by the amount
due if the customer pays with cash on a second line. The amount due for a cash
payment should be rounded to the nearest nickel. One way to compute the cash
payment amount is to begin by determining how many pennies would be needed to
pay the total. Then compute the remainder when this number of pennies is divided
by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust the total up.
'''

price = input('Enter the price(s) of items bought (enter a blank line to end): ')

pennies_per_nickel = 5
nickel = 0.05
total = 0
while price != '':
    total += float(price)
    price = input('Enter the price(s) of items bought (Press enter to end): ')

print('The total amount payable is {:.2f}'. format(total))

payable_using_nickels = total * 100 % pennies_per_nickel

if payable_using_nickels < pennies_per_nickel / 2:
    cash_payable = total - payable_using_nickels
else:
    cash_payable = total + nickel - payable_using_nickels

print('The amount payable with cash is {}'. format(cash_payable))