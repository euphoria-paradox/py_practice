# average of maximum from each row program

def avg(max1, max2, max3):
    return (max1 + max2 + max3)/3.0


values = [[10, 20, 25],
          [5, 15, 35],
          [20, 30, 25]]

n1 = max(values[0])
n11 = 20
n12 = 30
n2 = max(values[1])
n3 = max(values[2])

result = avg(avg(n1,n11,n12), n2, n3)
print(result)