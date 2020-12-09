import random

# For the lab, complete modexp(), RSA_enc(), and RSA_dec().
# HW 2 will allow you to submit the fully completed code from the lab,
#   as well as egcd(), mulinv(), and keygen(), for extra credit on the
#   assignment.
# You must work independently since this assignment will be part of HW 2.

# test constants
test_p = 23
test_q = 47
test_e =  35
test_d = 347
message = "Hello world!"

def calc_n(p, q):
    # do not modify!
    return p * q

def calc_phi(p, q):
    # do not modify!
    return (p - 1) * (q - 1)

def modexp(b, e, m):
    #b^e % m
    if m == 1:
        return 0

    result = 1
    b = b % m    

    while e > 0:
        if e % 2 == 1:
            result = (result * b) % m
        e = e >> 1
        b = (b * b) % m

    return result

def RSA_enc(plaintext, key):
    _k = key[1]
    _n = key[0]
    result = []

    for c in plaintext:
        #encrypt each letter in the plaintext
        #ord will five the ascii value of a string/letter
        result += [modexp(int(ord(c)), _k, _n)]

    return result

def RSA_dec(ciphertext, key):
    _d = key[1]
    _n = key[0]
    result = ""

    for c in ciphertext:
        #chr will return the string representation of an integer
        result += chr(modexp(c, _d , _n))
    return result

def test():
    # do not modify!
    n       = calc_n(test_p, test_q)
    private = [n, test_d]
    public  = [n, test_e]
    
    print("Public key:",public)
    print("Private key:",private)
    
    ciphertext = RSA_enc(message,public)
    plaintext  = RSA_dec(ciphertext,private)

    print("Original message:",message)
    print("Encrypted message:",ciphertext)
    print("Decrypted message:",plaintext)

# === Below this comment is the portions of this assignment that contribute to HW 2 ===

def egcd(b, n):
    (g_0, g) = (b, n)
    (x_0, x) = (1, 0)
    (y_0, y) = (0, 1)

    while g != 0:
        result = g_0 // g
        (g_0, g) = (g, g_0 - (result * g))
        (x_0, x) = (x, x_0 - (result * x))
        (y_0, y) = (y, y_0 - (result * y))
    
    return (g_0, x_0, y_0)

def mulinv(e, n):
    euc = egcd(e, n)
    if euc[0] == 1:
        if euc[1] > 0:
            return euc[1]
        return euc[1] + n

def checkprime(n, size):
    # do not modify!
    # determine if a number is prime
    if n % 2 == 0 or n % 3 == 0: return False
    i = 0

    # fermat primality test, complexity ~(log n)^4
    while i < size:
        if modexp(random.randint(1, n - 1), n - 1, n) != 1: return False
        i += 1

    # division primality test
    i = 5
    while i * i <= n:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    return True

def primegen(size):
    # do not modify!
    # generates a <size> digit prime
    if(size == 1): return random.choice([2, 3, 5, 7])
    lower = 10 ** (size - 1)
    upper = 10 ** size - 1
    p = random.randint(lower, upper)
    p -= (p % 6)
    p += 1
    if p < lower: p += 6
    elif p > upper: p -= 6
    q = p - 2
    while p < upper or q > lower:
        if p < upper:
            if checkprime(p, size): return p
            p += 4
        if q > lower:
            if checkprime(q, size): return q
            q -= 4
        if p < upper:
            if checkprime(p, size): return p
            p += 2
        if q > lower:
            if checkprime(q, size): return q
            q -= 2
        

def keygen(size):
    # generate a random public/private key pair
    # size is the digits in the rsa modulus, approximately. must be even, >2
    # return a tuple of tuples, [[n, e], [n, d]]
    # Complete this for HW 2 extra credit
    assert(size % 2 == 0 and size > 2) # keep this line!

    p = primegen(size/2)
    q = primegen(size/2)
    phi = calc_phi(p, q)
    n = calc_n(p, q)

    for e in range(3, phi):
        eg = egcd(e, phi)
        if eg[0] == 1:
            return [[n, e], [n, mulinv(e, phi)]]

def customkeytest(text, size):
    keypair = keygen(size)
    
    print("Public key:",keypair[0])
    print("Private key:",keypair[1])
    
    ciphertext = RSA_enc(text,keypair[0])
    plaintext  = RSA_dec(ciphertext,keypair[1])

    print("Original message:",text)
    print("Encrypted message:",ciphertext)
    print("Decrypted message:",plaintext)

# test()
customkeytest("hello world", 10)