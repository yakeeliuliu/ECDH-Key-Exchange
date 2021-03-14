# ECDH (Elliptic Curve Diffie Hellman) Key Exchange
With limited computing, caching, storage, energy and network bandwidth performance, lightweight controllers need comparable lightweight programs and protocol, especially for cryptography features with less key length and power consumption.

RSA, DSA and ECC are the most popular Public-key cryptography used.

DSA vs RSA: DSA and RSA use different mechanism to generate key pair, for purposes of cryptographic strength, they are considered to be equivalent while ECC promise to provide stronger security, increased performance, yet shorter key lengths.

ECC vs RSA: According to NIST recommendation, ECC can provide equivalent security strength with a significantly smaller key size. For example, to achieve the equivalent cryptographic strength of encrypting using a 112-bit symmetric key would require an RSA 2048 bit key, but only an ECC 224 bit key.

ECDH: ECC can be combined with DH for key exchange and encryption. Based on related research. Comparing to RSA, ECDH offers equivalent security with smaller key sizes, which results in lower power consumption, speedier calculations, and also lower memory and transmission capacity (bandwidth) reserve.

As above, ECDH is selected for this task. Key size which is equal to or above 128 can provide mathematic attacks protection till 2030 and beyond (NIST).

Simulation is implemented with Pure-Python ECDSA and ECDH library (tlsfuzzer).


How to run:
- run responder.py first, then run requestor.py.
- check if both have the same shared-key and verify each other's signature. 
