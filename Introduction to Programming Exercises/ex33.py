'''
Exercise 33: Day Old Bread
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
'''

n = int(input('How much "day old bread" did you purchase: '))
original_price = 3.49
discount = original_price * 0.6
total_price = n * (original_price - discount)

print('The regular price for {} bread(s) is {:.2f}'. format(n,  n*original_price))
print('The discount given is {:.2f}'. format(discount))
print('Total price: {:.2f}'. format(total_price))