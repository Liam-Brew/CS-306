# Lecture 09: Topics

## Certificate Transparency

Dealing with rogue certs or compromised CAs: **impossible** to prevent impersonation, but can we **detect** it after it happens?

Why should we?

- punish bad CAs
- victims learn they were impersonated
- deters attacks

Certificate Transparency (CT) to the rescue: extra system so that issued certificates are more transparent

Once a cert is in CT:

1. it cannot be deleted
2. it can be efficiently discovered

Non-equivocation: everyone sees the same log

Consequence: fake PK for VISA is discovered by VISA in the log (slide example)

## Buffer Overflow

Memory Basics

- stack
  - used whenever a function call is made
  - typically higher addresses growing downwards
- static data area
  - global variables used by programs (not initialized with zero)
  - e.g., char s[] = "hello world"
- heap
  - begins after data area, growing upwards
  - dynamically managed by malloc, realloc, free

Buffer overflows are based on a programmer's oversights (or programming language vulnerabilities)

- exploited by attackers by inputting more data than expected
  - attacker's data that is written beyond the space allocated for it
  - e.g., a 10th byte in a 9-byte array
- typical exploitable buffer overflow
  - users' inputs are expected to go into regions of memory allocated for data
  - attacker's inputs are allowed to overwrite memory holding executable code
- attacker's challenge is to discover buffer-overflow vulnerabilities

Harm for buffer overflows

- overwrite
  - an instruction or data item of some program's data
    - e.g., PC and data in the stack so that PC points to the stack
  - data or code belonging to another program or the OS
    - e.g., part of the code in low memory, substituting new instructions
    - gives to attacker that program's underyling information

### Attack Structure

To exploit a buffer overflow vulnerability the attacker must address some challenges

1. write malicious code that does harm

    - nontrivial task
    - special type of code called shellcode
    - solutions:
      - to invoke system call execve(), need to know the address of the string "/bin/sh" (storing and deriving this address is not easy)
        - **push string "/bin/sh" onto stack and use the stack pointer esp to get its location
      - function strcpy() will stop in the first occurrence of a NULL value
        - convert instructions containing 0 into equivalent instructions not containing 0

2. inject malicious code into the memory of the target program (TP)

    - control the contents of the buffer in TP
    - e.g., in following example, by storing malicious code in the input file
    - ex: functions such as strpy(buffer, str) that do not check length

3. jump to and execute the malicious code

    - control the execution of TP and execute injected malicious code
    - e.g., hijack the system
    - need to know absolute address of the malicious code
      - overflow buffer so that this address overwrites the return address
      - when the funciton returns the malicious code will run
    - strategies to find where the malicious code starts
      - make a copy of the TP and find (approximate) the start of malicious code by debugging
      - set-UID TP: allows to run an executable with the privileges of the executable's owner
    - if TP runs remotely you can always guess
      - stack usually starts at the same address and is not very deep
      - range of addresses to guess is actually quite small
    - to improve chance of success
      - add many NOP operations to the beginning of the malicious code
      - NOP (no operation) is a special instruction
        - does nothing other than advancing to the next instruction
        - therefore as long as the guessed address points to one of the NOPs, the attack will be successful
        - with NOPs the chance of guessing the correct entry point to the malicious code is significantly improved
