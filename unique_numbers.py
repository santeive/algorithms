def method_one(vals):
    if len(vals) == len(set(vals)):
       return True
    else:
        return False
        
def method_two(vals):
    flag = False
    for i in range(len(vals)):
        for j in range(len(vals)):
            if i != j:
                if vals[i] == vals[j]:
                    flag = True
    return flag

vals = [1,3,6,5]


flag = method_two(vals)
if flag:
    print("Existen valores repetidos")
else:
    print("Todos los valores son unicos")