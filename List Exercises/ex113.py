'''
Exercise 113: Formatting a List
When writing out a list of items in English, one normally separates the items with
commas. In addition, the word “and” is normally included before the last item, unless
the list only contains one item. Consider the following four lists:
apples
apples and oranges
apples, oranges and bananas
apples, oranges, bananas and lemons
Write a function that takes a list of strings as its only parameter. Your function
should return a string that contains all of the items in the list formatted in the manner
described previously as its only result. While the examples shown previously only
include lists containing four elements or less, your function should behave correctly
for lists of any length. Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the
function.
'''

def listformat(items):
    length = len(items)

    if length == 0:
        return 'Empty'
    elif length == 1:
        return str(items[0])
    
    results = ''
    for i in range(0, length - 2):
        results += str(items[i]) + ", "

    results = results + str(items[length - 2]) + ' and '
    results += str(items[length - 1]) 

    return results

def main():
    items = []
    line = input('Enter an item (Enter to cancel): ')
    while line != '':
        items.append(line)
        line = input('Enter an item (Enter to cancel): ')
    
    print('The items you entered are: {}'. format(listformat(items)))

main()