'''
Exercise 112: Below and Above Average
Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.
'''

values = []
lower = []
higher = []

line = input('Enter an integer (blank line to quit): ')
while line != '':
    line = int(line)
    values.append(line)

    line = input('Enter an integer (blank line to quit): ')

mean = round(sum(values) / len(values))

for i in values:
    if i > mean:
        higher.append(i)
    if i < mean:
        lower.append(i)

print('The average of the values entered is {}'. format(mean))
print('The value(s) below the average is(are) {}'. format(lower))
print('The value(s) above the average is(are) {}'. format(higher))
