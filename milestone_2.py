#!/usr/bin/python

import random

word_list=['rundown','tapout','underground','inside','carnival']
#word_list=[x.lower() for x in word_list]
#print(type(word_list))

word=random.choice(word_list)

guess=input('Please enter a letter:\n')
guess=guess.lower() # more robust if we are only dealing with lower case letters

if len(guess)!=1:
  print('Please enter only a single letter')
else:
  print('You have guessed %s'%(guess))
