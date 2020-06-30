'''
Exercise 111: Only the Words
In this exercise you will create a program that identifies all of the words in a string
entered by the user. Begin by writing a function that takes a string of text as its only
parameter. Your function should return a list of the words in the string with the punctuation marks at 
the edges of the words removed. The punctuation marks that you mustremove include commas, periods, 
question marks, hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove 
punctuation marks that appear in the middle of a words, such as the apostrophes used to form a contraction. 
For example, if your function is provided with the string "Examples of contractions
include: don’t, isn’t, and wouldn’t." then your function should return the list 
["Examples", "of", "contractions", "include", "don’t", "isn’t", "and", "wouldn’t"].
Write a main program that demonstrates your function. It should read a string
from the user and display all of the words in the string with the punctuation marks
removed. You will need to import your solution to this exercise when completing
Exercise 158. As a result, you should ensure that your main program only runs when
your file has not been imported into another program.
'''

def onlywords(s):
    punctuations = ''',., ?- '!:;'''
    words = s.split()

    for i in words:
        for j in i:
            if j in punctuations:
                i = i.replace(j, '')
    
    return words
    

def main():
    print(onlywords("Examples of contractions include: don’t, isn’t, and wouldn’t."))

if __name__ == '__main__':
    main()