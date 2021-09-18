# Temperature Conversion Program

# This program converts the temperature entered in Fahrenheit
# to equivalent degrees in Celcius and vice versa and determining Kelvin scale
# temperature from Celcius value
# absolute zero in F is -459.67
# absolute zero in C is -273.15
# 

# program greeting
print('This program will convert degrees Fahrenheit to degrees Celcius.')
print('Enter (F) to convert Fahrenheit to Celcsius')
print('Enter (C) to convert Celcsius to Fahrenheit')

#get temperature tonvert.
choice = input('Enter your choice: ')

while choice != 'F' and choice != 'C':
    choice = input('Please enter (F) or (C): ')
    
temp = float(input("Enter the temperature in: "))

if choice == 'F':
    
    #Checking wheather temperature input is valid or not
    if temp < -459.67:
        temp = float(input('INVALID-Enter a valid temperature: '))
    
    # Calculate degrees in Celcius
    celsius = (temp-32)*5/9
    #Output degrees in Celcius
    print(temp, 'degrees in Fahrenhit =',
        format(celsius, '.2f'), 'degrees Celsius.')
    
    kelvin = celsius + 273.15
    print(format(celsius, '.2f'), 'degrees Celsius =',format(kelvin,'.2f'), 'degrees Kelvin.')


elif choice == 'C':
    
    #Checking wheather temperature input is valid or not
    if temp < -273.15:
        temp = float(input('INVALID-Enter a valid temperature: '))
    # Calculate degrees in Celcius
    fahren = (9/5)*temp+32
    #Output degrees in Fahrenheit
    print(temp, 'degrees in Celsius =',
        format(fahren, '.2f'), 'degrees Fahrenheit.')
    kelvin = temp + 273.15
    print(temp, 'degrees Celsius =',kelvin,'degrees Kelvin.')

else:
    print('Invalid Input')