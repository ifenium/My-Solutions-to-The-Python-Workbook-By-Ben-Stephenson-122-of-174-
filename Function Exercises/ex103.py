'''
Exercise 103: Magic Dates
A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 100 helpful when completing this exercise.
'''
# Days in a month(ex100)
def days(month, year):
    if year % 400 == 0 or year % 4 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    else:
        leap = False

    days_30  = [9,4,6,11]
    days_31 = [1,3,5,7,8,10]

    if leap == True and month == 2:
        return 29
    elif leap == False and month == 2:
        return 28
    elif month in days_30:
        return 30 
    elif month in days_31:
        return 31 


def magicdate(day, month, year):
    if  day * month  == year % 100:
        return True 
    return False

def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days(month, year) + 1):
                if magicdate(day, month, year):
                    print('{}/{}/{} is a magic year'. format(day, month, year))

main()  