# Lectures 04 and 05: Ciphers in Practice

## Introduction to Cryptography

Antiquity - 1970s

- ad-hoc design
- vulnerabilities/insecurity of
  - Caesar's cipher
  - shift cipher
  - mono-alphabetic substitution cipher

1980s - today

- rigorous study
- problem statement: secret communication over insecure channel
- abstract solution concept: symmetric encryption, Kerckhoff's principle, perfect secrecy
- concrete solution and analysis: OTP cipher, proof of security

### Formal Definitions of Security

Successful project management

- good design requires clear/specific security goals: avoids critical ommissions or over engineering

Provable security

- rigorous evaluation requires a security definition

### Precise Assumptions

Precise description of all relevant problem components

Adversary/attacker

- type of attacks: aka threat model
- *capabilities*: prior knowledge, access to information, party corruptions etc.
- *limitations*: bounded memory, passive vs active

Computational assumpitions (about hardnesss of certain tasks): e.g. factoring of large composite numbers is hard

Computing setting: what can be attacked and what not

Why are precise assumptions important?

- basis for security proofs (secure under specific assumptions)
- comparison among possible solutions
  - relations among different assumptions
    - stronger/weaker (i.e. less/more plausible to hold), "A implies B"
    - refutable vs non-refutable
- flexibility (in design and analysis)
  - validation: to gain confidence or refute
  - modularity: to choose among concrete schemes that satsify the same assumptions

Possible eavesdropping attacks:

- attacker posesses a collection of plaintext/ciphertext pairs: known as a plaintext attack
  - chosen plaintext attack (CPA): **advanced threat model**

### Provable Security

Security

- subject to certain assumptions, a scheme is proved to be secure according to a specific definition against a specific adversary
  - in practice the scheme may break if:
    - some assumptions do not hold or the attacker is more powerful

Insecurity

- a scheme is proved insecure with respect to a definition
  - it suffices to find a counterexample attack

Why is provable security important?

- typical performance
  - in some areas formal proofs may not be essential
  - in practice, typical/average case occurs
- worst case performance
  - in cryptography and secure protocol design formal proofs are essential
    - "experimental" security analysis is not possible
    - the notion of a "typical" adversary makes little sense and is unrealistic
  - in practice worst case attacks will occur
    - an adversary will use any means to break a scheme

## Computational Security

OPT is perfect but impractical: employs a very large key which can only be used once (unavoidable and make OTP not practical)

Our approach: relax "perfectness"

Initial model:

- perfect secrecy requires that
  - cipher text leaks **absolutely** no extra information about the plaintext
  - to adversaries of **unlimited** computational power

Refined model:

- a relaxed notion of security, called **computational security**, requires that
  - the cipher text releases **some** inofmraiton
  - to adversaries of **limited** computational power

Computational security

- to be contrasted against information-theoretic security
  - de facto way to model security in most settings
  - integral part of modern cryptography with rigorous mathematical proofs
- two relaxations
  - security is guaranteed against **efficient** adversaries
    - goal: make required resources larger than those available to any realistic attacker
  - security is guaranteed in a probabilistic manner
    - with some small probability, an attacker may break security
    - goal: make attack probability sufficiently small

### Rigorous Definition of Computational Security

**Concrete** approach: "A scheme is (t,e)-secure if any Attacker A running for time **at most** T succeeds in breaking the scheme with probability **at most** e

**Asymptotic** approach: classifies hardness of computational problems using polynomial-time reducibility

Examples:

- almost optimal security guarantees
  - if key length n, the number of possible keys is 2^n
  - attacker running for time t succeeds with probability at most ~t/(2^n) (brute-force attack)
- if n=60, security is enough for attackers running a desktop computer
  - 4 GHz (4x10^9 cycles/second), checking all 2^60 keys require about 9 years (if n=80, a super computer needs 2 years)
- current recommendation is n=128 at least
  - large difference between 2^80 and 2^128, e.g. #seconds since Big Bang is ~2^58
  - a once-in-100 years event corresponds to probability 2^-30 of happening at a particular sec
  - if within 1 year of computation attack is successful w/ probability 1/2^60, then it is more likely that Alice and Bob are hit by lightning

## Symmetic Encryption Security: Revisited

### Security Relaxation

Perfect security: M, Enc^k(M) are independent, unconditionally

**Computational security**: M, Enc^k(M) are independent, for all practical purposes. No extra information is leaked but a tiny amount (e.g. with prob 2^-128) to **computationally bounded attackers** (e.g., who cannot count to 2^128). Attacker's best strategy remains ineffective (random guess a secret key or exhaustive search over key space (brute force attack))

Plain security: protects against ciphertext-only attacks

Advanced security: protects against CPA. **Must be probabilistic**

### Computational EAV-security or indistinguishability

- relax definition of perfect secrecy based on indistinguishability
  - require target messages m0,m1 are chosen by a PPT attacker
  - require that no such attacker can distinguish Enc^k(m0) from Enc^k(m1): non-negligibly better than guessing

**Indistinguishability**: for every A (PPT), it holds that Pr(b'=b) = 1/2 + negligible (negligible factors can be ignored)

### Computational CPA-security

Strengthen definition of computational plain-security

- allows attacker to have access to an **encryption "box"**
- allow attacker to select m0,m1 **after** using this "box" (as many times as desired)

**Indistinguishability**: for every A (PPT), it holds that Pr(b'=b) = 1/2 + negligible

This method is **probabilistic encryption**: increases randomness (same message can be represented by multiple different cipher texts)

## OTP with Pseudorandomness

Randomness plays an integral role in encryption

- in a perfectly secure cipher, the ciphertext doesn't depend on the message
  - the ciphertext appears to be truly random
  - the uniform key-selection distribution is imposed also onto produced ciphertexts
    - e.g., c = k XOR m (for uniform k and any distribution over m)

When security is computational, randomness is **relaxed** to "pseudorandomness"

### Symetric Encryption as "OPT with pseudorandomness"

Stream cipher: uses a short key to encrypt long symbol streams into a pseudorandom ciphertext (weaker for pseudorandomness)

- based on abstract crypto primitive of pseudorandom generator (PRG)

Block cipher: uses a short key to encrypt blocks of symbols into pseudorandom cipher texts (stronger for pseudorandomness)

- based on abstract crypto primitive of pseudorandom function (PRF)

### Pseudorandom Generators (PRG)

Deterministic algorithm G that on input **seed** s that is an element of {0, 1}^^t, outputs G(s) element of {0, 1}^^(lt)

G is a PRG if:

- expansion
  - for polynomial I, it holds that for any n, l(n) > n
  - models the process of **extracting** randomness from a short random string
- pseudorandomness
  - no efficient statistical test can tell apart G(s) from a truly random string

PRG-based symmetric encryption

- **fixed-length** message encryption: plain-secure as long as the underlying PRG is secure

### Stream Ciphers: Modes of Operations

**Bounded or arbitrary-length** message encryption

- on the fly computation of new pseudorandom bits, no IV needed, plain-secure
- random IV used for every new message is sent along with ciphertext

## Formal Treatment in Modern Cryptography

formal definitions: what it means to be secure

prciese: which forms of attacks are/are not allowed

provable security: why a candidate solution is/is not secure

## Block Ciphers

### Realizing Ideal Block Ciphers in Practice

We want a random mapping of n-bit inputs to n-but outputs

- there are ~2^(n2^n) possible such mappings
- none of the above can be implemented in practice

Instead, we use a keyed function Fk : {0,1}^n -> {0,1}^n

- indexed by a t-bit key k
- there are only 2^t such keyed function
- a random key selects a "random-enough" mapping or a pseudorandom function

### Generic PRF-based Symmetric Encryption

**Fixed-length** message encryption

Encryption scheme is advanced-secure as long as the underlying PRF is secure

### Modes of Operations (I)

ECB: electronic code block

- insecure, of only historic value
- deterministic, thus not CPA-secure
- not EAV secure

Strengths and weaknesses of ECB

Strengths

- very simple
- allows for parallel encryptions
- very efficient (more so than CBC)

### Modes of Operations (II)

CBC: cipher block chaining

- CPA-secure if Fk a permutation
- uniform IV
  - otherwise no security breaks

Chained CBC

- use last block ciphertext of current message as IV of next message
- saves bandwith but not CPA-secure

### Modes of Operations (III)

OFB: output feedback

- uniform IV
- no need message length to be multiple of n
- resembles synchronized stream-cipher mode
- CPA-secure if Fk is PRF
- required no preprocessing which it makes it more efficient
- close to OTP cipher as the IV can be treated as a key when put through the function
  - m would be the message to encrypt
  - goes through an additional step

### Mode of Operations (IV)

CTR: counter mode (best)

- uniform ctr
- no need message length to be multiple of n
- resembles synchronized stream-cipher mode
- CPA-secure if Fk is PRF
- no need for Fk to be invertible
- parallelizable
- very secury as it creates more obscurity (changing counter for every part of the message)

## Symmetric Encryption

Techniques used in symmetric encryption

- substitution: exchanging one set of bits for another
  - substitution boxes:
    - substitution can also be done on binary numbers
    - such substitutions are usually described by substitution boxes, or S-boxes
- transportation: rearranging the order of the ciphertext bits to break any regularities in the underlying plaintext
- confusion: enforce complex functional relationship between the plaintext/key pair and cipher text
  - e.g. flipping plaintext or key bit causes unpredictable changes to new ciphertext
- diffusion: distributes information from single plaintext characters over entire ciphertext output
