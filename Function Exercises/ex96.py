'''
Exercise 96: Check a Password
In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters
long and contains at least one uppercase letter, at least one lowercase letter, and at
least one number. Your function should return true if the password passed to it as
its only parameter is good. Otherwise it should return false. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure
that your main program only runs when your solution has not been imported into
another file.
'''

def passwordchecker(s):
    number = False 
    lower = False
    upper = False

    for i in s:
        if 'A' <= i <= 'Z':
            upper = True 
        elif 'a' <= i <= 'z': 
            lower = True
        elif '0' <= i <= '9':
            number = True 
        
    if len(s) >= 8 and number and lower and upper:
        return True
    else:
        return False

def main():
    s = input('Enter your password: ')
    if passwordchecker(s):
        print('Your password is a good one.')
    else:
        print('Your password is not a good one.')

if __name__ == '__main__':
    main()