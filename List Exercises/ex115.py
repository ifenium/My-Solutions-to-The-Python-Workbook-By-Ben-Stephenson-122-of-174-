'''
Exercise 115: Pig Latin
Pig Latin is a language constructed by transforming English words. 
While the origins of the language are unknown, it is mentioned in at least two documents from
the nineteenth century, suggesting that it has existed for more than 100 years. The
following rules are used to translate English into Pig Latin:

• If the word begins with a consonant (including y), then all letters at the beginning of
the word, up to the first vowel (excluding y), are removed and then added to the end
of the word, followed by ay. For example, computer becomes omputercay
and think becomes inkthay.

• If the word begins with a vowel (not including y), then way is added to the end
of the word. For example, algorithm becomes algorithmway and office
becomes officeway.
Write a program that reads a line of text from the user. Then your program should
translate the line into Pig Latin and display the result. You may assume that the string
entered by the user only contains lowercase letters and spaces.
'''

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']

line = input('Enter a sample text: ')

new = ''
i = 0
cond = False
length = len(line)

if line[0] in vowels:
    new += line + 'way'
else:
    while not cond:
        if line[i] in consonants and line[i+1] in vowels:
            new += line[i+1:] + line[:i+1] + 'ay'
            cond = True 
        else:
            i += 1

print(new)