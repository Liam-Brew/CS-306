import sys as sys

def calc_n(p, q):
    return p * q

def calc_phi(p, q):
    return (p - 1) * (q - 1)

def modexp(base, exponent, modulus):
    if modulus == 1:
        return 0

    result = 1
    base = base % modulus    

    while exponent > 0:
        if (exponent & 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result

def RSA_enc(plaintext, key):
    # key should be a tuple (n, e)
    # ord() function is useful
    # recommend extracting the components of the key from the tuple for efficiency purposes
    # return list of integers

    _k = key[1]
    _n = key[0]
    result = []

    for c in plaintext:
        #encrypt each letter in the plaintext
        #ord will five the ascii value of a string/letter
        result += [modexp(ord(c), _k, _n)]

    return result

def RSA_dec(ciphertext, key):
    # key should be a tuple (n, e)
    # chr() function is useful
    # recommend extracting the components of the key from the tuple for efficiency purposes
    # return a string

    _k = key[1]
    _n = key[0]
    result = ""

    for c in ciphertext:
        #chr will return the string representation of an integer
        result += chr(modexp(c, _k, _n))
    return result

def test():
    n = calc_n(test_p, test_q)
    private = [n, test_d]
    public = [n, test_e]


test()
