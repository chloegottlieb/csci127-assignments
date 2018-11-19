def encode(s):
    let_count = {}
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newstr = s.upper()
    neweststr = newstr.split()
    for letter in neweststr:
        firstlet = neweststr[0]
        let_count[neweststr] = 1
    return let_count
print(encode('adshf'))
    