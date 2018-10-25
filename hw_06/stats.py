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


def freq(l, num):
    '''
    Finds the frequency of a value in a list
    '''
    count = 0
    for i in l:
        if i == num:
            count += 1
            
    return count


l1 = rand_list(100,-10000,10000)
l2 = rand_list(100, 1,50)

print('Max value:', str(find_max(l1)), ', Index:', str(max_index(l1)))
print('Max value:', str(find_max(l2)), ', Frequency:', str(freq(l2, find_max(l2))))

