from functools import reduce

from bookingApplication import *
from cryptable import *

def decryptor(value):
    password=value
    splitPass=[]
    special=["[", "]", "}", "{", ":", ";", "+",",",".","?","-","_","=","~", "#", "*", "&","^","%"]
    test=[]
    counter=0
    tes2=[]

    for item in password:
        counter = counter + 1
        if item not in special:
            splitPass.append(item)
        else:
            splitPass.append(item)
            test.append(item)


    def getIndexPositions(listOfElements, element):
        ''' Returns the indexes of all occurrences of give element in
        the list- listOfElements '''
        indexPosList = []
        indexPos = 0
        while True:
            try:
                # Search for item in list from indexPos to the end of list
                indexPos = listOfElements.index(element, indexPos)
                # Add the index position in list
                indexPosList.append(str(indexPos))
                indexPos += 1
            except ValueError as e:
                break

        return indexPosList


    for item in test:
        if item in splitPass:
            find=getIndexPositions(splitPass,item)
            if find not in tes2:
                tes2.append(find)
            print(find)

    import operator

    allIndexes=reduce(operator.concat, tes2)
    splitPass
    for item in allIndexes:
        splitPass[int(item)] = splitPass[int(item)]+splitPass[int(item)+1]+splitPass[int(item)+2]
        splitPass[int(item)+1]= "niks"
        splitPass[int(item) + 2] = "niks"

    while "niks" in splitPass:
        splitPass.remove("niks")

    numberPass=[]
    for item in splitPass:
        getKey(item)

    for item in keyValue:
        numberPass.append(item[0])
    saltedPass= "".join(numberPass)
    with open('keylist.txt', 'r') as f:
        salt = f.read().splitlines()
    tickernummer=int(saltedPass)-int(salt[-1])

    print(tickernummer)






   # print(password)
   # print(splitPass)
   # print(test)

   # print(tes2)
   # print(allIndexes)
   # print(splitPass)
   # print(keyValue)
   # print(numberPass)
   # print(saltedPass)
   # print(tickernummer)








decryptor(cryptedpass)