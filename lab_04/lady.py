def happyLadybugs(b):
    b = b.upper()
    b = b.replace("_", " ")
    if len(b) <= 1:
        return "NO"
    else:
        for letter in b:
            i = 0
            counter = 0
            while i < len(b):
                if b[i] == letter:
                    counter = counter + 1
                i = i + 1
            if counter < 2:
                return "NO"
            elif counter >= 2:
                continue
        return "YES"
    return "test"
print(happyLadybugs("RBYRB_BRY"))
print(happyLadybugs("YBRRBY"))
print(happyLadybugs("YBR_RBY"))
