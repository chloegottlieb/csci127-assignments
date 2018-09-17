def pigLatin(word):
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return word + 'ay'
    else:
        pig = word[1:] + word[0] + 'ay'
        return pig
print(pigLatin('ate'))
<<<<<<< HEAD
print(pigLatin('hello'))
=======
>>>>>>> 8e887deb765a33c38a585a093e04ba4c16a64ac5
