'''
Exercise 83: Shipping Calculator
An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item, and $2.95 for each subsequent item. Write a function that takes the
number of items in the order as its only parameter. Return the shipping charge for
the order as the function’s result. Include a main program that reads the number of
items purchased from the user and displays the shipping charge.
'''

def shippingcalculator(items):
    base = 10.95
    if items == 1:
        cost = base
    elif items == 0:
        cost = 0 
    else:
        extra = items - 1
        cost = base + extra * 2.95
    return cost

def main():
    items = int(input('Enter the number of items bought: '))
    print('The shipping cost for {} items bought is {:.2f}'. format(items, shippingcalculator(items)))

main()