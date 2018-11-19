def score(w):
    scrabdict = {'AEIOULNRST':1, 'DG':2, 'BCMP':3, 'FHVWY':4, 'K':5, 'JX':8, 'QZ':10}
    word = w.upper()
    letters = []
    searchletter = word[1]
    #lets = word.split()
    #letters.append(lets)
    for letter in scrabdict.keys():
        letters.append(letter)
    return letters
print(score('hello'))