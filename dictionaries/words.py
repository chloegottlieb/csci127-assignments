

def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

filename="/home/chloe/csci127-assignments/dictionaries/moby.txt"
f = open(filename)
s = f.read()
words_uncleaned = build_word_counts(s)
#print(words_uncleaned)
cleaned_string = clean_data(s)
#print("-------------------")
words = build_word_counts(cleaned_string)
#print(words)
vals = words.values()
vals = sorted(vals)
#print("-----------")

common_words = [ [k,words[k]] for k in words if words[k] > 50 ]
#print(common_words)

word_search = [ ['call', words['call']] for call in words]
#print(word_search)
call_count = word_search[0]
words_count_dict = {}
words_count_dict.update(call_count)
print(words_count_dict)