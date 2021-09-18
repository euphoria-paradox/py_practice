# sum of numbers 

cont = True
sums = 0 

while cont:
    num = int(input('Enter a positive integer: '))
    if num >= 1 and num <= 100:
        sums += num
    else:
        continue
    
    choice = input('Continue? (y or n): ')
    if choice == 'n':
        cont = False
    else:
        cont = True
        
print('Sum is',sums)