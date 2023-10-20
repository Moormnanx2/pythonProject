# Jeu de devinettes
# Créé par Xavier Moorman 2023

import random
rejouer = True


while rejouer:
    nbr1 = int(input("Donnez-moi un nombre, il va être utilisé comme nombre minimum ou 'a': ")) #Nbr plus petit choisi
    nbr2 = int(input("Donnez-moi aussi votre nombre maximum ou 'b': ")) #Nbr plus grand choisi

    nbr_random = random.randint(nbr1, nbr2) #Choisir un nombre random dans les 2 nbr choisis au-dessus
    #print(nbr_random) #Print le nbr random choisi pour régler des bogues et permettre d'en trouver plus facilement
    reponse = True #Continue de faire le while de reponse, car c'est toujours vrai


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
                reponse = False #Arrête le deuxième while, donc ça permet au premier de recommencer


                nbr_essais = 0
            elif rejouerQ == "N":
                exit()
                rejouer = False #Arrête le code entièrement

            else:
                exit()
                rejouer = False #Arrête le code entièrement aussi
