# Lecture 02 : Symmetric-key Encryption

## Value

Computer systems comprise assets that have value

- computers store personal or important data (files, photos, emails etc.)
- personal, time-dependent, and often imprecise values (monetary vs. emotional)

Valuable assets deserve security protection

- to preserve their value -> exprpessed as a security property (ex: personal photos should always be accessible by their owner)
- to prevent harm -> examined as a concrete attack (deletion)

## Players of Security Game

Defenders

- system owners (users, admins etc.)
- seek to enforce one or more security properties or defeat certain attacks

Attackers

- external entities (hackers, other users etc.)
- seek to launch attacks that break a security property or impose the system to certain threats

## Security Properties

General statements about the value of a computer system
Examples

- CIA Triad: seeks to prevent unauthorized viewing or modification while preserving access
  - confidentiality: attacks are not possible
    - an asset is viewed only by authorized parties
    - tools: obfuscation, encryption
  - integrity: data is not maliciously manipulated
    - consistency: data is up-to-date for the most recent valid/approved copy
    - tools: hashing, MACs
  - availability: system is able to be accessed and used
    - usable: meets service's needs, bounded waiting/completion time, acceptable outcome
    - timely response, fairness, concurrency, fault tolerance
    - tools: redundancy, fault tolerance, distributed architectures

## Symmetric-key Encryption

Eavesdropping: main threat against confidentiality of in-transit data

Problem setting: secret communication

- two parties wish to communicate over a channel
  - Alice (source) wants to send a message to Bob (destination)
- underlying channel is unprotected
  - Eve (attacker) can eavesdrop any sent messagge
  - packet sniffing over networked or wireless communications

Solution concept: Symmetric-key encryption

Plantext -Encryption (key)-> Ciphertext -Decryption (key)-> Original Plantext

- main idea
  - secretly transform message so that it is unintelligible while in transit
  - message is sent in ciphertext instead of plaintext
  - destination decrypts message
  - attacker can intercept the encrypted message but cant decipher it
  - source and destination share a secret ket that is used to decipher the message (symmetric key)
  - **assume that there is a way for the key to be shared and remain secret**

Abstract crptographic primitive (aka cipher) is defined by a message space and a triplet of algorithms (Gen, Enc, Dec)

- Gen and Enc are probabilistic algorithms, whereas Dec is deterministic
  - probabilistic: different executions on the same input may result in different execution sequences and possibly different outputs (ex: the execution of quicksort)
    - internally makes use of some randomness
      - probabilistic can be the output of a deterministic algorithm plus inputs of randomized values (0s and 1s)
      - probabilistic can be either purely deterministic (more specific) or purely probabilistic (more general) -> probabilstic is a super class of all deterministic
        - ex: encryption is probabilistic but can be deterministic if it makes use of no additional random inputs
          - encryption is much stronger when it is probabilistic
  - deterministic: the same output is produced for the same input every time the algorithm is run
    - execution depends only on the input
- Gen outputs a uniformly random key k (from some key space K)

Desired properties for symmetric-key encryption scheme (should satisfy the following)

- efficiency: key generation & message transformations "are fast"
- correctness: for all m and k, it holds that Dec(Enc(m, k), k) = m
- security: one "cannot learn" plaintext m from ciphertext c

## Kerckhoff's Principle

Kerckhoff's Principle: *"The cipher method must not be required to be secret, and it must be able to fall into the hands of the enemy without inconvenience."*
Reasoning

- due to security and correctness, Alice & Bob must share some secret info
- if no shared key captures this secret info, it must be captured by Enc, Dec
- keeping Enc, Dec secret is problematic
  - **don't share info about the algorithm**
  - harder to keep secret an algorithm than a short key (e.g., after user revocation)
  - harder to change an algorithm than a short key (e.g., after secret info is exposed)
  - riskier to rely on custom/ad-hoc schemes than publicly scrutinized/standardized ones

Asymmetric-key encrpytion:
Plantext --Encryption (encryption key)--> Ciphertext --Decryption (decryption key)--> Original Plantext

## Main Application Areas

Secure communication

- encrypt messages
- assumption
  - Alice and Bob securely generate, distribute and store shared key k
  - attacker does not learn key k

Secure storage

- encrypt files outsourced to the cloud
- assumption
  - Alice securely generates and stores key k
  - attacker does not learn key k

## Brute-force Attack

Generic attack

- given a captured ciphertext c and known key space K, Dec
- strategy is an exhaustive search
  - for all possible keys k in K
    - determine if Dec (c, k) is a likely plaintext m
  - requires some knowledge on the messaging space M
    - i.e., a structure of the plaintext (e.g., PDF file or email message)

Countermeasure

- key should be a random value from a sufficiently large key space K to make exhaustive search attacks infeasible
- i.e., key space is large enough that brute forcing takes too long

## Classical Ciphers

Substitution ciphers: large class of ciphers

- each letter is uniquely replaced by another
- there are 26! possible substitution ciphers
  - e.g., one popular substitution "cipher" for some Internet posts is ROT13

Examples

- Caesar's cipher
  - shift each character in the message by 3 positions
    - or by 13 positions in ROT-13
  - crryptanalysis
    - no secret key is used - based on "security by obscurity"
    - thus the code is trivially insecure once knows Enc (or Dec)
- Shift cipher
  - keyed extension of Caesar's cipher
  - randomly set key k between 0:25
    - shift each character in the message by k positions
  - cryptanalysis
    - brute-force attacks are effective given that
      - key space is small (26 possibilities or, actually, 25 as 0 should be avoided)
      - message space M is restricted to "valid words"
        - e.g., corresponding to valid English text
