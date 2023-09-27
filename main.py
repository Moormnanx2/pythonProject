# Créé par Xavier Moorman 2023

nbr_etoiles = int(input("Donnez-moi le nombre d'étoiles à print: "))

while nbr_etoiles != 0:  # Tant que le nbr_etoiles n'est pas égal à 0, le code va continuer.
    for i in range(nbr_etoiles):  # Le nombre d'étoiles = au nbr de fois que ça va print les *.
        print("*", end="")  # Print une étoile et reste sur la même ligne.

    nbr_etoiles = nbr_etoiles - 1  # Enlève un à nbr_etoiles chaque fois que la boucle se répète.
    print("\n ")  # \n permet de sauter une ligne






