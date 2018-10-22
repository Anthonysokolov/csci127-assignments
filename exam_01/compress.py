def compress_word(s):
    '''
    Removes the vowels from a word
    '''
    out = ''
    for i in s:
        if i.lower() not in 'aeiou':
            out += i.lower()
    
    return out


print('2.1')
for w in ['halloween','Special','apple']:
    print(w,'->',compress_word(w))
    
    
def sentence(line):
    '''
    Removes the vowels from every word in a sentence
    '''
    out = []
    for w in line.split():
        out.append(compress_word(w))
    
    return ' '.join(out)

print('2.2')
for s in ['I like to eat apple pie','Who is there','Chicken wings are awesome']:
    print(s,'->',sentence(s))
    


    