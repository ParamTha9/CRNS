# Step 1: Greatest Common Divisor (GCD) using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Step 2: Compute modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    d_old, d = 0, 1
    r_old, r = phi, e
    while r != 0:
        quotient = r_old // r
        d_old, d = d, d_old - quotient * d
        r_old, r = r, r_old - quotient * r
    return d_old % phi  # Ensure the result is positive

# Step 3: Check if a number is prime (used only for demo)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Step 4: Key Generation
def generate_keys():
    # Choose two prime numbers (small for simplicity)
    p = 61
    q = 53

    # Calculate n = p * q (modulus)
    n = p * q

    # Calculate totient φ(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < φ(n), and e and φ(n) are coprime
    e = 17  # Common choice
    if gcd(e, phi) != 1:
        raise ValueError("e and phi are not coprime")

    # Calculate d (modular inverse of e mod φ(n))
    d = mod_inverse(e, phi)

    # Return public and private keys
    return (e, n), (d, n)

# Step 5: Encryption function
def encrypt(msg, public_key):
    e, n = public_key
    # Encrypt each character using: c = (m^e) mod n
    cipher = [pow(ord(char), e, n) for char in msg]
    return cipher

# Step 6: Decryption function
def decrypt(cipher, private_key):
    d, n = private_key
    # Decrypt each character using: m = (c^d) mod n
    msg = ''.join([chr(pow(char, d, n)) for char in cipher])
    return msg

# Step 7: Usage example
public_key, private_key = generate_keys()

message = "hello"

cipher = encrypt(message, public_key)
decrypted = decrypt(cipher, private_key)

# Step 8: Output results
print("Original message:", message)
print("Encrypted (numeric):", cipher)
print("Decrypted message:", decrypted)
