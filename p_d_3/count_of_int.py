# display of number of positive and negative integers entered.

pos_int = 0
neg_int = 0

condition = True

while condition:
    num = int(input('Enter the integer: '))
    if num > 0:
        pos_int += 1
    elif num < 0:
        neg_int += 1
    elif num == 0:
        continue
    
    choice = input('Continue(y or n)?')
    if choice == 'n':
        condition = False
        

# output
print('The number of positive integers entered are:',pos_int,
      '\n The number of negative integers entered are:',neg_int)
