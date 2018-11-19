def makeacronym(w):
    acronym = []
    firstletter = w[0]
    #acronym.append(firstletter)
    breakchar = ' '
    for word in w.split():
        if breakchar == ' ':
            nextfirstlet = word[0]
        acronym.append(nextfirstlet)
        #word = word + 1
    acronew = ''.join(acronym)
    return acronew
print(makeacronym('shaking my head'))