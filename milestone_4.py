import random

class Hangman:

    def __init__(self,word_list,num_lives=5):

        self.word_list=word_list
        self.num_lives=num_lives

        self.word=random.choice(word_list)
        self.num_letters=len(set(self.word))

        self.word_guessed=['_']*len(self.word)
        self.list_of_guesses=[]

    def check_guess(self,guess):

        self.guess=guess
        self.guess=self.guess.lower()

        if self.guess in self.word:
            count,i=0,0
            for x in self.word:
                if x==self.guess:
                    count+=1
                    self.word_guessed[i]=self.guess
                i+=1
            print('Good guess! %s is in the word'%(self.guess))
#            print('%s occurs %s times in the word'%(guess,count))
#            return self.word_guessed
#        else:
#            print('Sorry %s is not in the word'%(guess))
            return False

    def ask_for_input(self):

        while True:
            self.guess=input('Please enter a single letter:\n')
            if len(self.guess)!=1:
                self.guess=input('Invalid letter.  Please, enter a single alphabetical character.')
            elif self.guess.isalpha()==False:
                self.guess=input('Invalid letter.  Please, enter a single alphabetical character.')
            elif self.guess in self.list_of_guesses:
                print('You already tried that letter')
            else:
                print('You have guessed %s\n'%(self.guess))
                self.list_of_guesses.append(self.guess)
                break
word_list=['rundown','tapout','carnival','inside','underground']
hangman=Hangman(word_list)
hangman.ask_for_input()
