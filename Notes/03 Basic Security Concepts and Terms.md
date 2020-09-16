# Lecture 03: Basic Security Concepts and Terms

## Perfect Secrecy (Information-Theoretic Security)

***Everything besides the encryption algorithm is assumed to be known by everyone***

For any k in set K, m in set M, and any ciphertext c output of Enc(m), it holds that Pr(Dec^(c) = m) = 1. This means that the probability of decrypting message m using key k is 1. This is called perfect because no "slack" is allowed and there is always a certainty of successful execution

Towards defining perfect security

- defining security for an encryption scheme is not trivial
  - e.g., what do we mean by 'Eve "cannot learn" m (from c)?
- our setting so far is a random experiment
  - a message m is chosen according to Dm
  - a key key is chosen according to Dk
  - Enc^k(m) -> c is given to the adversary

**Attempt 1: Protect the Key**: security means that the adversary should not be able to compute the key k

- intuition -> necessary condition
  - it'd better be the case that the key is protected
- problem -> but not suffient condition
  - this definition fails to exclude clearly insecure schemes
  - e.g., the key is never used, such as when Enc^k(m) := m

**Attempt 2: Don't Learn M**: security means that the adversary should not be able to compute the message m or any useful data about m

- intuition
  - it'd be better be the case that the message m is not learned
- problem
  - this definition fails to exclude clearly undesirable schemes
  - e.g., those that protect m partially, i.e., they revel significant information about it

**Attempt 3: Learn Nothing**: the adversary should not be able to learn any information about m relating to the actual sending and recieving of m. Background information is still fair game

- intuition
  - it seems close to what we should aim for perfect secrecy
- problem
  - the definition ignors the adversary's prior knowledge on M
  - e.g., the distribution D^m may be known or estimated
    - m is a message to be sent

**Attempt 4: Learn Nothing More**: the adversary should not be able to learn any additional inormation on m. This is different from Attempt 3 in that nothing like background information or probability can be learned on m

- intuition
  - it seems close to what we should aim for perfect secrecy
- problem
  - the definition ignors the adversary's prior knowledge on M
  - e.g., the distribution D^m may be known or estimated
    - m is a message to be sent

### Two Equivalent Views of Perfect Security

Random experiment

- D^M -> m = M
- D^K -> k = K
- Enc^k(m) -> c = C

Expressed mathematically:

- a posteriori = a priori (what the attacker knew before is equal to what they kew after)
  - for every D^M, m is an element of set M and c is an element of set C, for which Pr(C = c) > 0, it holds that Pr(M = m | C = c) = Pr(M = m)
    - this assumes that one of the variables was learned by the attacker. Nevertheless, the power of the attacker to predict what is transfered has remained the same
    - basically that if one aspect is compromised than the attacker still doesn't know what the message is

C is independent of M

- for every m, m' is an element of M and c is an element of C, it holds that Pr(Enc^k(m) = c) = Pr(Enc^k(m') = c)

## The One-Time Pad

A type of substitution cipher that is "absolutely unbreakable". Unlike regular subsitution cipher, statistics are not preserved

- invented in 1917
- substitution cipher
  - individually replace plaintext characters with shifted ciphertext characters
  - independently shift each message character in a random manner
    - to encrypt a plaintext of length n, use n uniformly random keys k^1, ..., k^n
- "absolutely unbreakable"
  - perfectly secure when used correctly
  - based on message-symbol

### The OTP Cipher

Fix n to be any positive integer

Set M = C = K = {0, 1}^^n

- Gen: choose n bits uniformly at random (each bit independently with probability .5)
  - Gen -> {0,1}^^n
- Enc: given a key and a message of equal lengths, compute the bit-wise XOR
  - Enc(k, m) = Enc^k(m) -> k XOR m (i.e., mask the message with the key)
- Dec: compute the bit-wise XOR of the key and the ciphertext
  - Dec(k, c) = Dec^k(c) := k XOR c
- Correctness
  - k XOR c = k XOR k XOR m = 0 XOR m = m

According to the definition of Perfect Security, OTP is perfectly secure. For all n-bit long messages m1 and m2 and ciphertexts c, it holds that Pr(E^K(m1) = c) = Pr(E^k(m2)) = c), where probabilities are measured over the possible keys chosen by Gen.

Proof:

- events "Enc^k(m1) = c", "m1 XOR K = c", and "K = m1 XOR c" are equal-probable
- K is chosen at random, irrespectively of m1 and m2, with a probability 2^^(-n)
- thus, the ciphertext does not reveal anything about the plaintext

OTP characteristics

- A "substitution" cipher
  - encrypt an n-symbol m using n uniformly random "shift keys" k^1, k^2, ... k^n
- 2 equivalent views
  - K = M = C
    - {0,1}^^n
    - bit-wise XOR (m XOR k)
  - "shift" method
    - G,(G,+) is a group
    - addition/subtraction (m +/- k)
- perfect secrecy
  - since each shift is random, every ciphertext is equally likely for any plaintext
- limitations (on efficiency)
  - "shift keys"
    - **as long as messages**
    - ***can only be used once***

## Wireshark

Packet sniffer: used to view/analyze packets

**Transmission Control Protocol (TCP)**: controls/directs communication between two computers. Used to establish coordinate different machines to ensure that they are on the same communcation level. Two-way

**User Datagram Protocol (UDP)**: lower-level and lower-latency version of TCP. Sends messages without awaiting confirmation of communication agreement by recieving party

**Port**: communication endpoint and logical structure within the operating system

### Filtering

- filtering by port is important (etc. filter by tcp.port == 23)
  - this shows only communications on the Telnet-reserved port (Telnet is the example used for Star Wars)
- first 3 packets of a communication form the three-way handshake

  1. source attempts to synchronize with the source (port format in 'Info': request_sorce -> request_destination)
  2. destination acknowledges synchronization
  3. source acknowledges acknowledgement
  
HTTP communication that is not encrypted can be viewed in Wireshark packets
