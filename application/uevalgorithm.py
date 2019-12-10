import random as r
import hashlib
from cryptable import *
from bookingApplication import *

def encrypt(ticketnummer,Achternaam):

    passangerDB= open('users.txt', 'r')
    inhoud = passangerDB.read()

    if Achternaam in inhoud :
        file= open('keylist.txt','a')
        file.write('\n'+str(r.randint(0,int(ticketnummer))))
        file.close()

    with open('keylist.txt', 'r') as f:
        lines = f.read().splitlines()

    value = ticketnummer + lines[-1]
    passDict=[]
    key= r.randint(0,9)
    def encryptor(key):
        for index in value:
            passDict.append(str(index) + str(key))
        print(passDict)
        for item in passDict:
            Value(item)
        valEncrypted = "".join(encryption)
        print(valEncrypted)
        with open('keylist.txt', 'r') as f:
            fist = f.read().splitlines()

    encryptor(key)

    print(value)
    print(valSize)

