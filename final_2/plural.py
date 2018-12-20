def countPlurals(line):
    newline = line.lower()
    #word = line.split()
    words = newline.split()
    lastLetters = []
    print(words)
    
    for word in words:
        lastLet = word[-1:]
        lastLetters.append(lastLet)
    print(lastLetters)
    plurals = lastLetters.count('s')
    return plurals
print(countPlurals('the brothers were waiting for their sisters and parents'))

def notPossesive(line):
    newline = line.lower()
    words = newline.split()
    print(words)
    lastLetters = []
    for word in words:
        secondtolast = word[-2:]
        secondtolastchar = secondtolast[0]
        print(secondtolastchar)
        if secondtolastchar == "'":
            words.remove(word)
        lastLet = word[-1:]
        lastLetters.append(lastLet)
    print(lastLetters)
    plurals = lastLetters.count('s')
    return plurals
print(notPossesive("the girl's parents were late several times"))