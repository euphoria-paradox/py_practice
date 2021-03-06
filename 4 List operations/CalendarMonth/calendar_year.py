# Calendar Year Program (Stage 1)

#initialisation
terminate = False
days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

month_names= ('January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December')

calendar_year = []
month_separator = format(' ', '8')
blank_week = format(' ', '21')
blank_col = format(' ', '3')


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
    #print('Day of the week is:', first_day_month)
    
    for month_num in range(12):
        month_name = month_names[month_num]
        
        # init for new month
        current_day = 1
        if first_day_month == 0:
            starting_col = 7
        else:
            starting_col = first_day_month
            
        
        current_col = 1
        calendar_week  = ''
        calendar_month = []
        
        # add any leading space for first week of month
        while current_col < starting_col:
            calendar_week = calendar_week + blank_col
            current_col += 1
            
        #start month as separate weeks
        if (month_name == 'February') and leap_year:
            num_days_this_month = 29
        
        else:
            num_days_this_month = days_in_month[month_num]
            
            
        while current_day <= num_days_this_month:
            
            # store day of month in field of length 3
            calendar_week = calendar_week + format(str(current_day), '>3')
                
            #check if at last column of displayed week
            if current_col == 7:
                calendar_month = calendar_month + [calendar_week]
                calendar_week = ''
                current_col = 1
            
            else:
                current_col += 1
                
            # increment current day
            current_day += 1
            
        
        # fill out final row of month with needed  blanks
        calendar_week = calendar_week + \
            blank_week[0:(7- current_col + 1) * 3]
        calendar_month = calendar_month + [calendar_week]
        
        # reset values for next month
        first_day_month = current_col 
        calendar_year = calendar_year + [calendar_month]
        calendar_month = []
        
print(calendar_year)
        
    # print calendar year
'''    print('\n', year, '\n')
    
    # each row starts with January April July or October
    for month_num in [0, 3, 6, 9]:
        
        # display three months in each row
        for i in range(month_num, month_num + 3):
            print(' ' + format(month_names[i], '19'),
                  month_separator, end = '')
            
      
        # display each week of months on separate lines
        week = 0
        lines_to_print = True
        
        while lines_to_print:
            
            # init 
            lines_to_print = False
            
            # another week to display for first month in row?
            for k in range(month_num, month_num + 3):
                if week < len(calendar_year[k]):
                    print(calendar_year[k][week], end = '')
                    lines_to_print = True
                    
                else:
                    print(blank_week, end = '')
                    
                print(month_separator, end = '')
                
            
            # move to next screen line
            print()
            
            #increment week
            week += 1
'''