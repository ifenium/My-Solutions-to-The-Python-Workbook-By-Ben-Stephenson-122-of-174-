'''
Exercise 39: Sound Levels
The following table lists the sound level in decibels for several common noises.
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
'''

level = int(input('Enter the sound level in decibels(dB): '))

if level  == 130:
    print('That\'s sounds like a Jackhammer.')
elif level == 106: 
    print('That\'s sounds like a Gas Lawnmower.')
elif level == 70:
    print('That\'s sounds like an Alarm clock.')
elif level == 40:
    print('That\'s sounds like a Quiet room.')
elif  40 < level < 70:
    print('That sounds resides between a Quiet room and an Alarm clock.')
elif 70 < level < 106:
    print('That sounds resides between an Alarm clock and a Gas Lawnmower.') 
elif 106 < level < 130:
    print('That sounds resides between a Gas Lawnmower and a Jackhammer.')
elif level > 130:
    print('That\'s not bearable sound, turn it off or down.')
elif level < 40:
    print('That\'s realy quiet, you should sleep just fine.')