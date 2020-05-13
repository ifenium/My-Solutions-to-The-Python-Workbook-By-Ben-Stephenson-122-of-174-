''''
Exercise 17: Heat Capacity
(Solved—25 Lines)
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula: q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.
Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
'''

import math

mass = float(input('Enter the mass of water in gram(s) or millimeter(s): '))
temperature  = float(input('Enter the temperature change in Celcius: '))

q = mass * temperature * 4.186

print('That will reauire {} Joule of energy'. format(Q))

electricity_price = 8.9
j_to_kwh = 2.777e-7
kwh = q * j_to_kwh
cost = kwh * electricity_price

print('That much energy will cost {:.2f} cent'. format(cost))