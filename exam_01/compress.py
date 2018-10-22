def compress_word(w):
    w.lower()
    vowels = ['a','e','i','o','u']
    findFIrst = w[0]
    nonVowels = []
    i = 0
    for i in w:
        if i not in vowels:
            nonVowels.append(i)
            newWord = "".join(nonVowels)
        elif w[:1] in vowels:
            nonVowels.append(i)
            newWordWOFirst = "".join(nonVowels)       
    return newWord
print(compress_word('apple'))
print(compress_word('green'))

#def sentence(line):
#    Sentence = list(sentence)
#    w = Sentence[0]
#    newSentence = []
#    for w in line:
#        wrd = compress_word(w)
#        newestSentence = newSentence.append(wrd)
       # newerSentence = " ".join(newestSentence)
#    return wrd
#print(sentence("hi my name is chloe and i like apples"))