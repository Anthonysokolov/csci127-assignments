# Partners: Anthony Sokolov & Jia Qi He

def mysqrt(i):
    guess = 1
    while guess*guess != i:
        oldGuess = guess
        guess = (guess + (i/guess))/2
        if round(oldGuess, 5) == round(guess, 5):
            break
    return round(guess, 5)

i = 1
while i <= 16:
    print(i, ":", mysqrt(i))
    i = i + 1