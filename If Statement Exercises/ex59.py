'''
Exercise 59: Is a License Plate Valid?
In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers. When all of the license plates following that pattern had
been used, the format was changed to four numbers followed by three uppercase letters.
Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate.
'''

plate = input('Enter the license plate: ').upper()

if len(plate) == 6 and 'A' <= plate[0] <= 'Z' and \
    'A' <= plate[1] <= 'Z' and 'A' <= plate[2] <= 'Z' and \
    '0' <= plate[3] <= '9' and '0' <= plate[4] <= '9' and \
    '0' <= plate[5] <= '9':
    print('This is valid for the old plate style.')
elif len(plate) == 7 and  '0' <= plate[0] <= '9' and \
    '0' <= plate[1] <= '9' and '0' <= plate[2] <= '9' and \
    '0' <= plate[3] <= '9' and 'A' <= plate[4] <= 'Z' and \
    'A' <= plate[5] <= 'Z' and 'A' <= plate[6] <= 'Z':
        print('This is valid for the new plate style.')
else:
    print('This license plate is invalid.')