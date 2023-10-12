# Jeu de devinettes
# Créé par Xavier Moorman 2023

import random
rejouer = True


while rejouer:
    nbr1 = int(input("Donnez-moi un nombre, il va être utilisé comme nombre minimum ou 'a': "))
    nbr2 = int(input("Donnez-moi aussi votre nombre maximum ou 'b': "))

    nbr_random = random.randint(nbr1, nbr2)
    print(nbr_random)
    reponse = True


    nbr_essais = 0

    while reponse:

        question = int(input("Essayez de deviner le nombre choisi entre le nombre 'a' et 'b' par le programme: "))

        if question > nbr_random:
            print("Le nombre est trop grand!")
            nbr_essais = nbr_essais + 1

        elif question < nbr_random:
            print("Le nombre est trop petit!")
            nbr_essais = nbr_essais + 1

        else:
            nbr_essais = nbr_essais + 1
            print("Vous avez réussi en", nbr_essais, "essais!")
            rejouerQ = str(input("Voulez-vous rejouer? 'Y' ou 'N': "))
            if rejouerQ == "Y":
                print("\n\n")
                rejouer = True


                nbr_essais = 0
            elif rejouerQ == "N":
                exit()
                rejouer = False

            else:
                exit()

