# Oil change notification
print('This program determines if your car needs an oil change or not.')

#init
miles_oil_change = 7500 #miles between oil change
miles_warn = 500 # how soon to warn of oil change
valid_entries = False

# get mileage of last oil change and current mileage and display

while not valid_entries:
    miles_last_oil_change = int(input('Enter the mileage of last oil change: '))
    current_mileage = int(input('Enter the current mileage: '))
    
    if current_mileage < miles_last_oil_change:
        print('Invalid entry - current mileage less than')
        print('mileage entered of last oil change')
    else:
        miles_travelled = current_mileage-miles_last_oil_change
        valid_entries = True

if miles_travelled >= miles_oil_change:
    print('You are due for an oil change by',miles_travelled-miles_oil_change, 'miles.')
elif miles_travelled >= miles_oil_change - miles_warn:
    print('You will soon need an oil change in', miles_travelled-miles_oil_change, 'miles.')
else:
    print('You do not need an oil change any time soon , after about',
          (miles_oil_change-miles_travelled),'miles.')
    