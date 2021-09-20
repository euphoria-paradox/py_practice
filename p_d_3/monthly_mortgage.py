# Home Loan Amortization

# This program calculates the monthly mortgage payments for a given loan amount
# term and range of interests from  3 to 18%

# the formula for determinig  the mortgage is A/D
# A - original loan amount 
# D - discount factor given by D = ((1+r)^n -1)/r(1+r)^n

# n- number of payments, r-interest rate expressed in decimal divided by 12


# Greet 
print(format('Welcome to Monthly Mortgage calculator', '-^44'))

# get input for loan amount and term(number of years)
A = float(input('Enter the loan amount: $'))
term = int(input('Enter the term of loan amount: ')) # no of years


# interest rates are from 3 to 18%
# calculate the mortgage 

interest_rate = 3

blank_char = ' '

header = 'Loan Amount: $' + str(A) + '  Term: ' + str(term) + ' years\n'

blank_spaces = str(len(header)- 28)  # for proper alignment 

print('\nLoan Amount: $' + str(A) + '  Term: ' + str(term) + ' years\n')
print('Interest Rate' + format(blank_char, blank_spaces) + 'Monthly Payment\n')

'''
n = term * 12
r = (interest_rate/100)/12
num = (1 + r)**n - 1
denom = r
print(num)
'''

while interest_rate <= 18:
    n = term * 12
    r = (interest_rate/100)/12
    D = ((1 + r)**n - 1) / (r*(r + 1)**n)
    monthly_payment = A/D                       # monthly mortgage
    if interest_rate < 10:
        print(format(blank_char,'5') + str(interest_rate) + '%' +
              format(blank_char,'21') + str(format(monthly_payment,'.2f')) + '\n')
    else:
        print(format(blank_char,'5') + str(interest_rate) + '%' +
              format(blank_char,'20') + str(format(monthly_payment,'.2f')) + '\n')
    
    interest_rate += 1
    

   
