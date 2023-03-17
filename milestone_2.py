import random

word_list=['Rundown','Tap out','Maltese Falcon','Inside','Beantown Bailout']
word_list=[x.lower() for x in word_list]
word=random.choice(word_list)

guess=input('Please enter a letter:\n')
