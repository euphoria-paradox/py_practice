# First time buyer credit program

#Greet
print('This is a program that determines wheather a person qualifies for the',
      'government First Time Home Buyer Tax credit of $8000 based on some',
      'criterias like\n','a>bought a house for less than $ 800,000\n',
      'b>had a combined income of under $225,000\n',
      'c>had not owned a primary residence in the last 3 years.')

# input
name = input('Enter your name: ')
cost_of_first_house = int(input('Enter the total cost of first house: $'))
combined_income = int(input('Enter the combined income of your family: '))
owned_house = input('Have you owned any primary residence in the past 3 years?(Yes or No): ')

# check for conditions

if (cost_of_first_house < 800000) and (combined_income < 225000) and owned_house == 'Yes':
    print('You are eligible for a government First Time Home buyer credit',
          'of  $8,000. ')
    
else:
     print('You are not eligible for a government First Time Home buyer credit',
          'of  $8,000. ')
    
