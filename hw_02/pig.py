#Chloe Gottlieb and Sam Ebersole
def piglatinify(word):
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        return word + 'ay'
    else:
        pig = word[1:] + word[0] + 'ay'
        return pig
print(piglatinify('ate'))
print(piglatinify('hello'))