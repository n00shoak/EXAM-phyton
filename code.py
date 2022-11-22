# EXAM PHYTON :

print("partie 1:")

print ("tableau initiale :")
myTable = [1,2,3,4,5]
print(myTable)

print ("l'emplacement n°3 vint a l'emplacement n°1")
myTable.insert(1,4)
myTable.pop(4)
print(myTable)

print ("l'emplacement n°2 vint a l'emplacement n°4")
myTable.insert(4,2)
myTable.pop(2)
print(myTable)
print("")


print ("partie 2 :")

myTable = [12,23,56,78,10,33,75]
print("avant tri a bulle :")
print(myTable)

for i in range (len(myTable)) :
    if i != 0 and myTable[i - 1] > myTable[i]:
        myTable.insert(i - 1 , myTable[i])
        myTable.pop(i + 1)

print("après tri a bulle :")
print(myTable)
print("")


print ("partie 3 :")
print("avant tri a bulle :")
myTable = [12,23,56,78,10,33,75]
print(myTable)

for b in range (len(myTable)):
    for i in range (len(myTable)) :
        if i != 0 and myTable[i - 1] > myTable[i]:
            myTable.insert(i - 1 , myTable[i])
            myTable.pop(i + 1)

print("après tri a bulle :")
print(myTable)