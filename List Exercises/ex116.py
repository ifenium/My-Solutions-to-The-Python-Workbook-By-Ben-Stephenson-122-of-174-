'''
Exercise 116: Pig Latin Improved
Extend your solution to Exercise 115 so that it correctly handles uppercase letters and
punctuation marks such as commas, periods, question marks and exclamation marks.
If an English word begins with an uppercase letter then its Pig Latin representation
should also begin with an uppercase letter and the uppercase letter moved to the end of
the word should be changed to lowercase. For example, Computer should become
Omputercay. If a word ends in a punctuation mark then the punctuation mark
should remain at the end of the word after the transformation has been performed.
For example, Science! should become Iencescay!.
'''

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels = ['a','e','i','o','u']
punctuations = [',','.','?']

line = input('Enter a sample text: ')

new = ''
i = 0
cond = False
length = len(line)
index = ''

for i in line:
    if i in punctuations:
        index = line.index(i)
    break


punc = line[index]
line.pop(index)

if line[0] in vowels:
    new += line + 'way' + str(punc)
else:
    while not cond:
        if line[i] in consonants and line[i+1] in vowels:
            new += line[i+1:] + line[:i+1] + 'ay' + str(punc)
            cond = True 
        else:
            i += 1

print(new)