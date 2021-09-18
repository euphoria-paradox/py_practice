# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 12:41:08 2021

@author: Itachi
"""

# Number of days in a month program

# Greet
print('This program will determine the number of days in a given month\n')

# init
valid_input = True

# get input
month = int(input('Enter the month(1-12):'))
if month < 1 or month > 12:
    month = int(input('INVALID month - Enter a proper month: '))

year = int(input('Enter the year: '))

# determine number of days in a month

# feb
if month == 2:
    if (year%4==0) and not(year%100==0) or (year%400 ==0):
        leap_year = True
        num_days = 29
    else:
        leap_year = False
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
    if leap_year:
        print('\nThere are', num_days,'days in the month(a leap year)')
    else:    
        print('\nThere are', num_days,'days in the month')