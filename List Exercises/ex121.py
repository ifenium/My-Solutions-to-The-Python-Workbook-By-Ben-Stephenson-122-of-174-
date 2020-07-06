'''
Exercise 121: Count the Elements
Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create a new
function named countRange which determines and returns the number of elements
within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum
value and the maximum value. It will return an integer result greater than or equal to
0. Include a main program that demonstrates your function for several different lists,
minimum values and maximum values. Ensure that your program works correctly
for both lists of integers and lists of floating point numbers.
'''

def countRange(l, minimum, maximum):
    count = 0 
    
    for i in l:
        if minimum <= i < maximum:
            count += 1
        
    return count 

def main():
    l = [1,2,3,4,5,5,6,77,8,2,46]
    maximum = float(input('Enter the maximum number: '))
    minimum = float(input('Enter the minimum number: '))
    m = countRange(l, minimum, maximum)
    print('Counting the elements in {} that are between {} and {} are: {}'. format(l, minimum, maximum, m))


if __name__ == '__main__':
    main()