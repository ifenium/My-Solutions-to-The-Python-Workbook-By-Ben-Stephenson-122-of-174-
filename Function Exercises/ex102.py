'''
Exercise 102: Reduce Measures
Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
of ingredients used when cooking or baking. While such recipes are easy enough to
follow if you have the appropriate measuring cups and spoons, they can be difficult
to double, triple or quadruple when cooking Christmas dinner for the entire extended
family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
tablespoons when quadrupled. However, 16 tablespoons would be better expressed
(and easier to measure) as 1 cup.
Write a function that expresses an imperial volume using the largest units possible. 
The function will take the number of units as its first parameter, and the unit
of measure (cup, tablespoon or teaspoon) as its second parameter. Return a string
representing the measure using the largest possible units as the function’s only result.
For example, if the function is provided with parameters representing 59 teaspoons
then it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.
Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to 3 teaspoons.
'''

def reducemeasure(n, unit):
    unit = unit.lower()
    n = int(n)
    
    tablespoon_teaspoon = 3
    cup_teaspoon = 16 * 3

    if unit == 'teaspoon' or unit == 'teaspoons':
        teaspoons = n 
    elif unit == 'tablespoon' or unit == 'tablespoons':
        teaspoons = n * tablespoon_teaspoon
    elif unit == 'cup' or unit == 'cups':
        teaspoons = n * cup_teaspoon

    cups =  teaspoons // cup_teaspoon
    teaspoons = teaspoons - cups * cup_teaspoon
    tablespoons = teaspoons // tablespoon_teaspoon
    teaspoons = teaspoons - tablespoons * tablespoon_teaspoon

    result = ''
    
    if cups > 0:
        result += str(cups) + ' cup'
        if cups > 1:
            result += 's'
    
    if tablespoons > 0:
        if result != '':
            result += ', '
        result += str(tablespoons) + ' tablespoon'
        if tablespoons > 1:
            result += 's'

    if teaspoons > 0:
        if result != '':
            result += ', '
        result += str(teaspoons) + ' teaspoon'
        if teaspoons > 1:
            result += 's'
    
    if result == '':
        result = '0 teaspoons'

    return result

def main():
    print('100 teaspoon is {}'. format(reducemeasure(100, 'teaspoon' )))

if __name__ == '__main__':
    main()