'''
Exercise 17: Heat Capacity
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula: q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.
Extend your program so that it also computes the cost of heating the water. 
Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
'''

mass = float(input('Enter the mass of water in grams or volume in millimeters: '))
temperature = float(input('Enter the temperature change in Celsius: '))

KWH = 0.089
JKW = 2.77e-7

C = 4.186
q = mass * C * temperature
cost = q * JKW * KWH

print('The amount of energy that must be added or removed for that temperature change is {:.2f}'. format(q))
print('The cost taken in dollars is ${:.2f}'. format(cost))
