'''
Exercise 86: The Twelve Days of Christmas
The Twelve Days of Christmas is a repetitive song that describes an increasingly
long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
the first day. A new gift is added to the collection on each additional day, and then
the complete collection is sent. The first three verses of the song are shown below.
The complete lyrics are available on the internet.

On the first day of Christmas
my true love sent to me:
A partridge in a pear tree.
On the second day of Christmas
my true love sent to me:
Two turtle doves,
And a partridge in a pear tree.
On the third day of Christmas
my true love sent to me:
Three French hens,
Two turtle doves,
And a partridge in a pear tree.

Your task is to write a program that displays the complete lyrics for The Twelve
Days of Christmas. Write a function that takes the verse number as its only parameter
and displays the specified verse of the song. Then call that function 12 times with
integers that increase from 1 to 12.
Each item that is sent to the recipient in the song should only appear once in your
program, with the possible exception of the partridge. It may appear twice if that
helps you handle the difference between “A partridge in a pear tree” in the first verse
and “And a partridge in a pear tree” in the subsequent verses. Import your solution
to Exercise 85 to help you complete this exercise.
'''

# Previous Function (ex86.py)
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

def verse(n):
    print('On the {} day of Christmas'. format(int_ordinal(n))) 
    print('my true love sent to me: ')
    
    if n >= 12:
        print('12 drummers drumming')
    elif n >= 11:
        print('11 pipers piping')
    elif n >= 10:
        print('10 lords a-leaping')
    elif n >= 9:
        print('Nine ladies dancing')
    elif n >= 8:
        print('Eight maids a-milking')
    elif n >= 7:
        print('Seven swans a-swimming')
    elif n >= 6:
        print('Six geese a-laying')
    elif n >= 5:
        print('Five golden rings')
    elif n >= 4:
        print('Four calling birds')
    elif n >= 3:
        print('Three french hens')
    elif n >= 2:
        print('Two turtle doves, and')
    elif n == 1:
        print('A partridge in a pear tree')

def main():
    for i in range(1,13):
        verse(i)

main()