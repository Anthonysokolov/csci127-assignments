# Anthony Sokolov & Eric Dittus

def piglatinify(word):
    first_letter = word[0]
    if first_letter in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + first_letter + 'ay'
    
a = 'apple'
b = 'banana'

print('Vowel test case:',a,'->',piglatinify(a))
print('Consonant test case:',b,'->',piglatinify(b))