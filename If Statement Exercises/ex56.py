'''
Exercise 56: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.
Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.
'''

call = int(input('How much time in minutes did you spend on calls this month: '))
text = int(input('How many text messages did you send this month: '))

base = 15 
fee_911 = 0.44
extra_call = call - 50
extra_text = text - 50 
extra_call_charge = 0.25 * extra_call  
extra_text_charge = 0.15 * extra_text
subtotal = base + fee_911 + extra_call_charge + extra_text_charge 
tax = 0.05 * subtotal
total = tax + subtotal

if call <= 50 and text <= 50:
    print('Base charge: {:.2f} \n911 fee: {:.2f}\nTax(5%): {:.2f} \nTotal: {:.2f}'. format(base, fee_911, tax, total))
if call > 50 and text > 50:
    print('Base charge: {:.2f} \nAdditional minutes charge: {:.2f} \nAdditional text message charge: {:.2f}\
        \n911 fee: {:.2f}\nTax(5%): {:.2f} \nTotal: {:.2f}'. format(base, extra_call_charge, extra_text_charge, fee_911, tax, total))    