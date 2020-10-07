# Lecture 06: MACs and Hashing

## Message Authentication

Fundamental security property: an asset is modified only by authorized parties

**Alteration**: main threat against integrity of a system

Security problems in modern cryptography

- classical cryptography: message encryption
- modern cryptography: wide variery of security problems
- sibling of message encryption: message authentication

### Message Authentication: Motivation

Information has a value, but only when it is correct

- random, incorrect, inaccurate or maliciously altered data is useless or harmful
  - message authentication = message integrity + authenticity
    - while in transit (or at rest), no message should be modified by an outsider
    - no outsider can impersonate the stated message sender or owner

- its often necessary / worth to protect critical and valuable data
  - message encryption: while in transit no message should be leaked to an outsider

### Integrity of Communications/Computations

Highly important

- any unprotected system cannot be assumed to be trustworthy w.r.t 
  - origin/source of information (due to impersonation attacks, phishing etc.)
  - contents of information (due to main-in-the-middle attacks, email spam, etc.)
  - overall system functionality

Prevention vs. Detection

- unless a system is "closed", adversarial tampering with its integrity cannot be avoided 
- goal: identify system components that are not trustworthy
  - detect tampering or prevent undetected tampering
    - e.g., avoid "consuming" falsified information

Encryption does not imply authentication, a common misconception: "since ciphertext c hides message m, Mallory cannot meaningfully modfiy m via c"

This is incorrect because:

- all encryption schemes (seen so far) are based on OTP, i.e., masking via XOR
- consider flipping a single bit of ciphertext c; what happens to plaintext m?
  - ensure that the plaintext contents are tampered through flipping. You don't know necessarily how important this flipping is but it is a big attack

## Message Authentication Codes (MACs)

**Problem setting**: reliable communication. Two parties wish to communicate over a channel and the underlying channel is unprotected. The attacker can now manipulate any sent messages (e.g. message transmission via a compromised router)

**Solution concept**: Symmetric-key message authentication

Main idea:

- secretly annotate or "sign" message so that it is unforgeable while in transit
  - Alice **tags** her message m with **tag t** which is sent along with **plaintext m**
  - Bob **verifies** authenticity of received message using tag t
  - Attacker can manipulate m, t but "**cannot forge** a key
  - Modified messages are detected and disregarded

### Security tool: Symmetric Message Authentication code

Abstract cryptographic primitive, a.k.a. MAC, defined by

- a *message space M**, and
- a triplet of algorithms **(Gen, Mac, Vrf)**

Desired MAC properties

- efficiency: key generation and message transformations "are fast"
- correctness: for all m and k, it holds that Vrf^k(m, Mac^k(m)) == ACCEPT
- security: one "cannot forge" a fake verifiable pair m',t'

Main application areas:

- secure comminication
  - verify authenticity of messages
  - assumption
    - Alice and Bob securely generate, distribute and store shared key k
    - attacker does not learn key k
- secure storage
  - verify authenticity of files
  - assumption
    - Alice securely generates and stores key k
    - attacker does not learn k

### Conventions

Random key selection: Gen selects key k **uniformly at random** from the key space K

**Canonical verification:**

- when Mac is deterministic, Vrf typically amounts to re-computing the tag t
  - Vrf^k(m, t):

    1. t' := Mack(m)
    2. if t = t', output ACCEPT else output REJECT

## Replay Attacks

Real-life attacker: in practice, an attacker may:

- observe traffic of authenticated and verified messages
- manipulate (or often also partially influences) traffic
  - aims at inserting an invalid but verifiable message m*, t* into the traffic
    - interesting case: forged message is a new (unseen) one
    - trivial case: forged message is a previously observed one, aka a **replay attack**
- launch a **brute-force attack** (given that Mac^k(m) -> t is publicly known)
  - given any observed pair m, t, exhaustively search key space to find the used key k

Threat model: adversary A who is:

- "active" (on the wirde): A can observe and manipulate sent messages)
- "well-informed": A can request MAC tags of messages of its choice

Are replay attacks important? Yes: very realistic and serious threat: e.g., what if a money transfer order is "replayed"?

## MAC Constructions

1. Fixed-length MAC

    - based on use of a pRF
      - employ a PRF F^k in the obvious way to compute and canonically verify tags
      - set tag t to be the pseudorandom string derived by evaluating F^k on message m
    - secure provided that F^k is a secure PRF

2. Domain extension for MACs 

    - suppose we have the previous fix-length MAC scheme
    - how can we authenticate a message m of arbitrary length?
    - naive approach:
      - pad m and view it as d blocks m1, m2, ..., md
      - separately apply MAC to block mi
    - assumes a secure MAC scheme for messages of size n
    - set a tag of message m of size beta at most 2^(n/4) as follows
      - choose fresh random nonce r of size n/4, view m as d blocks of size n/4 each
      - separately apply MAC on each block, authenticating also its index, beta and nonce r

3. CBC-MAC

    - idea
      - employ a PRF in a manner similar to CBC-mode encryption
    - security
      - exension is secure if 
        - F^k is a secure PRF
        - only **fixed-langth** messages are authenticated
      - messages of length equal to any multiple of n can be authenticated
        - but this length needs to be fixxed in advance

### CBC-MAC vs Previous Schemes

- crucially for their security
  - CBC-MAC uses no IV (or uses an IV set to 0) and only the last PRF output
  - CBC-mode encryption uses a random IV and all PRF outputs
  - simple modifications can be catastrophic

## Hash Functions

Basic cryptographic primitive

- maps **objects** to  fixed-length binary strings
- core security property: mapping avoids collisions
  - collision: distinct objects (x != y) are mapped to the same hash value (H(x) = H(y))
  - although collisions necessarily exist, they are infeasible to find

Hash and compression functions

- **general** has function H() maps a message of **arbitrary length** to a **l(n)-bit** string

- **compression** (hash) function h() maps
  - a **long** binary string to a **shorter** binary string

Domain extension via the **Merkle-Damgard transform**: general design pattern for cryptographic has functions 

- H(x) is computed by applying h() in a "chained" manner over n-bit message blocks
  - reduces CR of general hash functions to CR of compression functions
  - thus it suffices to realize a collision-resistance

Well-known hash function:

- SHA2: can output 224, 256, 384, and 512 bits respectively
- based on Merkle-Damgard + Davies-Meyer

Secure MAC for messages of arbitrary lengths

- new MAC (Gen', Mac', Vrf') as the name suggests
  - Gen': insantiate H and Mac^k with key k
  - Mac': hash message m into h = H(m), output Mac^k-tag t on h
  - Vrf': canonical verification
