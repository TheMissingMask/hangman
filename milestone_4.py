import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list=word_list
        self.num_lives=num_lives
        self.word=random.choice(word_list)
        self.num_letters=len(set(self.word))
        self.word_guessed=['_']
        self.list_of_guesses=[]

    

def check_guess(guess,word,hidden):
    guess=guess.lower()
    word=word.lower()
    if guess in word:
        count,i=0,0
        for x in word:
            if x==guess:
                count+=1
                hidden[i]=guess
            i+=1
        print('%s occurs %s times in the word'%(guess,count))
        return hidden
    else:
        print('Sorry %s is not in the word'%(guess))
        return False
    
def ask_for_input(word,hidden):
    
    while True:
        guess=input('Please enter a single letter:\n')
        if len(guess)!=1:
            guess=input('Invalid letter.  Please, enter a single alphabetical character.')
        elif guess.isalpha()==False:
            guess=input('Invalid letter.  Please, enter a single alphabetical character.')
        else:
            print('You have guessed %s\n'%(guess))
            break
    hidden=check_guess(guess,word,hidden)

def printHidden(hidden):
    outString=''
    for i in hidden:
        outString+=i
    print(outString)
    
word_list=['rundown','tapout','carnival','inside','underground']
word=random.choice(word_list)
hidden=['_']*len(word)

ask_for_input(word,hidden)