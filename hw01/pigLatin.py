def pigLatin(word):

    #vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 'aeiou'
    
    if word[0].lower() in vowels:
        return word + 'ay'
    else:
        pig = word[1:] + word[0] + 'ay'
        return pig
print(pigLatin('ate'))