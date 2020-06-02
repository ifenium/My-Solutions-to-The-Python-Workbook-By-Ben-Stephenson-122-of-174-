'''
Exercise 61: Average
In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.
'''

numbers = input('To find the average, enter numbers separated by a comma(,) then 0 as the sentinel input: ').split(',')
numbers = list(map(int,numbers))

if numbers[-1] == 0:
    summation = 0
    for i in numbers:
        summation += i
        average = summation / (len(numbers) - 1)
    print('The average of those numbers is {:.2f}'. format(average))
elif numbers[0] == 0:
    print('"0" can\'t be used as the first number')
else:
    print('You\'re mean to end the list with "0"')
