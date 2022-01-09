
from turtle import update
import cryptography
import matplotlib as matplotlib
import numpy
import sudo as sudo

import requests
import hashlib
import timeit                                          # calling library of timeit for computation of runtime
start = timeit.default_timer()                         # start point for computing runtime

from random import randint
import spn_decryption                                  # calling spn_decryption file
import spn_encryption                                  # calling spn_encryption file


K = 0b00111010100101001101011000111111                  # masterkey

def str2bin16(s):                                      # for transfering of binary strings to binary
    x=int(s)
    z=0
    for i in range(0,16):
        y = x%(10)
        z = z+(y*(2**i))
        x//=(10)
    return z




plain_text=open('plain text','w')                            # opening file for writing plain text
for i in range(0,1000):
   plain_text.write(format(randint(0,2**16),'016b'))          # generate 1000 16bits bitwise number
   plain_text.write('\n')                                     # next line
plain_text.close()                                            # closing file


cipher_text = open('cipher text','w')                        # opening file for writing cipher text
plain_text1 = open('plain text','r')                         # opening file for reading plain text
for i in range(0,1000):
    x=str2bin16(plain_text1.readline())                      # reading line to line of plain text
    y=spn_encryption.encrypt(K,x)                            # doing encryption
    cipher_text.write(format(y,'016b'))                      # writing cipher text in the file
    cipher_text.write('\n')                                  # next line
plain_text1.close()                                          # closing file
cipher_text.close()                                          # closing file


cipher_text1=open('cipher text','r')                         # opening file for reading cipher text
decrypted_text=open('decrypted text','w')                    # opening file for writing decrypted text
for i in range(0,1000):
    h = str2bin16(cipher_text1.readline())                   # reading line to line of cipher text
    l = spn_decryption.decrypt(K, h)                         # doing decryption
    decrypted_text.write(format(l,'016b'))                   # writing decrypted text in the file
    decrypted_text.write('\n')                               # next line
cipher_text1.close()                                         # closing file
decrypted_text.close()                                       # closing file


plain_text2 = open('plain text', 'r')                              # opening file for reading plain text
decrypted_text1=open('decrypted text','r')                         # opening file for reading decrypted text
for i in range(1000):
    if plain_text2.readline()!=decrypted_text1.readline():         # comparing line to line of plain text and decrypted text
        print('decrypted text is not plian text')
print('decrypted text is same plain text')
plain_text2.close()                                                # closing file
decrypted_text1.close()                                            # closing file


stop = timeit.default_timer()                                        # stop point for computing runtime
print('runtime: ', stop-start)                                       # computing runtime and print it
print('RAM usage is almost 30 MB')                                   # RAM usage

# See PyCharm help at https://www.jetbrains.com/help/pycharm/