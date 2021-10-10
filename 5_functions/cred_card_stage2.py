# Credit card calculation program(stage 1)

def displayWelcome():
    print('This program displays the time to pay off a credit')
    print('card and the interest paid based on the curent balance,')
    print('the interest rate and monthly payments made.')
    

def displayPayments(balance, int_rate, monthly_payment):
    # init
    num_months = 0
    total_int_paid = 0
    
    # display loan info 
    print('Payoff Schedule')
    print('Credit Card Balance = $'+ format(balance, '.2f'))
    print('Annual interest rate = ' + str(1200* int_rate) + '%')
    print('Monthly Payment = $'+ format(monthly_payment, '.2f'))
    
    # display yearly account status
    while balance > 0:
        monthly_int = balance * int_rate
        total_int_paid = total_int_paid + monthly_int
        balance = balance + monthly_int - monthly_payment
        
        year = (num_months // 12) + 1
        print(year, format(balance, '.2f'), format(total_int_paid, '.2f'))
        
        num_months += 1
    
# main -----

#display welcome screen
displayWelcome()

# get current balance and APR
balance = int(input('\nEnter the balance on your credit card: '))
apr = int(input('Enter the interest rate (APR) on the card: '))

monthly_int_rate = apr/1200

#determine monthly payment
response = input('Use minimum monthly payment? (y or n):')

if response in ('y','Y'):
    if balance < 1000:
        monthly_payment = 20
    else:
        monthly_payment = balance *0.02
else:
    print('User entered monthly payment selected')
    monthly_payment = int(input('Enter the monthly payment: '))
    

# display monthly payoff
displayPayments(balance, monthly_int_rate, monthly_payment)
