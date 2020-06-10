'''
Exercise 95: Random License Plate
In a particular jurisdiction, older license plates consist of three letters followed by
three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.
'''

def randomplatenumber():
    from random import randint
    number = ''
    letter = ''
    while len(number) <= 4 and len(letter) <= 3:
        number += str(randint(0, 9))
        letter += chr(randint(97, 123))

    return number + letter

def main():
    print('{} is your randomly generated license plate'. format(randomplatenumber()))

if __name__ == '__main__':
    main()