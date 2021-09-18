# Number of days in a month program

# Greet
print('This program will determine the number of days in a given month\n')

# init
valid_input = True

# get input
month = int(input('Enter the month(1-12):'))

# determine number of days in a month

# feb
if month == 2:
    year = int(input('Enter the year: '))
    if (year%4==0) and not(year%100==0) or (year%400 ==0):
        num_days = 29
    else:
        num_days = 28

# jan, mar,may,july,august,oct,dec
elif month in (1,3,5,7,8,10,12):
    num_days = 31

#april , jun,sept,nov
elif month in (4,6,9,11):
    num_days = 30

else:
    valid_input = False
    print('Enter a valid month')

#output
if valid_input:
    print('\nThere are', num_days,'days in the month')