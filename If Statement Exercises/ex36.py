'''
Exercise 36:Vowel or Consonant
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.
'''

letter = input('Enter a letter of the alphabet: ').lower()

vowels = ['a','e','i','o','u']
if letter in vowels:
    print(letter, 'is a vowel')
elif letter is 'y':
    print(letter, 'sometimes can be a consonant')
else:
    print(letter, 'is a consonant')