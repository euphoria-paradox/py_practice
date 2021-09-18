# Temperature Conversion Program

# This program converts the temperature entered in Celcius
# to equivalent degrees in Fahrenheit

# program greeting
print('This program will convert degrees Celsius to degrees Fahrenheit.')

#get temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Calculate degrees in Celcius
fahren = (9/5)*celsius+32

#Output degrees in Fahrenheit
print(celsius, 'degrees in Celsius equals to',
    format(fahren, '.2f'), 'degrees Fahrenheit.')
