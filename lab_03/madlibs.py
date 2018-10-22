# Madison Chen & Anthony Sokolov

import random

# Madlib sentence
sentence =  '''<NAME> goes to <PLACE> in order to <VERB> their <NOUN> and eat some <FOOD> at
                <NUMBER> in the morning. Later <HERO> gets in a fight with <NAME> over the <FOOD>
                which they spilled. <HERO> barely wins the fight, and goes to <PLACE> to <VERB> <PNOUN> afterwards'''

# Options for filling in words
names = ['John', 'Cena', 'Billy', 'Erica']
places = ['hell', 'school','New York','subway','Chipotle','home','Argentina','The Matrix']
verbs = ['program','review','watch','enjoy','relax','impeach']
nouns = ['computer','classroom','iPhone','iPad','Russian brother','computer','brain','verb']
foods = ['bananas','apples','sushi','pizza','pickles','burrito']
numbers = ['4','3','28','7','3.1415']
heroes = ['Batman','Shrek','Spongebob','Spiderman','Bob']
pnouns = [word+'s' for word in nouns]


fills  = ['<NAME>','<PLACE>','<VERB>','<NOUN>','<FOOD>','<NUMBER>','<PNOUN>']
words = [names,places,verbs,nouns,foods,numbers,pnouns]

def madlib(s):
    '''
    Takes in a sentence and replaces designated words marked with '<>'
    '''
    out = []
    hero = heroes[random.randint(0,len(heroes)-1)]
    
    for w in s.split():
        if w in fills:
            ind = fills.index(w)
            out.append(words[ind][random.randint(0, len(words[ind])-1)])
        elif w == '<HERO>':
            out.append(hero)
        else:
            out.append(w)
    return ' '.join(out)

print(madlib(sentence))