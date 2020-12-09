# Lecture 08: Crypto Light

## Authentication

### Authenticated Encryption (AE)

Crypto primitive that realizes an "ideally secure" communication channel

- motivation
  - important in practice as real apps often need both
  - good security hygiene
    - even if a given app asks only/more for secrecy or integrity than the other, its always better to achieve both

Constructions of a secure authenticated encryption scheme Pi(AE) all make use of:

- CPA-secure encryption scheme Pi(E) = (Enc, Dec)
- secure MAC Pi(M) = (Mac, Vrf)
- instantiated using independent secret keys key, km
- the **order** in which these are used matters

Generic AE constructions (1)

1. encrypt-and-authenticate

    - Enc^ke(m) -> c; Mac^km(m) -> t; send ciphertext (c,t)
    - Dec^ke(c) = m != faill and Vrf^km(m,t) accepts, output m; else output fail
    - generally insecure
      - MAC tag t may leak information about m

2. authenticate-then-encrypt

    - Mac^km(m) -> t; Enc^ke(m||t) -> c; send ciphertext c
    - if Dec^ke(c) = m || t != fail and Vrf^km(m,t) accepts, output m; else output fail
    - generally insecure
      - used in TLS

3. encrypt-then-authenticate (cf. "authenticated encryption")

    - Enc^ke(m) -> c, Mac^km(c) -> t; send ciphertext (c,t)
    - if Vrf^km(c,t) accepts then output Dec^ke(c) = m, else output fail
    - generally secure (as long as Pi(M) is a "strong" MAC)
      - used in TLS, SSHv2, IPsec

An AE scheme Pi(AE) = (enc, Dec) enables two parties to communicate securely

- session: period of time during which sender and receiver maintain state
- idea: send any message m as c = Enc^k(m) & ignore received c that don't verify
- security: secrecy & integrity are protected
- remaining possible attacks:
  - re-ordering attack
  - reflection attack
  - replay attack

## Applications of Cryptographic Hashing

Crypto hash functions (basic crypto primitive):

- maps objects to a fixed-length binary strings
- for all practical purposes, mapping avoids collisions (distinct objects x != y mapped to same value H(x) = H(y))
  - collision resistance: no distinct inputs can be efficiently found that collide in the hash domain
    - "any object can be securely mapped to a practically-unique short digest"
- collision resistance implies two weaker security properties
  - finding a collusion w.r.t. a given raandom object x is also infeasible
  
### Hashing in Security

1. Digital Envelops

    - two operations
      - commit(x, r) = C
        - i.e., put message x into an evelop (using randomness r)
        - e.g., commit(x, r) = h (x || r)
        - hiding property: you cannot see through an envelop
      - open(C, m, r) = ACCEPT or REJECT
        - i.e., open envelop (using r) to check that it has not been tampered with
        - e.g., open(C, m, r): check if h(x || r) = ?C
        - binding property: you cannot change the contents ofa sealed envelop

2. Honeywords

    - based on decoy passwords, aka honeywords
      - red stores user i's real password P^i and k-1 fake ones in unlabeled set C^i
      - blue server stores the index d^i of P^i in set C^i
      - password verification through sequential verifications
