'''
Exercise 73: Multiple Word Palindromes
There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 72 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
extend your solution so that is also ignores punctuation marks and treats uppercase
and lowercase letters as equivalent.
'''

import string
punct = set(string.punctuation)

words = input('Enter a phrase or sentence to check if its is a palindrome: ').lower().replace(" ", "")
words_punct = ''.join(x for x in words if x not in punct)


if len(words_punct) == 1:
    print('You cannot check if a letter is a palindrome')
else:
    if words_punct[::-1] == words_punct:  
        print('{} is a palindrome'. format(words))
    else:
        print('{} is not a palindrome'. format(words))