def make_matrix(key):
    key = key.lower().replace('j', 'i')
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = ''
    for char in key + alphabet:
        if char not in matrix and char in alphabet:
            matrix = matrix + char
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def format_text(text):
    text = text.lower().replace('j', 'i')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            pairs.append(a + 'x')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    if len(pairs[-1]) == 1:
        pairs[-1] = pairs[-1] + 'x'
    print(pairs)
    return pairs

def encrypt_pair(pair, matrix):
    flat = ''.join(matrix)
    a, b = pair
    ra, ca = divmod(flat.index(a), 5)
    rb, cb = divmod(flat.index(b), 5)

    if ra == rb:
        return matrix[ra][(ca+1)%5] + matrix[rb][(cb+1)%5]
    elif ca == cb:
        return matrix[(ra+1)%5][ca] + matrix[(rb+1)%5][cb]
    else:
        return matrix[ra][cb] + matrix[rb][ca]

def playfair_encrypt(text, key):
    matrix = make_matrix(key)
    pairs = format_text(text)
    return ''.join(encrypt_pair(pair, matrix) for pair in pairs)

msg = "balloon"
key = "monarchy"
encrypted = playfair_encrypt(msg, key)
print("Encrypted:", encrypted)