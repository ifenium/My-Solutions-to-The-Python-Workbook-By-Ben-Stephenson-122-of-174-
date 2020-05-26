'''
Exercise 27: Body Mass Index
Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula: BMI = 703 x weight / height × height
If you read the height in meters and the weight in kilograms then body mass index
is computed using this slightly simpler formula: BMI = weight / height × height
'''

weight = float(input('Enter your current weight in Kilgrams(Kg): '))
height = float(input('Enter your current height in meteres(M): '))

bmi = weight / height * height

print('Your current BMI (Body Mass Index) is {}'. format(bmi))