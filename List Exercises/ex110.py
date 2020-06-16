'''
Exercise 110: Perfect Numbers
An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your function will return true. 
Otherwise it will return false. In addition, write a main program
that uses your function to identify and display all of the perfect numbers between 1
and 10,000. Import your solution to Exercise 109 when completing this task.
'''

# Function from Exercise 109
def properdivs(n):
    divs = []
    for i in range(1, n-1):
        if n % i == 0:
            divs.append(i)
    return divs

def perfectnumber(n):
    a = properdivs(n)
    if sum(a) == n:
        return True
    
    return False

perfect_numbers = []
def main():
    for i in range(1,10000):
        if perfectnumber(i): 
            perfect_numbers.append(i)
            i += 1
        else: 
            i += 1

    print('The Perfect numbers between 1 and 10,000 are: ')
    for j in perfect_numbers:
        print(j)

if __name__ == '__main__':
    main()