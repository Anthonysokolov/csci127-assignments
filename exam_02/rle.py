def encode(s):
    '''
    Encodes a string s using run length encoding by
    returning a list with each included letter and its count
    '''
    count = {}
    for l in s:
        count.setdefault(l,0)
        count[l] += 1
    
    out = []
    for k,v in count.items():
        out.append([k,v])
        
    return out


def decode(s):
    '''
    Decodes a list s using run length encoding
    '''
    out = ''
    for l in s:
        out += l[0]*l[1]
    return out
        

testen = ['test','alasdfjalds','aaaaaaaaaaaddddddddssdf','']
testde = []

print('ENCODE TEST')
for t in testen:
    print(t,'->',encode(t))
    testde.append(encode(t))
    
print('\nDECODE TEST')
for t in testde:
    print(t,'->',decode(t))

