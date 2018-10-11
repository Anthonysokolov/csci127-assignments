def filterodd(l):
    '''
    Returns only the odd values from a list l
    '''
    out = []
    for item in l:
        if item % 2 == 1:
            out.append(item)
            
    return out
            
    
def mapsquare(l):
    '''
    Returns a list with the square of each value in a list l
    '''
    out = []
    for item in l:
        out.append(item*item)
        
    return out

l = list(range(-5,5))
print('filterodd of',str(l),':',str(filterodd(l)))
print('mapsquare of',str(l),':',str(mapsquare(l)))
