'''
Exercise 100: Days in a Month
Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 57 helpful when solving this problem.
'''

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

def main():
    month = int(input('Enter the month: '))
    year = int(input('Enter the year: '))
    print(days(month, year))

if __name__ == '__main__':
    main()