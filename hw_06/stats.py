# Christopher He & Anthony Sokolov
import random

def rand_list(size, min, max):
    '''
    Generates a random list
    '''
    out = []
    for i in range(size):
        out.append(random.randint(min,max))
    return out


def find_max(l):
    '''
    Finds the maximum value of a list
    '''
    max = -99999999
    for i in l:
        if i > max:
            max = i
    
    return max


def max_index(l):
    '''
    Finds the index of the first occurence of a list's maximum value
    '''
    max = find_max(l)
    count = 0
    for i in l:
        if i == max:
            return count
        count += 1


def max_freq(l):
    '''
    Finds the frequency of the maximum value of a list
    '''
    max = find_max(l)
    count = 0
    for i in l:
        if i == max:
            count += 1
            
    return count


l = rand_list(100,1,10)

print('Max value:', str(find_max(l)), ', Index:', str(max_index(l)))
print('Max value:', str(find_max(l)), ', Frequency:', str(max_freq(l)))

