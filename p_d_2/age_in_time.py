'''Age in seconds program.
   This program calculate a person's age approximately in seconds.'''

import datetime

#Program greet
print('''This program computes the approximate age of person in seconds
based on a provided date of birth. Only the dates of birth from 1900 and 
after can be computed\n''')

#Get month,day,year of birth.
month_birth = int(input('Enter month born(1-12): '))
day_birth = int(input('Enter the day born(1-31): '))
year_birth = int(input('Enter the year born(4 digit): '))

#print(day_birth, '/', month_birth, '/', year_birth)

#Get current month,day,year
current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

#print(current_day,'/',current_month,'/',current_year)

#Determine the number of seconds in a day,average month, and average year.
numsecs_day = 60*60*24
numsecs_year = numsecs_day*365

average_secs_year = ((numsecs_year * 4) + numsecs_day)//4
avg_secs_month = average_secs_year//4

# Calculate the number of seconds of age.
numsecs_1900_dob = ((year_birth-1900)*average_secs_year) + \
    ((month_birth-1) * avg_secs_month) + (day_birth*numsecs_day)

numsecs_1900_current = ((current_year-1900)*average_secs_year) + \
    ((current_month-1)*avg_secs_month) + (current_day*numsecs_day)

age_in_seconds = numsecs_1900_current - numsecs_1900_dob
age_in_minutes = age_in_seconds/60
age_in_hours = age_in_minutes/60
age_in_days =  age_in_hours//24 

# Output result
print('\n You are approximately', age_in_seconds, 'seconds old.')
print('\n You are approximately', age_in_minutes, 'minutes old.')
print('\n You are approximately', age_in_hours, 'hours old.')
print('\n You are approximately', age_in_days, 'days old.')