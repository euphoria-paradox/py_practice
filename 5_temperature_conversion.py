# Temperature Conversion Program

# This program converts the temperature entered in Fahrenheit
# to equivalent degrees in Celcius and vice versa

def displayWelcome():
    # program greeting
    print('This program will convert degrees Fahrenheit to degrees Celcius.')
    print('Enter (F) to convert Fahrenheit to Celcsius')
    print('Enter (C) to convert Celcsius to Fahrenheit')


def getConvertTo():
    #get temperature tonvert.
    choice = input('Enter your choice: ')
    
    while choice != 'F' and choice != 'C':
        choice = input('Enter your choice: ')
    
    return choice



def displayFahrenheitToCelsius(start, end):
    print('\n Degrees', ' Degrees')
    print('Fahrenheit', ' Celsius')
    
    # Calculate degrees in Celcius
    for temp in range(start, end + 1):
        celsius = (temp-32)*5/9
        #Output degrees in Celcius
        print('  ', format(temp,'.4f'), '  ', format(celsius,'4.1f'))
        
        
def displayCelsiusToFahrenheit(start, end):
    print('\n Degrees', ' Degrees')
    print('Celsius', ' Fahrenheit')
    for temp in range(start, end + 1):
        # Calculate degrees in Celcius
        fahren = (9/5)*temp+32
        #Output degrees in Fahrenheit
        print('  ', format(temp,'.4f'), '  ', format(fahren,'4.1f'))
        


# --- main

# displaywelcome
displayWelcome()

#get conversion
which = getConvertTo()

# get range of temperature
temp_start = int(input('Enter the starting limit of temperature: '))
temp_end = int(input('Enter the end limit of temperature: '))

# calculate
if which == 'F':
    displayFahrenheitToCelsius(temp_start, temp_end)
else:
    displayCelsiusToFahrenheit(temp_start, temp_end)