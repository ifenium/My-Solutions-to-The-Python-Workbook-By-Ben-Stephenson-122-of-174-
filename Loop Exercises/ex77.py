'''
Exercise 77: Binary to Decimal
Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.
'''

binary = input('Enter an binary number(base 2): ')

decimal =  0
for i in binary:
    decimal = int(i) +  decimal * 2
    
print('{} in decimal is {}'. format(binary, decimal))

''' or 
binary = input('Enter an binary number(base 2): ')

decimal = []
for i, c in enumerate(binary[::-1]):
    decimal.append(int(c) * (2 ** i))

print('{} in decimal is {}'. format(binary, sum(decimal)))
'''