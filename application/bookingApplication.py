from uevalgorithm import *
from cryptable import *
from bookingApplication import *
import random as r

def encrypt(ticketnummer,Achternaam):

    passangerDB= open('users.txt', 'r')
    inhoud = passangerDB.read()
    passangerDB.close()
    if ticketnummer not in inhoud :
        file= open('keylist.txt','a')
        file.write('\n'+str(r.randint(0,int(ticketnummer))))
        file.close()

    with open('keylist.txt', 'r') as f:
        lines = f.read().splitlines()

    value = ticketnummer + lines[-1]
    passDict=[]
    key= r.randint(0,9)
    def encryptor(saltkey):
        for index in value:
            passDict.append(str(index) + str(saltkey))

        for item in passDict:
            Value(item)
        valEncrypted = "".join(encryption)

        with open('keylist.txt', 'r') as f:
            fist = f.read().splitlines()
        print(passDict)
        print(encryption)
        print(valEncrypted)
        return valEncrypted

    UEVstring= encryptor(key)
    return UEVstring



vn= input("Wat is uw voornaam: ")
an= input("Wat is uw achternaam: ")
gd= input("Voer uw geboortedatum in (dd-mm-yyyy): ")
gs= input("Bent u een man of vrouw: ")
addr= input("Voer uw straatnaam en huisnummer in: ")
pc= input("Wat is uw postcode: ")
wp= input("Waar woont u: ")
tel= input("wat is uw telefoonnummer: ")
ticketnr=[]

for x in range(0,9):
        ticketnr.append(str(r.randint(0,9)))
ticketnummer = "".join(ticketnr)


cryptedpass= hash(encrypt(ticketnummer,an))
transfer = open('database.txt','a')
transfer.write("voornaam: "+vn+", achternaam: "+an+", geboortedatum: "+gd+", geslacht: "+gs+", adres: "+addr+
               ", postcode: "+pc+", woonplaats: "+wp+", telefoonnummer "+tel+", ticketnummer: "+str(cryptedpass)+"\n")
transfer.close()


