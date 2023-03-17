while True:
  guess=input('Invalid letter.  Please, enter a single alphabetical character.')
  if guess!=1:
    guess=input('Invalid letter.  Please, enter a single alphabetical character.')
  elif guess.isalpha()==False:
    guess=input('Please enter letters only:\n')
  else:
    print('You have guessed %s\n'%(guess))
    break
