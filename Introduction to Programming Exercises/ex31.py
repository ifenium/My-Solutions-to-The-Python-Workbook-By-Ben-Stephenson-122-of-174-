'''
Exercise 31: Sum of the Digits in an Integer
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
'''

num = int(input('Enter your four digit number: '))
num_list = list(map(int, str(num)))
summation = sum(num_list)

print('{} + {} + {} + {} = {}'. format(num_list[0], num_list[1], num_list[2], num_list[3], summation))