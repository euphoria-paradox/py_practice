# check wheather entered integers are in ascending order

def ordered3(a, b, c):
    if a < b and b < c:
        print('True')
    elif a > b or b > c:
        print('False')