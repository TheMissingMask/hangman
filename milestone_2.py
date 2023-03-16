#!/usr/bin/python

import random

word_list=['Rundown','Tap out','Maltese Falcon','Inside','Beantown Bailout']
word_list=[x.lower() for x in word_list]

word=random.choice(word_list)

guess=input('Please enter a letter:\n')
guess=guess.lower() # more robust if we are only dealing with lower case letters
