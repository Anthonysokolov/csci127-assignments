# Kushendra Ramrup and Anthony Sokolov

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result


def next_word_dict(s):
    out = {}
    s = s.split()
    
    for i in range(len(s)-1):
        out.setdefault(s[i],[])
        out[s[i]].append(s[i+1])
    
    return out

file="moby-medium.txt"
f = open(file)
s = clean_data(f.read())
f.close()

next_words = next_word_dict(s)
print(next_words)
        
