# metric and amerian measurement systems conversions
# stage one

def displayWelcome():
    print(format('This program will be able to convert between the metric','^50'))
    print(format('measurements of cm,m,km,inches,miles,yards etc','^50'))
    
def getConvert():
    choice = 'Enter the unit of conversion input (cm or m or km or inch or feet'
    choice += ' or mile or yard): '
    select = input(choice)
    
    if select not in ('cm','m','km','inch','feet','mile','yard'):
        select = input(choice)
    
    if select == 'cm':
        output = input('Convert to?(m or km or inch or feet or mile or yard):')
        
    elif select == 'm':
        output = input('Convert to?(cm or km or inch or feet or mile or yard):')
    
    elif select == 'km':
        output = input('Convert to?(cm or m or inch or feet or mile or yard):')
        
    elif select == 'inch':
        output = input('Convert to?(cm or m or km or feet or mile or yard):')
        
    elif select == 'feet':
        output = input('Convert to?(cm or m or km or inch or mile or yard):')
        
    elif select == 'mile':
        output = input('Convert to?(cm or m or km or inch or feet or yard):')
        
    elif select == 'yard':
        output = input('Convert to?(cm or m or km or inch or feet or mile):')

    return (select, output)

def covertFromCM(output, value):
    
    if output == 'm':
        result = value / 100
        print(value,'cm =', format(result,'.2f'),'m')

    elif output == 'km':
        result = value / (100*1000)
        print(value,'cm =', format(result,'.2f'),'km' )
        
    elif output == 'inch':
        result = value * 0.3937007
        if result > 1:
            print(value,'cm =', format(result,'.2f'),'inches' )
        else:
            print(value,'cm =', format(result,'.2f'),'inch')
    
    elif output == 'feet':
        result = value * 0.032808
        if result > 1:
            print(value,'cm =', format(result,'.2f'),'feet')
        else:
            print(value,'cm =', format(result,'.2f'),'foot')
        
    elif output == 'mile':
        result = value * 6.2137e-6
        if result > 1:
            print(value,'cm =', format(result,'.2f'),'miles' )
        else:
            print(value,'cm =', format(result,'.2f'),'mile' )
        
    elif output == 'yard':
        result = value * 0.010936
        if result > 1:
            print(value,' cm', format(result,'.2f'),' yards' )
        else:
            print(value,'cm =', format(result,'.2f'),'yard' )


def convertFromM(output, value):

    if output == 'cm':
        result = value * 100
        print(value,'m =', format(result,'.2f'),'cm')

    elif output == 'km':
        result = value / (1000)
        print(value,'m =', format(result,'.2f'),'km' )
        
    elif output == 'inch':
        result = value * 39.37007
        if result > 1:
            print(value,'m =', format(result,'.2f'),'inches' )
        else:
            print(value,'m =', format(result,'.2f'),'inch')
    
    elif output == 'feet':
        result = value * 3.2808
        if result > 1:
            print(value,'m =', format(result,'.2f'),'feet')
        else:
            print(value,'m =', format(result,'.2f'),'foot')
        
    elif output == 'mile':
        result = value * 6.2137e-4
        if result > 1:
            print(value,'m =', format(result,'.2f'),'miles' )
        else:
            print(value,'m =', format(result,'.2f'),'mile' )
    
    elif output == 'yard':
        result = value * 1.0936
        if result > 1:
            print(value,' km', format(result,'.2f'),' yards' )
        else:
            print(value,'km =', format(result,'.2f'),'yard' )
        
        
def convertFromKm(output, value):

    if output == 'cm':
        result = value * 100 * 1000
        print(value,'km =', format(result,'.2f'),'cm')

    elif output == 'm':
        result = value * 1000
        print(value,'km =', format(result,'.2f'),'m' )
        
    elif output == 'inch':
        result = value * 39370.07
        if result > 1:
            print(value,'km =', format(result,'.2f'),'inches' )
        else:
            print(value,'km =', format(result,'.2f'),'inch')
    
    elif output == 'feet':
        result = value * 3280.8
        if result > 1:
            print(value,'km =', format(result,'.2f'),'feet')
        else:
            print(value,'km =', format(result,'.2f'),'foot' )
    
    elif output == 'mile':
        result = value * 0.62137
        if result > 1:
            print(value,'km =', format(result,'.2f'),'miles' )
        else:
            print(value,'km =', format(result,'.2f'),'mile' )
    
    elif output == 'yard':
        result = value * 1093.6
        if result > 1:
            print(value,' km', format(result,'.2f'),' yards' )
        else:
            print(value,'km =', format(result,'.2f'),'yard' )
    

def convertFromInch(output, value):
    
    if output == 'cm':
        result = value * 2.538071
        if value > 1:
            print(value,'inches =', format(result,'.2f'),'cm')
        else:
            print(value,'inch =', format(result,'.2f'),'cm')

    elif output == 'm':
        result = value * 0.0254
        if value > 1:
            print(value,'inches =', format(result,'.2f'),'m')
        else:
            print(value,'inch =', format(result,'.2f'),'m')
        
    elif output == 'km':
        result = value * 2.54e-5
        if value > 1:
            print(value,'inches =', format(result,'.2f'),'km' )
        else:
            print(value,'inch =', format(result,'.2f'),'km' )
    
    elif output == 'feet':
        result = value * 0.08333
        if value > 1:
            if result > 1:
                print(value,'inches =', format(result,'.2f'),'feet' )
            else:
                print(value,'inches =', format(result,'.2f'),'foot' )
        else:
            if result > 1:
                print(value,'inch =', format(result,'.2f'),'feet' )
            else:
                print(value,'inch =', format(result,'.2f'),'foot' )
        
    elif output == 'mile':
        result = value * 1.5782828e-5
        if value > 1:
            if result > 1:
                print(value,'inches =', format(result,'.2f'),'miles' )
            else:
                print(value,'inches =', format(result,'.2f'),'mile' )
        else:
            if result > 1:
                print(value,'inch =', format(result,'.2f'),'miles' )
            else:
                print(value,'inches =', format(result,'.2f'),'mile' )
                
                
    elif output == 'yard':
        result = value * 0.0278
        if value > 1:
            if result > 1:
                print(value,'inches =', format(result,'.2f'),'yards' )
            else:
                print(value,'inches =', format(result,'.2f'),'yard' )
        else:
            if result > 1:
                print(value,'inch =', format(result,'.2f'),'yards' )
            else:
                print(value,'inch =', format(result,'.2f'),'yard')
                

def convertFromfeet(output, value):
    
    if output == 'cm':
        result = value * 30.48
        if value > 1:
            print(value,'feet =', format(result,'.2f'),'cm')
        else:
            print(value,'foot =', format(result,'.2f'),'cm')

    elif output == 'm':
        result = value * 0.3048
        if value > 1:
            print(value,'feet =', format(result,'.2f'),'m')
        else:
            print(value,'foot =', format(result,'.2f'),'m')
        
    elif output == 'km':
        result = value * 0.3048e-3
        if value > 1:
            print(value,'feet =', format(result,'.2f'),'km' )
        else:
            print(value,'foot =', format(result,'.2f'),'km' )
    
    elif output == 'inch':
        result = value * 12
        if value > 1:
            if result > 1:
                print(value,'feet =', format(result,'.2f'),'inches' )
            else:
                print(value,'feet =', format(result,'.2f'),'inch' )
        else:
            if result > 1:
                print(value,'foot =', format(result,'.2f'),'inches' )
            else:
                print(value,'foot =', format(result,'.2f'),'inch' )
        
    elif output == 'mile':
        result = value * 0.189394e-3
        if value > 1:
            if result > 1:
                print(value,'feet =', format(result,'.2f'),'miles' )
            else:
                print(value,'feet =', format(result,'.2f'),'mile' )
        else:
            if result > 1:
                print(value,'foot =', format(result,'.2f'),'miles' )
            else:
                print(value,'foot =', format(result,'.2f'),'mile' )
                
                
    elif output == 'yard':
        result = value * 0.333333
        if value > 1:
            if result > 1:
                print(value,'feet =', format(result,'.2f'),'yards' )
            else:
                print(value,'feet =', format(result,'.2f'),'yard' )
        else:
            if result > 1:
                print(value,'foot =', format(result,'.2f'),'yards' )
            else:
                print(value,'foot =', format(result,'.2f'),'yard')
                

def convertFromMile(output, value):
    
    if output == 'cm':
        result = value * 160934
        if value > 1:
            print(value,'miles =', format(result,'.2f'),'cm')
        else:
            print(value,'mile =', format(result,'.2f'),'cm')

    elif output == 'm':
        result = value * 1609.34
        if value > 1:
            print(value,'miles =', format(result,'.2f'),'m')
        else:
            print(value,'mile =', format(result,'.2f'),'m')
        
    elif output == 'km':
        result = value * 1.60934
        if value > 1:
            print(value,'miles =', format(result,'.2f'),'km' )
        else:
            print(value,'mile =', format(result,'.2f'),'km' )
    
    elif output == 'inch':
        result = value * 63360
        if value > 1:
            if result > 1:
                print(value,'miles =', format(result,'.2f'),'inches' )
            else:
                print(value,'miles =', format(result,'.2f'),'inch' )
        else:
            if result > 1:
                print(value,'mile =', format(result,'.2f'),'inches' )
            else:
                print(value,'mile =', format(result,'.2f'),'inch' )
        
    elif output == 'feet':
        result = value * 5280
        if value > 1:
            if result > 1:
                print(value,'miles =', format(result,'.2f'),'feet' )
            else:
                print(value,'miles =', format(result,'.2f'),'foot' )
        else:
            if result > 1:
                print(value,'mile =', format(result,'.2f'),'feet' )
            else:
                print(value,'mile =', format(result,'.2f'),'foot' )
                
                
    elif output == 'yard':
        result = value * 1760
        if value > 1:
            if result > 1:
                print(value,'miles =', format(result,'.2f'),'yards' )
            else:
                print(value,'miles =', format(result,'.2f'),'yard' )
        else:
            if result > 1:
                print(value,'mile =', format(result,'.2f'),'yards' )
            else:
                print(value,'mile =', format(result,'.2f'),'yard')
                

def convertFromYard(output, value):
    
    if output == 'cm':
        result = value * 91.4444
        if value > 1:
            print(value,'yards =', format(result,'.2f'),'cm')
        else:
            print(value,'yard =', format(result,'.2f'),'cm')

    elif output == 'm':
        result = value * 0.91444
        if value > 1:
            print(value,'yards =', format(result,'.2f'),'m')
        else:
            print(value,'yard =', format(result,'.2f'),'m')
        
    elif output == 'km':
        result = value * 0.91444e-3
        if value > 1:
            print(value,'yards =', format(result,'.2f'),'km' )
        else:
            print(value,'yard =', format(result,'.2f'),'km' )
    
    elif output == 'inch':
        result = value * 36
        if value > 1:
            if result > 1:
                print(value,'yards =', format(result,'.2f'),'inches' )
            else:
                print(value,'yards =', format(result,'.2f'),'inch' )
        else:
            if result > 1:
                print(value,'yard =', format(result,'.2f'),'inches' )
            else:
                print(value,'yard =', format(result,'.2f'),'inch' )
        
    elif output == 'feet':
        result = value * 3
        if value > 1:
            if result > 1:
                print(value,'yards =', format(result,'.2f'),'feet' )
            else:
                print(value,'yards =', format(result,'.2f'),'foot' )
        else:
            if result > 1:
                print(value,'yard =', format(result,'.2f'),'feet' )
            else:
                print(value,'yard =', format(result,'.2f'),'foot' )
                
                
    elif output == 'mile':
        result = value * 0.5681818e-3
        if value > 1:
            if result > 1:
                print(value,'yards =', format(result,'.2f'),'miles' )
            else:
                print(value,'yards =', format(result,'.2f'),'mile' )
        else:
            if result > 1:
                print(value,'yard =', format(result,'.2f'),'miles' )
            else:
                print(value,'yard =', format(result,'.2f'),'mile')
                
    
    
