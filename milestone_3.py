import random

def check_guess(guess):
    guess=guess.lower()
    if guess in word:
        count,i=0,0
        for x in word:
            if x==guess:
                count+=1
                #hidden[i]=guess
            i+=1
        print('%s occurs %s times in the word'%(guess,count))
        return hidden
    else:
        print('Sorry %s is not in the word'%(guess))
        return False
    
def ask_for_input(word):
    
    while True:
        guess=input('Please enter a single letter:\n')
        if len(guess)!=1:
            guess=input('Invalid letter.  Please, enter a single alphabetical character.')
        elif guess.isalpha()==False:
            guess=input('Invalid letter.  Please, enter a single alphabetical character.')
        else:
            print('You have guessed %s\n'%(guess))
            break
    
word_list=['rundown','tapout','carnival','inside','underground']
word=random.choice(word_list)
ask_for_input(word)
