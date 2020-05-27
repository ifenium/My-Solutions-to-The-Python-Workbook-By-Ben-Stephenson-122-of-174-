'''
Exercise 32: Sort 3 Integers
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
'''

num = input('Enter your three integers separated by a comma(,): ')

num_list = list(map(int,num.split(',')))
summation = sum(num_list)
maximum = max(num_list)
minimum = min(num_list)
middle  = summation - maximum - minimum
 
print('Sorting the numbers {},{},{} you entered  from smallest to largest is {},{},{} '. \
    format(num_list[0], num_list[1], num_list[2],minimum, middle, maximum))