import random

word_list=['rundown','tapout','underground','carnival','inside']
word=random.choice(word_list)

guess=input('Please enter a letter:\n')

if len(guess)!=1:
  print('Oops!  That is not a valid input!')
  guess=input('Please try again\n')
elif len.isalpha()==False:
  print('Oops!  That is not a valid input!')
  guess=input('Please try again\n')
else:
  print('Good guess!')
