def addline(d,line):
    line = line.lower()
    k = line[0]
    if k in d.keys():
        d[k].append(line)
    else:
        d[k] = [line]
    return d


def spellcheck(d, word):
    word = word.lower()
    k = word[0]
    
    if k in d.keys():
        if word in d[k]:
            return True
    return False

d = {}
inputs = ['word','test','window','final','soccer']
for i in inputs:
    d = addline(d,i)
    
print('Dictionary:\n',d)
print('\nSpellcheck:')
    
tests = ['word','false','finals','window','xylophone']
for t in tests:
    print(t,':',spellcheck(d,t))