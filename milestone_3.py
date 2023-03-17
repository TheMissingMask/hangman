import random

word_list=['rundown','tapout','carnival','inside','underground']
word=random.choice(word_list)

while True:
    guess=input('Please enter a single letter:\n')
    if len(guess)!=1:
        guess=input('Invalid letter.  Please, enter a single alphabetical character.')
    elif guess.isalpha()==False:
        guess=input('Invalid letter.  Please, enter a single alphabetical character.')
    else:
        print('You have guessed %s\n'%(guess))
        break
if guess in word:
    count=0
    for x in word:
        if x==guess:
            count+=1
    print('%s occurs %s times in the word'%(guess,count))
else:
    print('Sorry %s is not in the word'%(guess))
