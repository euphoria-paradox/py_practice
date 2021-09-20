# Chinese Zodiac Program

import datetime

# Init
zodiac_animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
                  'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

rat = 'Forthright, industrious, sensitive, intellectual, socialable'
ox = 'Dependable, methodical, modest, born leader, patient'
tiger = 'Unpredictable, rebellious, passionate, darling, impulsive'
rabbit = 'Good friend, kind, soft-spoken, cautious, artistic'
dragon = 'Strong, self-assured, proud, decisive, loyal'
snake = 'Deep thinker, creative, responsible, calm, purposeful'
horse = 'Cheerful, quick-witted, perceptive, talkative, open-minded'
goat = 'Sincere, sympathetic, shy, generous, mothering'
monkey = 'Motivator, inquisitive, flexible, innovative, problem-solver'
rooster = 'Organized, self-assured, decisive, perfectionist, zealous'
dog = 'Honest, unpretentious, idealistic, moralistic, easy going'
pig = 'Peace-loving, hard-working, trusting, understanding, thoughtful'


characteristic = [rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey,
                  rooster, dog, pig]

terminate = False

#greet
print('This program will display chineses zodiac sign and associated personal')
print('characteristics\n')


while not terminate:
    
    #get birth year
    birth_year = int(input('Enter your birth year(yyyy): '))
    
    while birth_year< 1900 or birth_year> 2099:
        print('Invalid Year')
        birth_year = int(input('Enter your birth year(yyyy): '))
        
    # output
    cycle_num = (birth_year - 1900) % 12
    
    print('Your zodiac sign is the:', zodiac_animals[cycle_num], '\n')
    print(characteristic[cycle_num])
    
    
    #continue
    una_vez_mas = input('\n Would you like to try again? (y or n): ')
    
    while una_vez_mas != 'y' and una_vez_mas != 'n':
        una_vez_mas = input('Please enter "y" or "n": ')
        
    if una_vez_mas == 'n':
        terminate = True
        

    