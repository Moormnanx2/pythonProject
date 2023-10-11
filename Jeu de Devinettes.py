# Jeu de devinettes
# Créé par Xavier Moorman 2023

import random

nbr1 = int(input("Le code va choisir un nombre au hasard entre a et b. Donnez-moi un nombre, il va être utilisé comme nombre minimum ou 'a': "))
nbr2 = int(input("Donnez-moi aussi votre nombre maximum ou 'b': "))

nbr_random = random.randint(nbr1, nbr2)
print(nbr_random)
nbr_essais = 0



def loop1():
    global nbr_essais
    question = int(input("Essayez de deviner le nombre choisi entre le nombre 'a' et 'b' par le programme: "))
    if question > nbr_random:
        print("Le nombre est trop grand!")
        nbr_essais= nbr_essais+1
        loop1()
    elif question < nbr_random:
        print("Le nombre est trop petit!")
        nbr_essais= nbr_essais+1
        loop1()
    else:
        nbr_essais= nbr_essais+1
        print("Vous avez réussi en",nbr_essais,"essais!")
        rejouer = str(input("Voulez-vous rejouer? 'Y' ou 'N': "))
        if rejouer == "Y":
                loop1()
                nbr_essais=0
        elif rejouer == "N":
            exit()
        else:
            exit()

loop1()