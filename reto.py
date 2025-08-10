#!/usr/bin/env python3
from Crypto.Util.number import *
import gmpy2, binascii
from myrsa import myreal_p, myreal_q
from oximoron import flag

n = myreal_p * myreal_q
e = 65537
ciphertext = binascii.hexlify(long_to_bytes(pow(bytes_to_long(flag), e, n)))
file = open('secret.enc', 'w')
file.write("secret: {}\nN: {}\nE: {} ".format(ciphertext, str(n), str(e)))
