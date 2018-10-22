def divide(a,b,u):
    '''
    Divides a cake of u units into equal pieces of a/b units
    '''
    p = a/b
    return int(u/p)

print('1 unit and 5/10 unit pieces:', str(divide(5,10,1)))
print('2 units and 3/17 unit pieces', str(divide(3,17,2)))
print('35 units and 1/3 unit pieces:', str(divide(1,3,35)))