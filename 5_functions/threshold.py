# check for the values in a list greater than some threshold

def greaterValues(values, threshold_value):
    
    greatValues = []
    for i in values:
        if i > threshold_value:
            greatValues.append(i)
        
    print(greatValues)
    

values = [1, 4,7,5,10,56,78,3, 15, 15]
threshold_value = int(input('Enter the threshold: '))
greaterValues(values, threshold_value)
