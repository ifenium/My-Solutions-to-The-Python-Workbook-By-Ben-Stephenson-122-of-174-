'''
Exercise 54:Wavelengths of Visible Light
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:
Color                   Wavelength (nm)
Violet                  380 to less than 450
Blue                    450 to less than 495
Green                   495 to less than 570
Yellow                  570 to less than 590
Orange                  590 to less than 620
Red                     620 to 750
Write a program thatreads a wavelengthfrom the user andreports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
'''

wavelength = float(input('Enter the wavelength of your color in nanometeres(nm): '))

if 380 < wavelength <= 450:
    color = 'Violet'
elif 450 < wavelength <= 495:
    color = 'Blue'
elif 495 < wavelength <= 570:
    color = 'Green'
elif 570 < wavelength <= 590:
    color = 'Yellow'
elif 590 < wavelength <= 620:
    color = 'Oranege'
elif 620 < wavelength <= 750:
    color = 'Red'
else:
    color = 'null'

if color == 'null':
    print('Please enter a valid wavelength')
else:
    print('The corresponding color to the wavelength {} nm is {}'. format(wavelength, color))