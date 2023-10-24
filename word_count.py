# Made by Xavier Moorman en 2023, aidé par Alexandre Wilbur et Mathéo Bui


def count_word(phrase=str(input("Donnez-moi votre phrase!: "))): #Fonction permet d'être appelée n'importe où
    word_count = len(phrase .split())
    return(word_count) #Donne le nombre de mots de la phrase

#hello = count_word() #Tester la fonction
#print(hello) #Print le nombre de mots
