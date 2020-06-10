'''
Exercise 93: Next Prime
In this exercise you will create a function named nextPrime that finds and returns
the first prime number larger than some integer, n. The value of n will be passed to
the function as its only parameter. Include a main program that reads an integer from
the user and displays the first prime number larger than the entered value. Import
and use your solution to Exercise 92 while completing this exercise.
'''
# Previous Function (ex92.py)
def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
        
def nextprime(n):
    found = False
    while (not found):
        n += 1
        if prime(n):
            found = True
    return n

def main():
    n = int(input('Enter an integer: '))
    print('{} is the next prime after the integer {}'. format(nextprime(n), n))

if __name__ == '__main__':
    main()