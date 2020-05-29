'''
Exercise 41: Note To Frequency
The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.
Note Frequency (Hz)
C4      261.63
D4      293.66
E4      329.63
F4      349.23
G4      392.00
A4      440.00
B4      493.88
'''

note_name = input('Enter the musical note name (e.g. C4): ').upper()

note = note_name[0]
octave = int(note_name[1])

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

if note  == 'C':
    frequency = C4
elif note == 'D':
    frequency = D4
elif note == 'E':
    frequency = E4
elif note == 'F':
    frequency = F4
elif note == 'G':
    frequency = G4
elif note == 'A':
    frequency = A4
elif note == 'B':
    frequency = B4
else:
    print('Enter a valid musical note')

frequency =  frequency / 2  ** (4 - octave)
print('The musical note {} corresponds to the frequency {}'. format(note_name, frequency))