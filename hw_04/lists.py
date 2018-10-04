import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l


print('Random List:', build_random_list(5,10))


def locate(l, value):
    '''
    Accepts a list l and returns the index of value
    Returns -1 if value not in l
    '''
    for i in range(len(l)):
        if l[i] == value:
            return i
    return -1


l = ['a','b','c','d','e']
value = 'b'
print('Locate ' + value + ' in ' + str(l) + ': ' + str(locate(l,value)))
value = 'g'
print('Locate ' + value + ' in ' + str(l) + ': ' + str(locate(l,value)))


def count(l,value):
    '''
    Accepts a list l and return the amount of times value appears in l
    '''
    c = 0
    for item in l:
        if item == value:
            c += 1
    return c


l = ['a','a','b','a','d','e']
value = 'a'
print('Count of ' + value + ' in ' + str(l) + ': ' + str(count(l,value)))


def reverse(l):
    '''
    Returns a list l in reverse order
    '''
    rev = []
    for i in range(1, len(l) + 1):
        rev.append(l[-i])
    
    return rev


print('Reversal of ' + str(l) + ': ' + str(reverse(l)))


def isIncreasing(l):
    '''
    Returns True if a list l is strictly increasing
    Returns False if it is not
    '''
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            continue
        else:
            return False
    return True


l = [-5,-2,0,1,6,700]
print('Is ' + str(l) + ' increasing?: ' + str(isIncreasing(l)))
l = [14,-2,3,1,18,700]
print('Is ' + str(l) + ' increasing?: ' + str(isIncreasing(l)))


def palindrome(l):
    '''
    Returns True if a list l is a palindrome, False if it is not
    '''
    if l == reverse(l):
        return True
    else:
        return False


l = [1,2,'a',2,1]
print('Is ' + str(l) + ' a palindrome?: ' + str(palindrome(l)))
l = [1,'a',3,'b',4]
print('Is ' + str(l) + ' a palindrome?: ' + str(palindrome(l)))
    
