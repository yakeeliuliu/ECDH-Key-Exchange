# ECDH (Elliptic Curve Diffie Hellman) Key Exchange
With limited computing, caching, storage, energy and network bandwith performance, lightweight controllers need compareable lightweight programs and protcol, especially for cyptography features with less key length and power comsuption.
 
RSA, DSA and ECC are the most popular Public-key cryptography used for. DSA and RSA sue different mechanism to generate key pair, for purposes of cryptographic strength, tehy are considered to be equivalent while ECC promise to provide stronger security, increased performance, yet shorter key lengths. 

Key Size Comparison ( NIST ):

----------------------------------------------------------------------------
| Symmetric Key Size (bits) |	RSA Size (bits) |	Elliptic Curve Key Size (bits)
----------------------------------------------------------------------------
  80	                         1024	             160
  112	                        2048	             224
  128	                        3072	             256
  192	                        7680	             384
  256	                        15360	            521
----------------------------------------------------------------------------

ECC can be combined with DH for key exchange and encryption. Based on related research, Compareing to RSA, ECDH offers equivalent security withsmaller key sizes, which results in lower power consumption,speedier calculations, and also lower memory and transmissioncapacity (bandwidth) reserve.
As above, ECDH is choosed for this task. Key size which is equal to or above 128 can provid mathematic attacks protection till 2030 and beyond (NIST).

Simulation is implemented with Pure-Python ECDSA and ECDH library (tlsfuzzer).

How to run:

run responder.py first, then run requestor.py.
check if both have the same shared-key and verify each other's signature. 
