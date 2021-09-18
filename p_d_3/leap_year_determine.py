# Leap years to come program

import datetime

# This is a program that determines the leap years to come from the present
# year to the year inputted by the user
print('Welcome to the program!',
      'This program is used to determine the leap years ahead from present to',
      'the year input by user ....')

# get the current year
current_year = datetime.date.today().year
year = current_year

# get the final year input
final_year = int(input('Enter the year of limit(yyyy): '))

# determining leap year
while year <= final_year:
    
    if year % 4 == 0 and not(year % 100 == 0) or (year % 400 == 0):
            print(year,'is a leap year.')
    else:
        print('\t')
    year+=1
    

print('Program exiting...')
