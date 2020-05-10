'''
Exercise 10: Arithmetic
Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10a
• The result of a^b
'''

from math import log10

a = int(input('Please enter your first number: '))
b = int(input('Please enter your first number: '))

print('The sum of {} and {} is {}'. format(a, b, a+b))
print('The difference between {} and {} is {}'. format(a, b, a-b))
print('The product of {} and {} is {}'. format(a, b, a*b))
print('The quotient when {} is divided by {} is {}'. format(a, b, a//b))
print('The remainder when {} is divided by {} is {}'. format(a, b, a%b))
print('The result when the logarithm of {} is taken is {}'. format(a,log10(a)))
print('The result when {} is raised to the power of {} is {}'. format(a,b,a**b))