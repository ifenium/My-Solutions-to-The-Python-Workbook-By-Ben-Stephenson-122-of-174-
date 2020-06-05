'''
Exercise 72: Is a String a Palindrome?
A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words.Write a program
that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.
'''

word = input('Enter a word to check if its is a palindrome: ')

if len(word) == 1:
    print('You cannot check if a letter is a palindrome')
else:
    if word[::-1] == word:  
        print('{} is a palindrome'. format(word))
    else:
        print('{} is not a palindrome'. format(word))