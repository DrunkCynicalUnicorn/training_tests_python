import json

def exercice_1():
    # Créer un fichier texte (carte.txt) contenant la variable text
    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW"
    with open("carte.txt", "w") as writter_object:
        writter_object.write(text)

        
def exercice_2():
    # Afficher en console le fichier texte créé à l'exercice 1
    with open("carte.txt", "r") as reader_object:
        maze = reader_object.read()
        print(maze)

def exercice_3(lettre):
    # Vérifier si la lettre entrée en paramètre est présente
    # dans le fichier créé à l'exercice 1 (retourner True si
    # la lettre est présente et False sinon)
    letter_test = False
    with open("carte.txt", "r") as reader_object:
        maze = reader_object.read()
        for element in maze:
            if lettre is element:
                letter_test = True
    return letter_test

def exercice_4(lettre):
    # Trouver la position de la lettre passée en paramètre dans
    # le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    # doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    # 4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    # l'exercice 1.
    

    with open("carte.txt", "r") as reader:                          # pas encore satisfaisant :
        line_list_maze = reader.readlines()                         # ne retourne que la 1re
        for nb_line, line in enumerate(line_list_maze):             # occurence de "W" car return
            if lettre.upper() in line:                              # met fin à l'exécution de la
                for i_char, char in enumerate(line):                # fonction => renvoyer le résultat
                    if lettre == char:                              # sous la forme d'un liste où l'on
                        return (line.index(lettre), nb_line)        # .append des tuples à chaque tour
                                                                    # de boucle for pour y pallier
        

def exercice_5():
    # Créer un dictionnaire contenant toutes les lettres présentes
    # dans le fichier texte de l'exercice avec leur nombre d'apparition
    # dans le fichier : {"W": 22, "M": 1}
    nb_char = {}
    with open("carte.txt", "r") as reader_object:
        for element in reader_object.read():
            if element in nb_char:
                nb_char[element] += 1
            else :
                nb_char[element] = 1
    print(nb_char) 

            
def exercice_6():
    # Tranformer le fichier texte de l'exercice 1 en fichier JSON
    with open("carte.txt", "r") as reader_object:
        maze = reader_object.readlines()
    with open("carte.json", "w") as writter_object:
        maze_json = []
        for i, char in enumerate(maze):
            maze_json.append({i : char})
        writter_object.write(json.dumps(maze_json))
	    

	
    pass

def exercice_7():
    # Demander si le joueur veut continuer le jeu (avec input). Si la
    # réponse est "oui" ou "o", on repose la même question. Si la réponse
    # est "non" ou "n", la boucle s'arrête. Si une autre réponse est donnée,
    # afficher "Réponse non correcte" puis reposer la question.
    play = True
    while play == True:
        decision = input("Voulez-vous continuer le jeu ? Taper \"oui\"/\"non\" : ")
        if decision.lower() == "oui" or decision.lower() == "o":
            continue
        elif decision.lower() == "non" or decision.lower() == "n":
            play = False
        else:
            print("Réponse non correcte")
            continue

    
if __name__ == "__main__":    
    exercice_1()
    exercice_2()
    print(exercice_3("M"))
    print(exercice_4("M"))
    exercice_5()
    exercice_6()
    exercice_7()
