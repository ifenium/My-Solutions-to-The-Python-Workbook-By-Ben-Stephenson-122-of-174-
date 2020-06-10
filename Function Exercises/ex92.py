'''
Exercise 92: Is a Number Prime?
A prime number is an integer greater than 1 that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.
'''

def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def main():
    n = int(input('Enter an integer: '))
    if prime(n):
        print('{}  is a prime number'. format(n))
    else:
        print('{} is not a prime number'. format(n))

if __name__ == '__main__':
    main()