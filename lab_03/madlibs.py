# Madison Chen & Anthony Sokolov

import random

sentence =  '<NAME> goes to <PLACE> in order to <VERB> their <NOUN> and eat some <FOOD> at <NUMBER> in the morning.'
names = ['John', 'Cena', 'Billy', 'Erica']
places = ['hell', 'school','New York','subway']
verbs = ['program','review','watch','enjoy']
nouns = ['computer','classroom','iPhone','iPad','Russian brother']
foods = ['bananas','apples','sushi','pizza','pickles']
numbers = ['4','3','28','7']


fills  = ['<NAME>','<PLACE>','<VERB>','<NOUN>','<FOOD>','<NUMBER>']

def madlib(s):
    out = []
    for w in s.split():
        if w == '<NAME>':
            out.append(names[random.randint(0,len(names)-1)])
        elif w == '<PLACE>':
            out.append(places[random.randint(0,len(places)-1)])
        else:
            out.append(w)
    return ' '.join(out)

print(madlib(sentence))