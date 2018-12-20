def addline(d,line):
    
    lineLower = line.lower()
    words = lineLower.split()
    
    for word in words:
        firstLet = word[0]
        values = d.values()
        keys = d.keys()
        key = firstLet
        d.setdefault(firstLet, word)
        if any((firstLet in keys) for firstLet in keys):
            d[firstLet] = word
    return d


print(addline({}, "hi there my name is Chloe this is the Computer Science final"))
print(addline({}, "the semester is just about over"))
print(addline({}, "I am almost done with this exam"))
print(addline({}, "it is very cold out today"))
finaldict = print(addline({}, "this building is part of Hunter College located in Manhattan New York"))

## I was working on a function so that each add line becomes part of the main dictionary. Also I'm aware the new values override the old per letter (if each letter matches  an existing key) i forgot the function to "append" for a dictionary so i just updated.

def spellcheck(d, word):
    newword = word.lower()
    print(newword)
    
    keys = d.keys()
    if all((newword in d) for newword in d):
        return True
    else:
        return False
print(spellcheck(finaldict, "COLD"))

