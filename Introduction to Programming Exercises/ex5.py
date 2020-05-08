'''
Exercise 5: Bottle Deposits
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places
'''

less_deposit = 0.10
more_deposit = 0.25

less = float(input('How many drink containers holding one liter or less do you have? '))
more = float(input('How many drink containers holding more than one liter do you have? '))

refund = less_deposit * less + more_deposit * more

print('Your total refund will be $%.2f.' % refund)