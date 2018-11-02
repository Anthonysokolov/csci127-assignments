def happy_ladybugs(b):
    values = distinct_values(b)
    
    if '_' in values:
        values.remove('_')
        for v in values:
            count = 0
            for c in b:
                if v == c:
                    count += 1
            if count <= 1:
                return 'NO'
        return 'YES'
    
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


def distinct_values(l):
    distinct = []
    for c in l: 
        if c not in distinct:
            distinct.append(c)
    
    return distinct


games = ['AABBCC','AABCBC','A','__','A__A','B__BG','RADA_D_R',
         'CC_DDD_FGFGC_C']

for g in games:
    print(g,'->',happy_ladybugs(g))        
        
    
