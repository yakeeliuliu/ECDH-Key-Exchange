import socket
from ecdsa import SigningKey, VerifyingKey, NIST192p, ECDH

#############################################################
#####               CHOOSE CURVE AND PRIMES       ###########
#############################################################
# curve = NIST192p
primes_curve_192 = {
    "p": 6277101735386680763835789423207666416083908700390324961279,
    "n": 6277101735386680763835789423176059013767194773182842284081,
    "b": "64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1",
    "Gx": "188da80e b03090f6 7cbf20eb43a18800f4ff0afd82ff1012",
    "Gy": "07192b95 ffc8da78631011ed6b24cdd573f977a11e794811"
}
#############################################################
#####    GENERATE LOCAL KEY PAIRS AND SIGNATURE       #######
#############################################################
ecdh_local = ECDH(curve=NIST192p)
# need to generate signing key first using ecdsa.keys.SigningKey class
# private and public key key will be extracted from signing key
# Verifying key == Local private key
sk = SigningKey.generate(curve=NIST192p)
sk_string = sk.to_string()
# extract private key from signing key
ecdh_local.load_private_key(sk)
# extract public key ( equals to verifying key )
local_public_key = ecdh_local.get_public_key()
vk = sk.verifying_key
local_public_key_string = local_public_key.to_string()
# DH is vulnerable to MITM attack
# Prior to execution of the protocol, each side need to sign their public key
signature = sk.sign(local_public_key_string)


##############################################################
#####      listen on remote machine for key suite         ####
##############################################################

local_port = 5000
local_host = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((local_host, local_port))
print("--- Listening on port {0}".format(local_port))
(received_curve, addr1) = sock.recvfrom(1024)
(received_key, addr2) = sock.recvfrom(1024)
(received_siganture, addr3) = sock.recvfrom(1024)
# print(curve,received_key,signature)

if received_curve.decode('utf-8') == 'curve=NIST192p':
    ##############################################################
    #######    send curve and signature to remote ip      ########
    ##############################################################

    print("---- Remote primes, public key and signature have been received, now send local suite:")
    remote_ip = input("Remote ip: ")
    remote_port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(received_curve, ((remote_ip, remote_port)))
    sock.sendto(local_public_key_string, (remote_ip, remote_port))
    sock.sendto(signature, (remote_ip, remote_port))

    ##############################################################
    #####                calculate master-key             ########
    ##############################################################

    print("----------calculating shared key...")
    ecdh_local.load_received_public_key_bytes(received_key)
    master_key = ecdh_local.generate_sharedsecret_bytes()
    print("Shared key value is: ", end=" ")
    print(master_key)

    ##############################################################
    #####    verify received signature and public key     ########
    ##############################################################

    remote_public_key = VerifyingKey.from_string(received_key)
    assert remote_public_key.verify(received_siganture, remote_public_key.to_string())
    print("Congrats! signature has been verified ")
