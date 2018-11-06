def happy_ladybugs(b):
    '''
    Returns 'YES' if all of the ladybugs can be made happy
    Returns 'NO' otherwise
    '''
    # If the board has an underscore, check to see if there is
    # more than one of every color ladybug
    if '_' in b:
        b = b.replace('_','')
        # Create a dict to count the amount of every color ladybug
        count = {}
        
        for v in b:
            count.setdefault(v,0)
            count[v] += 1
        # Check if there is more than one of every color ladybug
        for v in count.values():
            if v < 2:
                return 'NO'
        
        return 'YES'
    # If the board has no underscore, check to see if all
    # the ladybugs are already happy
    elif is_full(b):
        return 'YES'
    
    else:
        return 'NO'
    
    
def is_full(b):
    '''
    Checks to see if a game with no underscores is valid
    '''
    # If there is only one ladybug, then it cannot be happy
    if len(b) == 1:
        return False
    
    prev = b[0]
    streak = 1
    
    # Loop through all the ladybugs, if every distinct character is part of a 
    # consecutive substring then all the ladybugs are happy
    
    for i in range(1,len(b)):
        if b[i] == prev:
            streak += 1
        elif streak > 1:
            if i == len(b) -1:
                return False
            prev = b[i]
            streak = 1
        else:
            return False
    return True


games = ['AABBCC','AABCBC','A','__','A__A','B__BG','RADA_D_R',
         'CC_DDD_FGFGC_C']

for g in games:
    print(g,'->',happy_ladybugs(g))        


