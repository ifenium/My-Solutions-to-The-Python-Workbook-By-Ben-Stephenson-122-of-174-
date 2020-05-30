'''
Exercise 47: Birth Date to Astrological Sign
The horoscopes commonly reported in newspapers use the position of the sun at the
time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:
Zodiac sign                 Date range
Capricorn                   December 22 to January 19
Aquarius                    January 20 to February 18
Pisces                      February 19 to March 20
Aries                       March 21 to April 19
Taurus                      April 20 to May 20
Gemini                      May 21 to June 20
Cancer                      June 21 to July 22
Leo                         July 23 to August 22
Virgo                       August 23 to September 22
Libra                       September 23 to October 22
Scorpio                     October 23 to November 21
Sagittarius                 November 22 to December 21
Write a program that asks the user to enter his or her month and day of birth. Then 
your program should report the user’s zodiac sign as part of an appropriate output
message.
'''

month = input('Enter your birth month: ').lower()
day = int(input('Enter your day of the birth: '))

if month == 'december' and 22 <= day <= 31 or month == 'january' and 1 <= day <= 19:
    print('Your zodiac sign is Capricon')
elif month == 'january' and  20 <= day <= 31 or month == 'february' and 1 <= day <= 18:
    print('Your zodiac sign is Aquarius ')
elif month == 'february' and  19 <= day <= 29 or month == 'march' and 1 <= day <= 20:
    print('Your zodiac sign is Pisces')
elif month == 'march' and  21 <= day <= 31 or month == 'april' and 1 <= day <= 19:
    print('Your zodiac sign is Aries')
elif month == 'april' and  20 <= day <= 30 or month == 'may' and 1 <= day <= 20:
    print('Your zodiac sign is Taurus')
elif month == 'may' and  21 <= day <= 31 or month == 'june' and 1 <= day <= 20:
    print('Your zodiac sign is Gemini')
elif month == 'june' and  21 <= day <= 30 or month == 'july' and  1 <= day <= 22 :
    print('Your zodiac sign is Cancer')
elif month == 'july' and  23 <= day <= 31 or month == 'august' and 1 <= day <= 22:
    print('Your zodiac sign is Leo')
elif month == 'august' and  23 <= day <= 31 or month == 'september' and 1 <= day <= 22:
    print('Your zodiac sign is Virgo')
elif month == 'september' and  23 <= day <= 30 or month == 'october' and 1 <= day <= 22:
    print('Your zodiac sign is Libra')
elif month == 'october' and  23 <= day <= 31 or month == 'november' and 1 <= day <= 21:
    print('Your zodiac sign is Scorpio')
elif month == 'november' and  22 <= day <= 30 or month == 'december' and 1 <= day <= 21:
    print('Your zodiac sign is  Sagittarius')