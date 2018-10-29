import random

def build_random_list(num_items, max_value):
    l=[]

    for i in range(num_items):
        l = l + [ random.randrange(0,max_value) ]
    return l
l = build_random_list(100,10)
print(l)

def index_largest(l):
    li = 0
    for i in range(1,len(l)):
        if l[i] > l[li]:
            li = i
    return li

def max(l): 
    li = index_largest(l)
    return li
print(max(l))

def freq(l, val):
    count = len([i for i in l if i == val])
    return count
print(freq(l, 5))

def mode(l):
    frequencies = []
    frequencies.append(freq(l,0))
    frequencies.append(freq(l,1))
    frequencies.append(freq(l,2))
    frequencies.append(freq(l,3))
    frequencies.append(freq(l,4))
    frequencies.append(freq(l,5))
    frequencies.append(freq(l,6))
    frequencies.append(freq(l,7))
    frequencies.append(freq(l,8))
    frequencies.append(freq(l,9))
    frequencies.append(freq(l,10))
    #print(frequencies)
    my_max = frequencies[0]
    for num in frequencies:
        if my_max < num:
            my_max = num
    #print(my_max)
    if my_max == frequencies[0]:
        return 0
    elif my_max == frequencies[1]:
        return 1
    elif my_max == frequencies[2]:
        return 2
    elif my_max == frequencies[3]:
        return 3
    elif my_max == frequencies[4]:
        return 4
    elif my_max == frequencies[5]:
        return 5
    elif my_max == frequencies[6]:
        return 6
    elif my_max == frequencies[7]:
        return 7
    elif my_max == frequencies[8]:
        return 8
    elif my_max == frequencies[9]:
        return 9
    elif my_max == frequencies[10]:
        return 10
print(mode(l))
    