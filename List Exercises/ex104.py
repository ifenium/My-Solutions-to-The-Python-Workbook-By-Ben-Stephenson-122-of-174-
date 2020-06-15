'''
Exercise 104: Sorted Order
Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in order from smallest to largest,
with one value appearing on each line. Use either the sort method or the sorted
function to sort the list.
'''

num_list = []
num = int(input('Enter an integer (0 to quit): '))

while num != 0:
    num_list.append(num)
    num = int(input('Enter an integer (0 to quit): '))

num_list.sort()

print('The integers sorted in ascending order are:') 
for i in num_list:
    print(i)
