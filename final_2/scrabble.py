def canMakeWord(letters,word):
    letters = list(letters)
    for l in word:
        if l in letters:
            letters.remove(l)
        else:
            return False
    return True


def withWild(letters,word):
    letters = list(letters)
    for l in word:
        if l in letters:
            letters.remove(l)
        elif '?' in letters:
            letters.remove('?')
        else:
            return False
    return True


tests = [('ladilmy','daily'),('???','any'),('ssjfa;','word'),('','test'),
         ('letranas','rental'),('fi?al','final'),('??','not')]

print('2.1')
print('***************************')
for t in tests:
    print(t,':',canMakeWord(t[0],t[1]))

print('\n2.2')
print('***************************')
for t in tests:
    print(t,':',withWild(t[0],t[1]))