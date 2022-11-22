# EXAM PHYTON :

print("partie 1:")

print ("tableau initiale :")
myTable = [1,2,3,4,5]
print(myTable)

print ("l'emplacement n3 vint a l'emplacement n1")
myTable.insert(1,4)
myTable.pop(4)
print(myTable)

print ("l'emplacement n2 vint a l'emplacement n4")
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

print("apres tri a bulle :")
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

print("apres tri a bulle :")
print(myTable)
print("")

# partie 4 :
#  1- le tr à bulles est considéré comme très lent car il nécéssite un nombres d'actions important 
# démultiplier par la longueur du tableau
#  2- si l'ont pars du principe qu'une actions nécéssite une seul frame pour s'executer : 
# le tableau mets alors : ((3 frames * longueur du tableau) +1) * longueur du tableau
# le nombre de frame par seconde lui est dépendant du système executant le programme



print ("pratie 5 :")
print ("cadrillage de base:")
ligneA = ["0","0","0"]
ligneB = ["0","0","0"]
ligneC = ["0","0","0"]

print (ligneA)
print (ligneB)
print (ligneC)

# ajout du symbole
end = 0
player = "O"
while end == 0 :
    
    # joueur O :
    print ("joueur", player,": quel ligne  (1 , 2 , 3)")

    i = input()
    if i == "1" :
        print ("quel case ?  (1 , 2 , 3)")
        i = input()
        
        if i == "1" :
            ligneA[0] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        elif i == "2" :
            ligneA[1] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        elif i == "3" :
            ligneA[2] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        else :
            print("mauvais input")

    elif i == "2" :
        print ("quel case : (1 , 2 , 3)")
        i = input()
                
        if i == "1" :
            ligneB[0] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        elif i == "2" :
            ligneB[1] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        elif i == "3" :
            ligneB[2] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        else :
            print("mauvais input")

    elif i == "3" :
        print ("quel case : (1 , 2 , 3)")
        i = input()
        
        if i == "1" :
            ligneC[0] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        elif i == "2" :
            ligneC[1] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        elif i == "3" :
            ligneC[2] = player
            print (ligneA)
            print (ligneB)
            print (ligneC)
        else :
            print("mauvais input")
    else :
        print("mauvais input")

    # check if someone won :
    if ligneA[0] == "O" and ligneB[1] == "O" and ligneC[2] == "O" :
        end = 1
    if ligneA[2] == "O" and ligneB[1] == "O" and ligneC[0] == "O" :
        end = 1

    if ligneA[0] == "O" and ligneA[1] == "O" and ligneA[2] == "O" :
        end = 1
    if ligneB[0] == "O" and ligneB[1] == "O" and ligneB[2] == "O" :
        end = 1
    if ligneC[0] == "O" and ligneC[1] == "O" and ligneC[2] == "O" :
        end = 1

    if ligneA[0] == "O" and ligneB[0] == "O" and ligneC[0] == "O" :
        end = 1
    if ligneA[1] == "O" and ligneB[1] == "O" and ligneC[1] == "O" :
        end = 1
    if ligneA[2] == "O" and ligneB[2] == "O" and ligneC[2] == "O" :
        end = 1
   
   
    if ligneA[0] == "x" and ligneB[1] == "x" and ligneC[2] == "x" :
        end = 1
    if ligneA[2] == "x" and ligneB[1] == "x" and ligneC[0] == "x" :
        end = 1

    if ligneA[0] == "x" and ligneB[0] == "x" and ligneC[0] == "x" :
        end = 1
    if ligneA[1] == "x" and ligneB[1] == "x" and ligneC[1] == "x" :
        end = 1
    if ligneA[2] == "x" and ligneB[2] == "x" and ligneC[2] == "x" :
        end = 1

    if ligneA[0] == "x" and ligneA[1] == "x" and ligneA[2] == "x" :
        end = 1
    if ligneB[0] == "x" and ligneB[1] == "x" and ligneB[2] == "x" :
        end = 1
    if ligneC[0] == "x" and ligneC[1] == "x" and ligneC[2] == "x" :
        end = 1

        
    if end == 1 :
        print ("player", player , "gagne !")

    #change player
    if player == 'O' :
        player = "x"
    elif player == "x" :
        player = 'O'

print ("end ")

   