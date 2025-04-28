import numpy as np

def make_matrix(key):
    key = key.lower().replace('j', 'i')
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = ''
    for char in key + alphabet:
        if char not in matrix and char in alphabet:
            matrix = matrix+char
    return [matrix[i:i+5] for i in range(0, 25, 5)]








def playfair_encrypt(text, key):
    matrix = make_matrix(key)
    pairs = format_text(text)
    return ''.join(encrypt_pair(pair, matrix) for pair in pairs)
    
msg = "balloon"
key = "monarchy"
encrypted = playfair_encrypt(msg, key)
print("Encrypted:", encrypted)