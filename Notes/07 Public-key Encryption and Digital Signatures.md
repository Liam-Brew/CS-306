# Lecture 07: Public-key Encryption and Digital Signatures

## Principles of Modern Cryptography

1. security definitions
2. precise assumptions
3. formal proofs

For symmetric-key encryption/authentication:

- adversary
  - types of attacks
- trusted set-up
  - secret key is distributed securely
  - secret key remains secret
- trust basis
  - underlying primitives are secure
  - PRG, PRF, hashing, ...
    - e.g., block ciphers, AES, SHA-2 etc.

"Secret key is distributed securely": 2 individuals must **securely obtain** a **shared secret key**

- securely obtain: need of a secure channel (**strong assumption**)
- shared secret key: too many keys (**challenging problem**)

## Public-key (or asymmetric) cryptography

Goal: device a cryptosystem where key setup is "more" manageable

Main idea: user-specific keys (that come in pairs)

- user U generates two keys (Upk, Usk)
  - Upk is public: can safely be known by everyone
  - Usk is private: must remain secret

Usage:

- employ public key Upk for certain "public" tasks
- employ private key Usk for certain "sensitive" tasks

Assumption:

**public-key infrastructure (PKI)**: public keys become **securely** available to users

From symmetric to asymmetric encryption:

- secret-key encryption
  - main limitation: **session-specific** keys
- public-key encryption
  - main flexibility: **user-specific** keys

From symmetric to asymmetric authentication:

- secret-key encryption (MAC)
  - main limitation: **session-specific** keys
- public-key encryption (or digital signatures)
  - main flexibility: **user-specific** keys

  (only messages signed by sender's SK can be verified by sender's PK)

For asymmetric-key encryption/authentication:

- adversary
  - types of attacks
- trusted set-up
  - PKI is needed
  - secret key remains secret
- trust basis
  - underlying primitives are secure
  - typically, algebraic computationally-hard problems
    - e.g., discrete logic, factoring etc.

General comparison

- symmetric crypto
  - key management
    - less scalable and riskier
  - assumptions
    - secret & authentic communication
    - secures storage
  - primitives
    - generic assumptions
    - more efficient in practice
- asymmetric crypto
  - key management
    - more scalable and simpler
  - assumptions
    - authenticity (PKI)
    - secure storage
  - primitives
    - math assumptions
    - less efficient (2-3x orders of magnitude more costly than symmetric)

### Public-key Infrastructure (PKI)

Mechanism for securely managing, in a dynamic multi-user setting, user-specific public-key pairs

- dynamic, multi-user
  - system is open to anyone; user can join & leave
- user-specific public-key pairs
  - each user U in the system is assigned a unique key pair (Upk, Usk)
- secure management (authenticated public keys)
  - public keys are authenticated: current Upk of user U is publicly known to everyone

Very challenging to realize: currently using **digital certificates** but more efficient research is ongoing

## Public Key Signature

Distribution of public keys:

- public announcement: broadcast public keys to recipients/community
- publicly available directory: greater security by registering keys with a public directory

### Certificates

A public key and an identity bound together in a document signed by a certificate authority

**Certificate authority (CA)**: authority users trust to securely bind identity to public keys

- CA verifies identities before generating certificates for these identities
- secure binding via digital signatures
  - ASSUMPTION: the authority's PK CApk is authentic

Certificate hierarchy: single CA certifying every public key is impracticaly; instead use root certificate authorities:

- root CA signs certificates for intermediate CAs, they sign certificates for lower-level CAs etc.

## Secure Channel

Secret-key cryptography is "reduced" to public-key. PK encryption can be used on-the-fly to securely distribute session keys. Main idea is to leverage PK encryption to securely distribute session keys

- sender generates a fresh session-specific key k and learns reciever's public key Rpk
- session key k is sent to receiver encrypted under ker Rpk
- session key k is employed to run symmetric-key crypto

Hybrid encryption reduces secret-key crypto to public-key crypto

Main idea:

- encapsulate secret key k into c
- user k for secret-key encryption of m
- KEM: key-encapsulation mechanism
