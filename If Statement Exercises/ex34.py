'''
Exercise 34: Even or Odd?
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.
'''

num = int(input('Enter an integer: '))

if num % 2 == 0:
    print('The integer {} is even'. format(num))
else:
    print('The integer {} is odd'. format(num))