'''
Exercise 98: Hexadecimal and Decimal Digits
Write two functions, hex2int and int2hex, that convert between hexadecimal
digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and base 10 integers. The
hex2int function is responsible for converting a string containing a single hexadecimal digit to a base 10 integer,
while the int2hex function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit.
Each function will take the value to convert as its only parameter and return the converted value
as the function’s only result. Ensure that the hex2int function works correctly for
both uppercase and lowercase letters. Your functions should end the program with a
meaningful error message if an invalid parameter is provided.
'''

def hex2int(s):
    s = str(s)
    integer = int(s,16)
    print('The equivalent decimal value is {}'. format(integer))

def int2hex(n):
    n = int(n)
    hexadecimal = hex(n)
    print('The quivalent hexadecimal value is {}'. format(hexadecimal[2:]))