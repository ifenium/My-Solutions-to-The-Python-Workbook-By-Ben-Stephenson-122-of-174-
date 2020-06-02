'''
Exercise 63:Temperature Conversion Table
Write a program that displays a temperature conversion table for degrees Celsius and
degrees Fahrenheit. The table should include rows for all temperatures between 0
and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
headings on your columns. The formula for converting between degrees Celsius and
degrees Fahrenheit can be found on the internet.
'''


for i in range(101):
    print('Celsius(C)   Fahrenheit(F)')
    fahrenheit = 32 + 1.8 * i
    print('{}           {:.2f}'. format(i,fahrenheit))