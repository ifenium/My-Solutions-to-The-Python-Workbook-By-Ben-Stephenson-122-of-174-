'''
Exercise 55: Frequency to Name
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:
Name                        Frequency range (Hz)
Radio waves                 Less than 3 × 109
Microwaves                  3 × 109 to less than 3 × 1012
Infrared light              3 × 1012 to less than 4.3 × 1014
Visible light               4.3 × 1014 to less than 7.5 × 1014
Ultraviolet light           7.5 × 1014 to less than 3 × 1017
X-rays                      3 × 1017 to less than 3 × 1019
Gamma rays                  3 × 1019 or more
Write a program that reads the frequency of the radiation from the user and displays
the appropriate name.
'''

frequency = float(input('Enter the frequency of the electromagnetic radiation in Hertz(Hz): '))

if frequency <= 3 * 10e9:
    name = 'Radio Wave'
elif 3 * 10e9 <= frequency <= 3 * 10e12:
    name = 'Microwaves'
elif 3 * 10e12 <= frequency <= 4.3 * 10e14:
    name = 'Infrared Light'
elif 4.3 * 10e14 <= frequency <= 7.5 * 10e14:
    name = 'Visible light'
elif 7.5 * 10e14 <= frequency <= 3 * 10e17:
    name = 'Ultraviolet light'
elif 3 * 10e19 <= frequency <= 3 * 10e19:
    name = 'X-rays'
elif frequency >= 3 * 10e19:
    name = 'Gamma rays'
else:
    name = 'null'

if name == 'null':
    print('')
else:
    print('That frequency {} nm corresponds to {}'. format(frequency, name))