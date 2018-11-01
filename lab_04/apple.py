def countApplesAndOranges(s,t,a,b,apples,oranges):
    '''
    Counts the number of apples and oranges that fall into a 
    range [s,t]
    '''
    apple_count = 0
    orange_count = 0
    
    for i in apples:
        pos =  a + i
        if pos >= s and pos <= t:
            apple_count += 1
    
    for i in oranges:
        pos = b + i
        if pos >= s and pos <= t:
            orange_count += 1
    
    print(apple_count)
    print(orange_count)
    

print('Case:')
print('House position: [7,11], Apple tree: 5,\nOrange tree: 15, Apples: [-2,2,1], Oranges: [5,-6]\n')
print('Results:')
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])


print('\nCase:')
print('House position: [-9,-5], Apple tree: -12,\nOrange tree: -3, Apples: [4,3,-2,10], Oranges: [-3,4,-1]\n')
print('Results:')
countApplesAndOranges(-9,-5,-12,-3,[4,3,-2,10],[-3,4,1])