# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:52:17 2021

@author: Itachi
"""

# Calendar Month Program
# (stage 2)

#init
terminate = False

#program greeting
print(format('This program will display a calendar month between 1800 and 2099','.^80'))

while not terminate:
    #get month and year
    month = int(input('Enter the month(1-12)(-1 to quit): '))
    
    if month == -1:
        terminate = True
    
    else:
        while month < 1 or month > 12:
            month = int(input('INVALID INPUT Enter month (1-12):'))
            
        year = int(input('Enter the year(yyyy): '))
        
        while year < 1800 or year > 2099:
            year = int(input('INVALID - Enter year(1800-2099): '))
        
        
        #determine if leap year or not
        if year % 4 == 0 and not(year % 100 == 0) or (year % 400 == 0):
            leap_year = True
        
        else:
            leap_year = False
            
        
        # determine the number of days in the month
        if month in (1, 3, 5, 7, 8, 10, 12):
            num_days = 31
        
        elif month in (4, 6, 9, 11):
            num_days = 30
        
        elif leap_year:     # February
            num_days = 29
        
        else:
            num_days = 28
        
        
        # determine the days of week
        century_digits = year//100
        year_digits = year%100
        
        value = year_digits + round(year_digits/4)
        
        
        if century_digits == 18:
            value += 2
        
        elif century_digits == 20:
            value += 6
        
        if month == 1 and not leap_year:
            value+=1
        
        elif month == 2:
            if leap_year:
                value+= 3
            
            else:
                value += 4
        
        elif month == 3 or month == 11:
            value += 4
            
        elif month == 4 or month == 7:
            value += 0
        
        elif month == 5:
            value += 2
        
        elif month == 6:
            value += 5
            
        elif month == 8:
            value += 3
            
        elif month == 10:
            value += 1
            
        elif month == 9 or month == 12:
            value += 6
        
        
        day_of_week = (value + 1) % 7       # 1-Sunday 2-Monday .....
        
        # display result
        
        print('\nDay of the week is', day_of_week)