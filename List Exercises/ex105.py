'''
Exercise 105: Reverse Order
Write a program that reads integers from the user and stores them in a list. Use 0 as
a sentinel value to mark the end of the input. Once all of the values have been read
your program should display them (except for the 0) in reverse order, with one value
appearing on each line.
'''


num_list = []
num = int(input('Enter an integer (0 to quit): '))

while num != 0:
    num_list.append(num)
    num = int(input('Enter an integer (0 to quit): '))

num_list.reverse()

print('The integers sorted in ascending order are:') 
for i in num_list:
    print(i)