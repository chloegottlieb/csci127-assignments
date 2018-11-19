def score(w):
    scrabdict = {'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1, 'T':1, 'D':2, 'G':2, 'B':2, 'C':2, 'M':2, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q': 10, 'Z':10}
    word = w.upper()
    letters = []
    values = []
    #searchletter = word[0]
    #lets = word.split()
    #letters.append(lets)
    i = 0
    for letter in word:
        searchletter = word[i]
        if searchletter in scrabdict.keys():
            letters.append(searchletter)
            value = scrabdict.get(searchletter)
            values.append(value)
    i = i + 1
    #print(letters)
    return values
print(score('ate'))