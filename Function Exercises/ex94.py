'''
Exercise 94: Random Password
Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters. Each character should be randomly
selected from positions 33 to 126 in the ASCII table. Your function will not take
any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file.
Hint: You will probably find the chr function helpful when completing this
exercise. Detailed information about this function is available online.
'''

def randompassword():
    from random import randint 
    maximum = 10
    minimum = 7
    password_range = randint(minimum, maximum)
    generated = ''
    
    for i in range(password_range):
        randomchar = chr(randint(33,126))
        generated += randomchar
    return generated

def main():
    print('{} is your randomized passoword'. format(randompassword()))

if __name__ == '__main__':
    main()