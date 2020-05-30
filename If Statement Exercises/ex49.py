'''
Exercise 49: Richter Scale
The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors:
Magnitude                   Descriptor
Less than 2.0               Micro
2.0 to less than 3.0        Very minor
3.0 to less than 4.0        Minor
4.0 to less than 5.0        Light
5.0 to less than 6.0        Moderate
6.0 to less than 7.0        Strong
7.0 to less than 8.0        Major
8.0 to less than 10.0       Great
10.0 or more                Meteoric
Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.
'''

magnitude = float(input('Enter te magnitude of the earthquake using Richter\'s scale: '))

if 2 < magnitude:
    des = 'Micro'
elif 2 <= magnitude < 3:
    des = 'Very minor'
elif 3 <= magnitude < 3:
    des = 'Minor'
elif 4 <= magnitude < 3:
    des = 'Light'
elif 5 <= magnitude < 3:
    des = 'Moderate'
elif 6 <= magnitude < 3:
    des = 'Strong'
elif 7 <= magnitude < 3:
    des = 'Major'
elif 8 <= magnitude < 3:
    des = 'Great'
elif 10 <= magnitude:
    des = 'Metroric'

print('A mangnitude {} earthquake is considered to be a a {} earthquake'. format(magnitude, des))