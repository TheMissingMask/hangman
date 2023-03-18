# simple game of hangman with random and potentially very obscure words #
### very messy and could really use more in the class and less in the main body of the code

import random
from random_word import RandomWords

class Hangman:

    def __init__(self,word,nGuess=14):

        self.word=word # this is the random word
        self.nGuess=nGuess # this is the number of guesses left


    def printHidden(self,hidden): # just print out the current state of guessing in a user-friendly way

        self.hidden=hidden
        outString=''
        for i in self.hidden:
            outString+=i
        print(outString)

    def graphic(self,nGuess):

        self.guessDict={ # for the same of suspense, start drawing the hangman as more failed guesses take place...
                0:'''
                
                ''',
                1:'''
                .
                ''',
                2:
                '''
                ..
                ''',
                3:'''
                ...
                ''',
        4:'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
        5:'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
        6:'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
        7:'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
        8:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
        9:'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
        10:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
}

        print(self.guessDict[self.nGuess])


    def getGuess(self): # get the user to guess and check it is a viable input

        self.guessList=[]

        self.nGuess=0 # start with no wrong guesses

        while True:

            self.guess=input('Please enter a letter or the word [solved]:\n') # want a single letter or the word 'solved'
            self.guess=self.guess.lower()

            if self.guess=='solved':
                self.guess=self.guessWord(word) # option to guess the whole word
            elif len(self.guess)!=1:
                self.guess=input('Please enter only a single letter:\n') # check only one character was given
            elif self.guess.isalpha()==False:
                self.guess=input('Please enter letters only:\n') # check the character is a letter
            elif self.guess in self.guessList:
                self.guess=input('You have already tried that letter.  Please choose a new one:\n') # protect against duplicate guesses
            else:
                print('You have guessed %s\n'%(self.guess))
                self.guessList.append(self.guess)
                if self.guess in self.word:
                    count=0
                    for i in range(len(self.word)):
                        if self.word[i]==self.guess:
                            self.hidden[i]=self.guess
                            count+=1
                    print('\n%s appears %s times in the word\n'%(self.guess,count))
                    if '_' not in self.hidden:
                        print('Solved!  The answer is:\n')
                        self.printHidden(self.hidden)
                        break
                    else:
                        self.printHidden(self.hidden)
                else:
                    print('\n%s does not appear in the word\n'%(self.guess))
                    self.nGuess+=1
                    self.graphic(self.nGuess)
                    if self.nGuess==10:
                        print('No more guesses, I\'m afraid...\nThe word was %s'%(self.word))
                        break

        return(self.guess)

    def guessWord(self,word):

        self.word=word

        self.guess=input('What do you think the word is?\n')
        self.guess=self.guess.lower()

        if self.guess==self.word:
            print('\nYou are correct!\nThe word was %s\n'%(self.word))
            return True
        else:
            print('\nSorry, try again\n')
            return False

print('\n')
# start by getting a bunch of random words from the depths of the internet and selecting one at random
r=RandomWords()
word=r.get_random_word()
word=word.lower()


hangman=Hangman(word)
nGuess=14
hidden=['_']*len(word)
hangman.printHidden(hidden) # this just prints out underscores to indicate the number of letters
print('\n')
hangman.getGuess()
print('\n') # just have an extra bit of whitespace
