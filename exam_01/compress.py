def compress_word(w):
    
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
 #   Sentence = sentence.split()
  #  w = Sentence[0]
   # for w in line:
    #    wrd = compress_word(w)
       # newestSentence = newSentence.append(compress_word(w))
        #newerSentence = " ".join(newestSentence)
   # return wrd
#print(sentence("hi my name is chloe and i like apples"))