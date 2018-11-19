def encode(s):
    '''
    Encodes a string s using run length encoding by
    returning a list with each included letter and its count
    '''
    if len(s) == 0:
        return []
    
    count = 0
    i = 0
    out = []
    prev = s[0]
    
    while i < len(s):
        if s[i] == prev:
            count += 1
        else:
            out.append([prev,count])
            prev = s[i]
            count = 1
        i += 1
    out.append([prev,count])
        
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

