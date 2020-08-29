def minmax(values):
    values.sort()
    return (values[0], values[-1])

def min_max(values):
    ma_x = min_x = values[0]
    for val in values:
        if val > ma_x:
            ma_x = val
        elif val < min_x:
            min_x = val
            
    return (min_x, ma_x)

values = [11,12,14,2,4,100,6,3,1,345,342,764,24,0,5]
print( min_max(values) )
