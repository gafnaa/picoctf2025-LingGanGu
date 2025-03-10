def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = pow(a, -1, 26)  # Modular inverse of a modulo 26
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')  # Convert letter to number (0-25)
            x = (a_inv * (y - b)) % 26  # Decryption formula
            plaintext += chr(x + ord('A'))  # Convert number back to letter
        else:
            plaintext += char
    return plaintext

ciphertext = "MZDRAQKZQARQKTPGZBEKD"

# Possible values for a (must be coprime with 26)
possible_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

# Try all combinations of a and b
for a in possible_a:
    for b in range(26):
        decrypted = affine_decrypt(ciphertext, a, b)
        print(f"a = {a}, b = {b}: {decrypted}")