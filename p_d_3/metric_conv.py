# Metric conversion program

# This is a program to convert pounds to grams,inches to cm, km to miles
# and vice versa.
# shorthand input of conversion types are:
# pounds to grams = lbgm
# inches to cm = incm
# km to miles = kmmiles
# greet
print('Welcome to the metric conversion program!')

# ask for type of conversion lb to gm or in to cm or km to miles
type_of_conversion = input('Enter the type of conversion(q to quit)(lbgm) or (incm) or (kmmiles):')

# conversion calculations
while type_of_conversion != 'q':
    
    # pounds to gram and vice versa conversion
    if type_of_conversion == 'lbgm':
        print(format('Pounds/Grams conversion','-^27'))
        choice = input('Enter the unit of input value:(lb or gm)(q to quit):')
        
        # pounds to grams
        if choice == 'lb':
            lbs = float(input('Enter the weight/mass in pounds: '))
            grams = lbs*453.92  # 1 pound = 0.454 kg = 453.92 gms
            print(lbs,'lb =',grams,'grams\n')
        
            #grams to pounds
        elif choice == 'gm':
            grams = float(input('Enter the weight/mass in grams: '))
            lbs = grams/453.92
            print(grams,'grams =',lbs,'lb\n')
        
        elif choice == 'q':
            print('\nGoodbye')
            break
        
        else:
            print('Invalid unit')
            break
            
    
    elif type_of_conversion == 'incm':
        print(format('Inches/Cms coversions','-^27'))
        choice = input('Enter the unit of input value:(inch or cm)(q to quit):')
        
        if choice == 'inch':
            inches = float(input('Enter the dimension in inches: '))
            cms = inches/2.54   # 1 inch = 2.54 cm
            print(inches,'inch =',format(cms,'.2f'),'cm.')
            
        elif choice == 'cm':
            cm = float(input('Enter the dimension in centimetres: '))
            inches = cm*2.54
            print(cm,'cm =',inches,'inch\n')
        
        elif choice == 'q':
            print('\nGoodbye')
            break
        
        else:
            print('Invalid unit')
            break
            
        
    elif type_of_conversion == 'kmmiles':
        print(format('Km/Miles conversion','-^27'))
        choice = input('Enter the unit of input value:(km or miles)(q to quit):')
        
        if choice == 'km':
            kms = float(input('Enter the distance in km: '))
            miles = kms/1.609
            print(kms,'km =',format(miles,'.2f'),'mile\n')
            
        elif choice == 'miles':
            miles = float(input('Enter the distance in miles: '))
            kms = miles * 1.609
            print(miles,'miles =',format(kms,'.2f'),'kms\n')            
            
        elif choice == 'q':
            print('\nGoodbye')
            break
        
        else:
            print('Invalid unit')
            break
        
        
print('\nThank you')