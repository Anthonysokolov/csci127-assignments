def countPlurals(words):
    return len([w for w in words.split() if w[-1].upper() == 'S'])


def notPossessive(words):
    return len([w for w in words.split() if w[-1].upper() == 'S' 
                and w[-2] != "'"])


tests = ["cats dogs bat's frogs","nothing plural here","","the cat's cradles"]
print('1.1')
print('*******************')
for t in tests:
    print(t,':',countPlurals(t))
print('1.2')
print('*******************')
for t in tests:
    print(t,':',notPossessive(t))