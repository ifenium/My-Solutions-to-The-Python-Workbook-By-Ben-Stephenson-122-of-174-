'''
Exercise 89: Capitalize It
Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. In this exercise, you will write a function that capitalizes
the appropriate characters in a string. A lowercase “i” should be replaced with an
uppercase “I” if it is both preceded and followed by a space. The first character in
the string should also be capitalized, as well as the first non-space character after a
“.”, “!” or “?”. For example, if the function is provided with the string “what time
do i have to be there? what’s the address?” then it should return the string “What
time do I have to be there? What’s the address?”. Include a main program that reads
a string from the user, capitalizes it using your function, and displays the result.
'''

def capitalize(s):
    result = s.replace(' i ', ' I ')

    if len(s) > 0:
        result = result[0].upper() + result[1 : len(result)]

    pos = 0
    while pos < len(s): 
        if result[pos] == '.' or result[pos] == '!' or result[pos] == '?':
            pos += 1
    
            while pos < len(s) and result[pos] == ' ':
                pos += 1

            if pos < len(s):
                result = result[0: pos] + result[pos].upper() + result[pos + 1 : len(result)]
        pos += 1 
    return result

def main():
    s = input('Enter sample text: ')
    print('You text capitalized is: {} '. format(capitalize(s)))

main()