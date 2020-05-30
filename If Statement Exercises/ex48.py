'''
Exercise 48: Chinese Zodiac
The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare.
Year Animal
2000 Dragon
2001 Snake
2002 Horse
2003 Sheep
2004 Monkey
2005 Rooster
2006 Dog
2007 Pig
2008 Rat
2009 Ox
2010 Tiger
2011 Hare
Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.
'''

year = int(input('What year is it? '))
if year >= 0:
    if year % 12 == 8:
        print('Year of the Dragon')
    elif year % 12 == 9: 
        print('Year of the  Snake')
    elif year % 12 == 10: 
        print('Year of the  Horse')
    elif year % 12 == 11: 
        print('Year of the  Sheep')
    elif year % 12 == 0: 
        print('Year of the  Monkey')
    elif year % 12 == 1: 
        print('Year of the  Rooster')
    elif year % 12 == 2: 
        print('Year of the  Dog')
    elif year % 12 == 3: 
        print('Year of the  Pig')
    elif year % 12 == 4: 
        print('Year of the Rat')
    elif year % 12 == 5: 
        print('Year of the  Ox')
    elif year % 12 == 6: 
        print('Year of the Tiger')
    elif year % 12 == 7: 
        print('Year of the Hare')
else:
    print ('Enter a valid year greater than or equals to 0')s