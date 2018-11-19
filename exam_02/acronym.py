def makeacronym(w):
    '''
    Takes in a string w and returns the acronym formed
    by taking the first letter of every word
    '''    
    return ''.join([s[0] for s in w.split()])


tests = ['laugh out loud','acronym','to be honest','']

for t in tests:
    print(t,'->',makeacronym(t))