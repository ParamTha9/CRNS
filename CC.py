def encrypt(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            shifted_index = (index + shift) % 26
            result = result +alphabet[shifted_index]
        else:
            result = result + char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = "hello world"
s = 3
enc = encrypt(msg, s)
dec = decrypt(enc, s)

print("Encrypted:", enc)
print("Decrypted:", dec)
