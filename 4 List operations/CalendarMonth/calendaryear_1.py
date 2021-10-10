# Calendar Year Program (Stage 1)

#initialisation
terminate = False


#prompt for year until quit
while not terminate:
    
    #get year
    year = int(input('Enter the year(yyyy) (-1 to quit): '))
    
    while (year < 1800 or year > 2099) and year != -1:
        year = int(input('INVALID - Enter year(1800-2099): '))
        
        
    if year == -1:
        terminate = True
        
    else:
        # check if leap year
        if (year % 4 == 0) and (not(year % 100 == 0)) or (year % 400 == 0):
            leap_year = True
        else:
            leap_year = False
            
    
    # determine day of the week
    century_digits = year // 100
    year_digits = year % 100
    
    value = year_digits + (year_digits // 4)
    
    if century_digits == 18:
        value += 2
    elif century_digits == 20:
        value += 6
    
    
    # check leap year
    if not leap_year:
        value += 1
    
    
    # determine first day of month for Jan 1
    first_day_month = (value + 1) % 7
    
    
    print('Day of the week is:', first_day_month)