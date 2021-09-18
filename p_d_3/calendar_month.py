# Calendar Month Program
# (stage 1)

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
        
        print('\n', month, '/', year, 'has', num_days, 'days.')
        
        if leap_year:
            print('\n',year,'is a leap year\n')
        else:
            print(year,'is not a Leap year.\n')