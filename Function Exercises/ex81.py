'''
Exercise 81: Compute the Hypotenuse
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.
'''

from math import sqrt

def hypotenuse(adjacent, opposite):
    hypotenue = sqrt(adjacent ** 2 + opposite ** 2)
    return hypotenue

def main():   
    adjacent = float(input('Enter the adjacent side of the Right angled triangle: '))
    opposite = float(input('Enter the opposite side of the Right angled triangle: '))

    print('The Hypotenuse(longest side) of the right angled triangle is: {:.2f}'. format(hypotenuse(adjacent,opposite)))

main()
