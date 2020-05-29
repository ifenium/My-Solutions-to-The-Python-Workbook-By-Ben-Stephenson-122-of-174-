'''
Exercise 45: What Color is that Square?
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:
Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error checking.
'''

position = input('Enter your position on the chess board e.g.(a7): ').lower()

letter = position[0]
number = int(position[1])
white  = ['a','c','e','g']

if number % 2 == 0 and letter in white:
    print('You\'re on a White square.')
else:
    print('You\'re on a Black square.')