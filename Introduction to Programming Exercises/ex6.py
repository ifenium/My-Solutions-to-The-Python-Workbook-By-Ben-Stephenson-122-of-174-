'''
Exercise 6:Tax and Tip 
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places
'''
meal = float(input('What was the cost of your meal: '))

tax = 0.075 * meal
tip = 0.18 * meal 
grand_total = tax +  tip + meal

print('Tax $%.2f' % tax)
print('Tip $%.2f' % tip)
print('Grand Total $%.2f' % grand_total)

'''
# or 
print('Tax is ${:.2f}, Tip is ${:.2f} and the Grand Total is ${:.2f}'. format(round(tax,2),round(tip,2),round(grand_total,2)))
'''