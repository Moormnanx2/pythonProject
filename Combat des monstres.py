#Créé par Xavier Moorman
#TP3

import random, time

def regles_du_jeu():
    print("\n\n\nVoici les règles du jeu!")
    print("┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐")
    print("│Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.                  │")
    print("│Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.                                    │")
    print("│Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.      │")
    print("│Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.                                     │")
    print("│La partie se termine lorsque les points de vie de l’usager tombent sous 0.                                             │")
    print("│L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.│")
    print("└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘")

def stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires): #Statistiques
  if nbrvictoires < 10:

      print("\n\n\n┌─────────────────────────────────────────────────────────────────────────────┐")
      print("│Vous avez",vie_usager,"points de vie. Vous avez gagnés",nbrvictoires,"combats en total.             │")
      if nbrvictoires_de_suite == 0:
        print("│Vous avez perdu",nbrpertes_de_suite,"combats de suite.                                          │")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
      elif nbrvictoires_de_suite != 0:
        print("│Vous avez gagné",nbrvictoires_de_suite,"combats de suite.                                          │")
        print("└─────────────────────────────────────────────────────────────────────────────┘")
  elif nbrvictoires >= 10:
      print("\n\n\n┌──────────────────────────────────────────────────────────────────────────────┐")
      print("│Vous avez",vie_usager,"points de vie. Vous avez gagnés",nbrvictoires,"combats en total.             │")
      if nbrvictoires_de_suite == 0:
        print("│Vous avez perdu",nbrpertes_de_suite,"combats de suite.                                           │")
        print("└──────────────────────────────────────────────────────────────────────────────┘")
      elif nbrvictoires_de_suite != 0:
        print("│Vous avez gagné",nbrvictoires_de_suite,"combats de suite.                                          │")
        print("└──────────────────────────────────────────────────────────────────────────────┘")


def game():

  niveau = 1
  vie_usager = 20
  nbrvictoires_de_suite = 0
  nbrpertes_de_suite = 0
  nbrvictoires = 3

  while vie_usager>0:
    print("\n\n\n\nBienvenue dans le niveau",niveau,"!")
    print("\nVous ouvrez une porte, il y a un monstre devant vous!")
    force_adversaire1 = random.randint(1,5)
    force_adversaire2 = random.randint(1,5)
    force_adversaire = force_adversaire1 + force_adversaire2

    menu = int(input("Que voulez-vous faire? (Appuyez 1, 2, 3, 4 ou 5 pour choisir)\n1- Combattre l'adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Afficher vos stats\n5- Quitter la partie\n\n"))

    if menu == 1: #Combattre le monstre
      if nbrvictoires <3:
        #Si le nbr de victoires de suite n'est pas 3,
        #le monstre n'est pas un boss.
        print("Vous combattez un monstre qui a une force de",force_adversaire,".\nOn roule les dés...")
        time.sleep(5)

        nbr1=1
        nbr2=6
        nbr_dice1 = random.randint(nbr1, nbr2)
        nbr_dice2 = random.randint(nbr1, nbr2)
        nbr_dice_ajoute = nbr_dice1+nbr_dice2

        print("Vous avez eu un ",nbr_dice1," et un ",nbr_dice2," (donc un",nbr_dice_ajoute,")! Le monstre a une force de",force_adversaire)

        if force_adversaire <nbr_dice_ajoute: #Monstre Battu

          vie_usager += force_adversaire
          print("Vous avez battu le monstre! Vous gagnez",force_adversaire,"vies!")
          nbrvictoires_de_suite += 1
          nbrpertes_de_suite = 0
          nbrvictoires +=1
          niveau += 1
          stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires)
          time.sleep(3)

        elif force_adversaire > nbr_dice_ajoute: #Monstre Perdu

          vie_usager -= force_adversaire
          print("Vous avez perdu! Vous perdez",force_adversaire,"vies!")
          nbrpertes_de_suite += 1
          nbrvictoires_de_suite = 0
          stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires)
          time.sleep(3)


      elif nbrvictoires >=3 :
        #Si le nbr de victoires de suite est plus grand ou égal à 3,
        #le monstre est un boss.
        print("Vous combattez le magicien qui a une force de",force_adversaire,". \nOn roule les dés...")
        time.sleep(5)

        nbr1=1
        nbr2=6
        nbr_dice1 = random.randint(nbr1, nbr2)
        nbr_dice2 = random.randint(nbr1, nbr2)
        nbr_dice_ajoute = nbr_dice1+nbr_dice2


        print("Vous avez eu un ",nbr_dice1," et un ",nbr_dice2," (donc un",nbr_dice_ajoute,")! Le vilain magicien a une force de",force_adversaire,".")

        if force_adversaire <nbr_dice_ajoute: #Boss Battu
          vie_usager += force_adversaire

          print("Vous avez battu le monstre, mais il vous lance un éclair! Vous perdez ",force_adversaire1," vies")
          vie_usager -= force_adversaire1
          print("Vous gagnez",force_adversaire - force_adversaire1,"vies!")
          nbrvictoires_de_suite += 1
          nbrpertes_de_suite = 0
          nbrvictoires +=1
          niveau += 1
          stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires)
          time.sleep(3)

        elif force_adversaire > nbr_dice_ajoute: #Boss Perdu
          print("Vous avez perdu! Vous perdez",force_adversaire,"vies!")
          vie_usager -= force_adversaire
          nbrpertes_de_suite += 1
          nbrvictoires_de_suite = 0
          stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires)
          time.sleep(3)


    elif menu == 2: #Choisir une autre porte

      vie_usager -= 1
      print("Vous avez choisi de vous sauver du monstre! Vous perdez une vie.")
      stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires)
      time.sleep(3)

    elif menu == 3: #Règles du jeu

      regles_du_jeu()
      time.sleep(3)


    elif menu == 4: #Statistiques

      stats(vie_usager, nbrvictoires_de_suite, nbrpertes_de_suite, nbrvictoires)
      time.sleep(3)


    elif menu ==5: #Quitter le jeu
        print("Merci et au revoir...")
        exit()


    else: #Pas chiffre de 1 à 5, donc le code s'arrête

      print("Erreur! Recommencez!")
      exit()

game()