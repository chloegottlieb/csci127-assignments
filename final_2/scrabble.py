def canMakeWord(letters, word):
    letterslow = letters.lower()
    wordlow = word.lower()
    print(letterslow, wordlow)
    if all((wordlow in letterslow) for wordlow in letterslow):
        #print("true")
        return True
    else:
        return False
print(canMakeWord("wolllwety", "yellow"))