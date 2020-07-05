'''
Exercise 120: Is a List already in Sorted Order?
Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is
already sorted. Otherwise it should return False. Write a main program that reads
a list of numbers from the user and then uses your function to report whether or not
the list is sorted.
Make sure you consider these questions when completing this exercise: Is a
list that is empty in sorted order? What about a list containing one element?
'''

def sortorder(n):
    if len(n) <= 2:
        value True
    elif n == sorted(n):
        value = True
    else:
        value = False
    
    print(value)

def main():
    n = input('Enter some integers and separate with a comma: ').split(',')
    n = list(map(int, n))
    sortorder(n)

if __name__ == '__main__':
    main()