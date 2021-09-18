# Life Signs
# This is a test program to that determines number of breaths
# and the number of heartbeats the person had in their life
# based on their age.

# The average respiration rate of people changes during different
# stages of development.

# the breath rates used are :
    # Infant - 30-60 breaths per min
    # 1-4 years - 20-30 breaths per min
    # 5-14 years - 15-25 breaths per min
    # adults - 12-20

# Avg heart rate is 67.5 beats per second.

# Greet 
print('Welcome to the program')
print('''This is a test program to that determines number of breaths
and the number of heartbeats the person had in their life based on their age.''')

#init
valid = True

#user input of age
age = int(input('Enter your age: '))

# calculate the breaths.

if age>=1 and age<=4:
    num_breaths = (((30+60)//2)*60*24*365)+((age)*((20+30)//2)*60*24*365)
    
elif age>4 and age<=14:
    num_breaths = (((30+60)//2)*60*24*365)+(4*((20+30)//2)*60*24*365)+ (age*(15+25//2)*60*24*365)
   
elif age>14:
    num_breaths = (((30+60)//2)*60*24*365)+(4*((20+30)//2)*60*24*365)+ (14*(15+25//2)*60*24*365)+(age*((12+20)/2)*60*24*365)

else:
    valid = False
    print('Enter the correct age')

if valid:
    heart_rate = age*67.5*60*24*365
    print('The approximate number of breaths taken by you in',age,'years is',format(num_breaths,','),'\n',
        'The approximate number of heartbeats you had in',age,'years is',format(heart_rate,','),'\n')