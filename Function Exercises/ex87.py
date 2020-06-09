'''
Exercise 87: Center a String in the Terminal
Write a function that takes a string of characters as its first parameter, and the width of
the terminal in characters as its second parameter. Your function should return a new
string that consists of the original string and the correct number of leading spaces
so that the original string will appear centered within the provided width when it is
printed. Do not add any characters to the end of the string. Include a main program
that demonstrates your function.
'''

width = 150

def center(s, width):
    if width < len(s):
        return s

    whitespace = (width - len(s)) // 2
    result = ' ' * whitespace + s 
    return result

def main():
    print(center('This is us', width))
    print(center('How center is this?', width))
    
main()