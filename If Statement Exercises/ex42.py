'''
Exercise 42: Frequency To Note
In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other octaves.
'''

frequency = float(input('Enter a frequencyin Hertz to find the corresponding musical note note: '))

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if B4 - 1 <= frequency <= B4 + 1:
    note = 'B4'
elif A4 - 1 <= frequency <= A4 + 1:
    note = 'A4'
elif G4 - 1 <= frequency <= G4 + 1:
    note = 'G4'
elif F4 - 1 <= frequency <= F4 + 1:
    note = 'F4'
elif E4 - 1 <= frequency <= E4 + 1:
    note = 'E4'
elif D4 - 1 <= frequency <= D4 + 1:
    note = 'D4'
elif C4 - 1 <= frequency <= C4 + 1:
    note = 'C4'
else:
    print('Enter a valid frequency!')

print('The frequency {} corresponds to the musical note {}'. format(frequency, note))