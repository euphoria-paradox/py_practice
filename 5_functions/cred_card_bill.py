# Credit card calculation program(stage 1)

def displayWelcome():
    print('This program displays the time to pay off a credit')
    print('card and the interest paid based on the curent balance,')
    print('the interest rate and monthly payments made.')
    

def displayPayments(balance, int_rate, monthly_payment):
    # init
    num_months = 0
    total_int_paid = 0
    payment_num = 1
    
    empty_area = format(' ', '8')
    
    # display loan info 
    print('\n', format('PAYOFF SCHEDULE', '>20'))
    print(format('Year', '>10') + format('Balance','>10') + 
          format('Payment Num','>14') + format('Interest Paid','>16'))
    
    
    # display yearly account status
    while balance > 0:
        monthly_int = balance * int_rate
        total_int_paid = total_int_paid + monthly_int
        balance = balance + monthly_int - monthly_payment
        
        if balance < 0:
            balance = 0
            
        if num_months % 12 == 0:
            year = format((num_months // 12) + 1, '>8')
        else: 
            year = empty_area
            
        print(year + format(balance, '>12,.2f') +
              format(payment_num,'>9') + format(total_int_paid, '>17.2f'))
        
        payment_num += 1
        num_months += 1
        
    
# main -----

#display welcome screen
displayWelcome()

# get current balance and APR
balance = int(input('\nEnter the balance on your credit card: '))
apr = int(input('Enter the interest rate (APR) on the card: '))

monthly_int_rate = apr/1200

yes_response = ('y','Y')
no_response = ('n','N')

calc = True

while calc:
    # minimum monthly payment
    if balance < 1000:
        min_monthly_payment = 20
    else:
        min_monthly_payment = balance *0.02
    
    
    #get monthly payment
    print('\n Assuming a 2% of the balance ($ 20 min)')
    print('Your minimum payment would be',
          format(min_monthly_payment, '.2f'), '\n')
    
    response = input('Use minimum monthly payment? (y or n):')

    while response not in yes_response + no_response:
        response = input('Use minimum monthly payment? (y or n):')
        
        
    if response in ('y','Y'):
        monthly_payment = min_monthly_payment
    else:
        acceptable_rate = False
        while not acceptable_rate:
            monthly_payment = int(input('Enter the monthly payment: '))
            
            if monthly_payment < balance *0.02:
                print('Minimum payment of 2% of balance required($' + 
                      str(balance*0.02) + ')')
            elif monthly_payment < 20:
                print('Monthly payment of $20 required')
            else:
                acceptable_rate = True
            
#    check if single payment pays off balance
    if monthly_payment >= balance:
        print('*This payment would pays off your balance*')
    else:
        displayPayments(balance, monthly_int_rate, monthly_payment)

        # calculate another monthly payment
        again = input('\n Recalculate another payment? (y or n) ?')
        
        while again not in yes_response + no_response:
            again = input('\n Recalculate another payment? (y or n) ?')
            
        if again in yes_response:
            calc = True #continue program
            print('\n\n For your current balance of $' + str(balance))
        else:
            calc = False


# display monthly payoff
displayPayments(balance, monthly_int_rate, monthly_payment)
