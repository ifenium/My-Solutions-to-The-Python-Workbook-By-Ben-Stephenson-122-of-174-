'''
Exercise 84: Median of Three Values
Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median.
'''

def median(a, b, c):
    return a+b+c - min(a,b,c) - max(a,b,c)

def main():
    a = float(input('Enter the first value: '))
    b = float(input('Enter the second value: '))
    c = float(input('Enter the third value: '))

    print('The median value of {},{},{} is {}'. format(a, b, c, median(a,b,c) ))

main()