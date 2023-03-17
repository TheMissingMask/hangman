while True:
    guess=input('Please enter a single letter:\n')
    if len(guess)!=1:
        guess=input('Invalid letter.  Please, enter a single alphabetical character.')
    elif guess.isalpha()==False:
        guess=input('Invalid letter.  Please, enter a single alphabetical character.')
    else:
        print('You have guessed %s\n'%(guess))
        break
