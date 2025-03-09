from Crypto.Util.number import long_to_bytes, inverse
from sympy import factorint

# Diberikan
N = 20678530596164170484781526079001536389832697538175401903953471660681415670468791803515841251146671799807504490870956068973963480841909243261079323545765418
e = 65537
ciphertext = 18427020265758898678944636001604262108288842913870365923835511707930914487938976177256349268999827847566275443209774888335110004327432289001889424655623585

# Faktorisasi N untuk mendapatkan p dan q
factors = factorint(N)
p, q = list(factors.keys())

# Hitung phi(N)
phi = (p - 1) * (q - 1)

# Hitung d (modular inverse dari e terhadap phi)
d = inverse(e, phi)

# Dekripsi ciphertext
plaintext = pow(ciphertext, d, N)

# Konversi ke string
flag = long_to_bytes(plaintext)
flag.decode()