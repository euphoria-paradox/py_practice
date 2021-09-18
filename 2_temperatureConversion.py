# Temperature Conversion Program

# This program converts the temperature entered in Fahrenheit
# to equivalent degrees in Celcius

# program greeting
print('This program will convert degrees Fahrenheit to degrees Celcius.')

#get temperature in Fahrenheit
fahr = float(input("Enter the temperature in Fahrenheit: "))

# Calculate degrees in Celcius
celsius = (fahr-32)*5/9

#Output degrees in Celcius
print(fahr, 'degrees in Fahrenhit equals to',
    format(celsius, '.2f'), 'degrees Celsius.')
