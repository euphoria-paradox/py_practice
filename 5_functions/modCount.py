# check for divisibility of range of numbers from 1 to n
# by m

def modCount(n,m):
    # check if divisible
    i = 1
    print('The numbers divisible by', m , 'are: ')
    while i <= n:
        if i % m == 0:
            print(i)
        
        i += 1

n = int(input('Enter the upper limit of numbers: '))
m = int(input('Enter the divisor: '))

modCount(n, m)
