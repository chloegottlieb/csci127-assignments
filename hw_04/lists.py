import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
l = build_random_list(8, 18)
print(l)

def locate(l, value):
    if value in l:
        i = 0
        while i < len(l):
            if l[i] == value:
                i = i + 1
                return i
            i = i + 1
    else:
        return -1
print(locate(l, 6))

def count(l,value):
    if value in l:
        i = 0
        val = 0
        while i < len(l):
            if l[i] == value:
                val = val + 1
            i = i + 1
        return val
    else:
        print("value not found in list")
print(count(l, 6))

def reverse(l):
    i = 0
    j = len(l)-1
    while i < j:
        l[i],l[j] = l[j],l[i]
        i = i + 1
        j = j - 1
    return l
print(reverse(l))

def isIncreasing(l):
    val = l[0]
    for element in l:
        if element < val:
            return False
        val = element
    return True
print(isIncreasing(l))

def palindrome(l):
    i = 0
    for element in l:
        if element != l[i-1]:
            return False
        i = i - 1
    return True
print(palindrome(l))
