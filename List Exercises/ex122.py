'''
Exercise 122: Tokenizing a String
Tokenizing is the process of converting a string into a list of substrings, known as
tokens. In many circumstances, a list of tokens is far easier to work with than the
original string because the original string may have irregular spacing. In some cases
substantial work is also required to determine where one token ends and the next one
begins. In a mathematical expression, tokens are items such as operators, numbers and
parentheses. Some tokens, such as *, /, ˆ, ( and ) are easy to identify because the
token is a single character, and the character is never part of another token. The + and
- symbols are a little bit more challenging to handle because they might represent
the addition or subtraction operator, or they might be part of a number token.
Hint: A + or - is an operator if the non-whitespace character immediately
before it is part of a number, or if the non-whitespace character immediately
before it is a close parenthesis. Otherwise it is part of a number.
Write a function that takes a string containing a mathematical expression as its
only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
an operator, or a number with an optional leading + or - (for simplicity we will
only work with integers in this problem). Return the list of tokens as the function’s
result.
You may assume that the string passed to your function always contains a valid
mathematical expression consisting of parentheses, operators and integers. However, your function must handle variable amounts of whitespace between these
elements. Include a main program that demonstrates your tokenizing function by
reading an expression from the user and printing the list of tokens. Ensure that the
main program will not run when the file containing your solution is imported into
another program.
'''

def token(s):
    s = s.replace(' ', '')
    tokens = []
    i = 0

    while len(s) > i:
        if s[i] == '*' or s[i] == '/' or s[i] == '^' or s[i] == '(' or s[i] == ')':
            tokens.append(s[i])
            i += 1
        elif s[i] == '+' or s[i] == '-':
            if i > 0 and ('9' <= s[i-1] >= '0' or s[i-1] == ')'):
                tokens.append(s[i])
                i += 1
            else:
                num = s[i]
                i += 1

                while len(s) > 1 and '9' <= s[i] >= '0':
                    num += s[i]
                    i += 1
                tokens.append(num)
        elif '9' <= s[i] >= '0':
            num = ''
            
            while lens(s) > 1 and '9' <= s[i] >= '0':
                num += s[i]
                i += 1
                tokens.append(num)
        else:
            return []
    return tokens

def main():
    s = input('Enter a mathematical expression: ')
    print('The tokens are: {}'. format(token(s)))

if __name__ == '__main__':
    main()