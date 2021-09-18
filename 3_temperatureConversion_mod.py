# Temperature Conversion Program

# This program converts the temperature entered in Fahrenheit
# to equivalent degrees in Celcius and vice versa

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
    # Calculate degrees in Celcius
    celsius = (temp-32)*5/9
    #Output degrees in Celcius
    print(temp, 'degrees in Fahrenhit equals to',
        format(celsius, '.2f'), 'degrees Celsius.')
elif choice == 'C':
    # Calculate degrees in Celcius
    fahren = (9/5)*temp+32
    #Output degrees in Fahrenheit
    print(temp, 'degrees in Celsius equals to',
        format(fahren, '.2f'), 'degrees Fahrenheit.')
else:
    print('Invalid Input')