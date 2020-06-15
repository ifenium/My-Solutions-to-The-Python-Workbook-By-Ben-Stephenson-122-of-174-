'''
Exercise 99: Arbitrary Base Conversions
Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and
the result number. If the user chooses a base outside of this range then an appropriate
error message should be displayed and the program should exit. Divide your program
into several functions, including a function that converts from an arbitrary base to
base 10, a function that converts from base 10 to an arbitrary base, and a main
program that reads the bases and input number from the user. You may find your
solutions to Exercises 77, 78 and 98 helpful when completing this exercise.
'''

#  Functions from Exercise 98
def hex2int(s):
    s = str(s)
    integer = int(s,16)
    return integer

def int2hex(n):
    n = int(n)
    hexadecimal = hex(n)
    return hexadecimal

def decimaltothers(number, base):
    result = ''
    q = number

    r = q % base
    result  += int2hex(r)
    q //= base

    while q > 0:
        r = q % base
        result += int2hex(r)
        q //= base
    
    return result 

def otherstodecimal(number, base):
    decimal = 0     
    power = 10

    for i in range(len(number)):
        decimal *= base
        decimal += hex2int(number[i])

    return decimal

def main():
    from_base = int(input('Enter the base you want to convert from: '))
    from_number = input('Enter the digits of the number in that base: ')
    dec = otherstodecimal(from_number, from_base)
    print('{} is {} in base 10'. format(from_number, dec))

    to_base = int(input('Enter the base to convert to: '))
    to_num = decimaltothers(dec,to_base)
    print('That\'s {} in base {}'. format(to_num, to_base))

if __name__ == '__main__':
    main()