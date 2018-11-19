letters = ['AEIOULNRST','DG','BCMP','FHVWY','K','JX','QZ']
values = [1,2,3,4,5,8,10]

scores = {}
for k,v in zip(letters,values):
    for c in k:
        scores[c] = v
        
        
def score(w):
    '''
    Returns the word score for a word w
    '''
    out = 0
    for c in w:
        out += scores[c.upper()]
        
    return out


tests = ['hello','test','quartz','xylophone','jetski','']

for t in tests:
    print(t,'->',score(t))