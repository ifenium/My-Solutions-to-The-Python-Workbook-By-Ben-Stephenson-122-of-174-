'''
Exercise 106: Remove Outliers
When analysing data collected as part of a science experiment it may be desirable
to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the
n smallest elements removed. Then it should return the new copy of the list as the
function’s only result. The order of the elements in the returned list does not have to
match the order of the elements in the original list.
Write a main program that demonstrates your function. Your function should read
a list of numbers from the user and remove the two largest and two smallest values
from it. Display the list with the outliers removed, followed by the original list. Your
program should generate an appropriate error message if the user enters less than 4
values.
'''

def removeoutiers(list1, outliers):
    list2 = sorted(list1)

    for i in range(2):
        list2.pop()

    for i in range(2):
        list2.pop(0)
    
    return list2

def main():
    list1 = []
    line = input('Enter a value (blank to quit): ')

    while line != '':
        line = float(line)
        list1.append(line) 
        line = input('Enter a value (blank to quit): ')

    if len(list1) < 4:
        print('You need more than 4 values')
    else:
        print('The original list with outliers removed is: {}'. format(removeoutiers(list1, 2)))
        print('The original values are: {}'. format(list1))

if __name__ == '__main__':
    main()