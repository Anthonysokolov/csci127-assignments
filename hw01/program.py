def capitalize(name):
    s = name.find(' ')
    first = name[:s]
    last = name[s+1:]
    
    first = first[0].upper() + first[1:]
    last = last[0].upper() + last[1:]
    
    return first + ' ' + last

print(capitalize('james bond'))

def init(name):
    s = name.find(' ')
    first = name[0].upper()
    last = name[s+1:].capitalize()
    
    return first + '. ' + last

print(init('James Bond'))

def part_pig_latin(name):
    return name[1:] + name[0] + 'ay'

print(part_pig_latin('hello'))

def make_out_word(out, word):
    return out[:2] + word + out[2:]

print(make_out_word('<<>>','Yay'))

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

print(make_tags('i','hello'))
