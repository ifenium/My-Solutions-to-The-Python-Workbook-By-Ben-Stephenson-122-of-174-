'''
Exercise 85: Convert an Integer to its Ordinal Number
Words like first, second and third are referred to as ordinal numbers. In this exercise,
you will write a function that takes an integer as its only parameter and returns a
string containing the appropriate English ordinal number as its only result. Your
function must handle the integers between 1 and 12 (inclusive). It should return an
empty string if a value outside of this range is provided as a parameter. Include a
main program that demonstrates your function by displaying each integer from 1 to
12 and its ordinal number. Your main program should only run when your file has
not been imported into another program.
'''

def int_ordinal(num):
    if num <= 0 or num > 12:
        return ''
    else:
        if num == 1:
            return 'First'
        elif num == 2:
            return 'Second'
        elif num == 3:
            return 'Third'
        elif num == 4:
            return 'Fourth'
        elif num == 5:
            return 'Fifth'
        elif num == 6:
            return 'Sixth'
        elif num == 7:
            return 'Seventh'
        elif num == 8:
            return 'Eighth'
        elif num == 9:
            return 'Ninth'
        elif num == 10:
            return 'Tenth'
        elif num == 11:
            return 'Eleventh'
        elif num == 12:
            return 'Twelfth'

def main():
    num = int(input('Enter an integer: '))
    print('The Integer {} represented in ordinal number is {}'. format(num, int_ordinal(num)))

main()