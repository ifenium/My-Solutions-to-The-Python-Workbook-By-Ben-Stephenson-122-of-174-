'''
Exercise 29: Celsius to Fahrenheit and Kelvin
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
'''

celsius = float(input('Enter the current temperature in Celsius: '))

fahrenheit = 32 + celsius * 9/5
kelvin = celsius + 273.15

print('The temperature in Fahrenheit is {} \nThe temperature in Kelvin is {}'. format(fahrenheit,kelvin))