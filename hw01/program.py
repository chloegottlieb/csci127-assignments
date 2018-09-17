def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    result = name.upper()
    return result

print(capitalize("chloe gottlieb"))

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    firstChar = name[0]
    capFirstChar = firstChar.upper()
    spaceIndex = name.find(" ")
    lastName = name[spaceIndex+1:]
    capLastName = lastName.upper()
    result = capFirstChar + '. ' + capLastName
    return result

print(init("chloe gottlieb"))

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    pig = name[1:] + name[0] + 'ay'
    return pig

print(part_pig_latin('computer'))

def make_out_word(out, word):
  result = out[:2] + word + out[2:]
  return result

print(make_out_word('(())', 'science'))

def make_tags(tag, word):
  result = '<' + tag + '>' + word + '</' + tag + '>'
  return result

print(make_tags('h1', 'Website'))
