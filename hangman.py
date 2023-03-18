#!/usr/bin/python

#####start with simpler version of the code and then tidy up later

import random
from random_word import RandomWords

r=RandomWords()
word=r.get_random_word()
word=word.lower()

def printHidden(hidden):

    outString=''
    for i in hidden:
        outString+=i
    print(outString)

def checkChar(guess):

    alphabet=[chr(value) for value in range(97,123)]
    for x in ['-',' ']:
        alphabet.append(x) # allow hyphens and spaces

    if guess not in alphabet:
        return False
    else:
        return True

def getGuess(word):

    guess=input('Please enter a letter or the word [solved]:\n')

    if guess=='solved':
        guess=guessWord(word)
    elif len(guess)!=1:
        guess=input('Please enter only a single letter:\n')
    elif checkChar(guess)==False:
        guess=input('Please enter letters, hyphens and spaces only:\n')
    else:
        print('You have guessed %s\n'%(guess))

    return(guess)

def guessWord(word):

    guess=input('What do you think the word is?\n')
    guess=guess.lower()

    if guess==word:
        print('\nYou are correct!\nThe word was %s\n'%(word))
        return True
    else:
        print('\nSorry, try again\n')
        return False

nGuess=14
hidden=['_']*len(word)
printHidden(hidden)
print('\n')

while nGuess>=0: # while there are still guesses left
    try0=getGuess(word)
    if try0==False:
        nGuess-=1
    elif try0==True:
        break
    elif try0 in word:
        count=0
        for i in range(len(word)):
            if word[i]==try0:
                hidden[i]=try0
                count+=1
        print('\n%s appears %s times in the word\n'%(try0,count))
        printHidden(hidden)
        if '_' not in hidden:
            print('\nYou have solved the word\nIt is:\n')
            printHidden(hidden)
            break
    else:
        print('\n%s does not appear at all in the word\n'%(try0))
        nGuess-=1
        if nGuess==-1:
            print('Hung!\nThe word was %s\n-------'%(word))
            break
        else:
            print('%s guesses left\n'%(nGuess))

print('\n')
