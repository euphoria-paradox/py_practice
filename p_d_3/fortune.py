# Fortune teller program

have_question = 'y'

while have_question == 'y':
    question = input('What is your question?: \n')
    print('\nYou can ask me','"'+ question + '" . . .')
    
    if 'I' in question:
        print('You are in charge of your own destiny')
    
    elif 'new' in question:
        print('Changes are up to you and the unpredictable events in life.')
    
    elif 'bogus' in question or 'fake' in question:
        print("If it was the case, you wouldn't be here")
    
    elif 'he' in question or 'she' in question or 'they' in question:
        print('Someone unexpected can be most helpful with this.')
    
    elif 'real' in question:
        print('I would not allow such words')
    
    
    have_question = input('\nDo you have any other questions ?(y/n) ')

print('Goodbye ... hope I was of some help!')