import random

def sommeTroisDes():
    desA = random.randrange(1, 6, 1)
    desB = random.randrange(1, 6, 1)
    desC = random.randrange(1, 6, 1)
    somme = desA + desB + desC
    return somme

def compteNombreDeN(N, nbSim):
    counter = 0
    for k in range(0, nbSim):
        sommeTroisDes()
        if sommeTroisDes() == N:
            counter += 1
    return counter


N = int(input("Saisir une somme : "))
nbSim = int(input("Saisir un nombre de lancers : "))

count = compteNombreDeN(N, nbSim)

print("La valeur ", N, " est sortie ", count, " fois sur les ", nbSim, " lancers.")
