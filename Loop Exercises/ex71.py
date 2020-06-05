'''
Exercise 71: Square Root
Write a program that implements Newton’s method to compute and display the square
root of a number entered by the user. The algorithm for Newton’s method follows:
Read x from the user Initialize guess to x/2 While guess is not good enough do
Update guess to be the average of guess and x/guess
When this algorithm completes, guess contains an approximation of the square
root. The quality of the approximation depends on how you define “good enough”.
In the author’s solution, guess was considered good enough when the absolute value
of the difference between guess ∗ guess and x was less than or equal to 10−12. 
'''

num = float(input('Enter number to find sqaure root: '))

initial = num / 2

while abs(initial * initial - num) >= 10e-20:
    initial = (initial + num / initial) / 2
    print('The square root of {} is {}'. format(num, initial))