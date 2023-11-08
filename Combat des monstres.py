#Créé par Xavier Moorman
#TP3


import random

niveau = 1
vie_usager = 20



def animation():
    while True:
        print("\n .-------.    ______\n/   o   /|   /\     \\n/_______/o|  /o \  o  \\n| o     | | /   o\_____\\n|   o   |o/ \o   /o    /\n|     o |/   \ o/  o  /\n'-------'     \/____o/")
        
        
def combattre_adversaire():
    print("Vous décidez de combattre le monstre de niveau ",niveau,"On roule les dés...")
    animation()
    nbr_dice1 = random.randint(1, 6)
    nbr_dice2 = random.randint(1, 6)
    nbr_dice_ajoute = nbr_dice1 +nbr_dice2
    force_adversaire = random.randint(1, niveau)
    print("Vous avez eu un ",nbr_dice1," et un ",nbr_dice2," (donc un ",nbr_dice_ajoute,") ! Le monstre a une force de ",force_adversaire,"")
    if force_adversaire >=nbr_dice_ajoute:
        print()
    


def ouvrir_autre_porte():
    var = vie_usager - 1
    proposer_combat()

def regles_du_jeu():
    print("Voici les règles du jeu!\n******************************************")
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0.L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

def mort_usager():
    niveau = 0
    rejouer = int(input("Vous êtes mort! Voulez-vous recommencer ou quitter la partie?\n1- Rejouer 2- Quitter"))
    if rejouer == 1:
        niveau = 1
    elif rejouer == 2:
        quitter_jeu()

def quitter_jeu():
    print("Merci et au revoir...")
    exit()

def erreur():
    print("Erreur! Recommencez")
    exit()

while niveau == 1:
    print("Bienvenue dans le niveau ",niveau,"!")

    def proposer_combat():
        menu = int(input("Vous ouvrez une porte, il y a un monstre devant vous! Que voulez-vous faire? (Appuyez 1, 2, 3 ou 4 pour choisir)\n1- Combattre l'adversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie"))
        if menu == 1:
            combattre_adversaire()
        elif menu == 2:
            ouvrir_autre_porte()
        elif menu == 3:
            regles_du_jeu()
        elif menu == 4:
            quitter_jeu()
        else:
            erreur()








