l = [2, 4, 2, 7, 3 , 8, 23, 4, 9]

def filterodd(l):
    odds = []
    for i in l:
        if (i%2)==1:
            odds.append(i)
    return odds

print(filterodd(l))

def mapsquare(l):
    squared = []
    for i in l:
        i2 = i**2
        squared.append(i2)
    return squared

print(mapsquare(l))