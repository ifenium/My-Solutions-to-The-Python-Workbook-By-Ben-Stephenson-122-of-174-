'''
Exercise 30: Units of Pressure
In this exercise you will create a program that reads a pressure from the user in kilopascals. 
Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
'''
kilopascals = float(input('Enter the current pressure in kilopascal: '))

pound_per_square_inch = kilopascals * 0.145038
millimeter_of_mercury = kilopascals *  7.501875
atmospheres = kilopascals * 0.00986923

print('The pressure in Pound per Square Inch is {:.2f}'. format(pound_per_square_inch))
print('The pressure in Millimeter of Mercury is {:.2f}'. format(millimeter_of_mercury))
print('The pressure in Atmosperes is {:.2f}'. format(atmospheres))