# Madison Chen & Anthony Sokolov

import random

# Madlib sentence
sentence =  '<NAME> goes to <PLACE> in order to <VERB> their <NOUN> and eat some <FOOD> at <NUMBER> in the morning.'
# Options for filling in words
names = ['John', 'Cena', 'Billy', 'Erica']
places = ['hell', 'school','New York','subway']
verbs = ['program','review','watch','enjoy']
nouns = ['computer','classroom','iPhone','iPad','Russian brother']
foods = ['bananas','apples','sushi','pizza','pickles']
numbers = ['4','3','28','7']


fills  = ['<NAME>','<PLACE>','<VERB>','<NOUN>','<FOOD>','<NUMBER>']
words = [names,places,verbs,nouns,foods,numbers]

def madlib(s):
    '''
    Takes in a sentence and replaces designated words marked with '<>'
    '''
    out = []
    for w in s.split():
        if w in fills:
            ind = fills.index(w)
            out.append(words[ind][random.randint(0, len(words[ind])-1)])
        else:
            out.append(w)
    return ' '.join(out)

print(madlib(sentence))