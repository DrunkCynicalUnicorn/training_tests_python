
from random import choice
import pickle
import os

from data import *



def get_scores():

    """ function importing the scores_file if exists, or creating an empty
        hash table if not, to attribute a value to 'scores' variable """
    
    if os.path.exists(scores_file):
        with open(scores_file, "rb") as binary_reader:
            depickler = pickle.Unpickler(binary_reader)
            def_scores = depickler.load()
    else:
        def_scores = dict()
    return def_scores





def get_user(scores):

    # ma 1re version ne prenait pas le dict scores en paramètres :
    # l'enchaînement des 2 1res fonctions, get_scores() et get_user() marchait
    # alors très bien lorsque je lançait CE script de fonction dans le shell, mais
    # dans le fichier main, cette fonction get_user(), sans paramètre donc
    # dans sa 1re version, levait une NameError disant
    # que le nom 'scores" n'était pas assigné... Ne comprenant pas bien comment ça
    # pouvait fonctionner depuis ce fichier func.py mais pas depuis le fichier main,
    # qui après tout ne fait qu'appliquer les mêmes fonctions, j'ai essayé en passant
    # 'scores' en paramètres et ça fonctionne. Fausse bonne nouvelle, car je ne comprends
    # absolument pas pourquoi il faut lui passer le dictionnaire en paramètres pour qu'elle
    # fonctionne. Il me semblait que si une fonction ne trouvait pas une variable dans son
    # espace local, elle le cherchait dans l'espace parent, or dans le fichier main la variable
    # scores était très clairement définie à la ligne précédente, et se voyait bien assigner
    # une valeur

    """ function identifying or creating a username in scores hash table.
    Returns a user_name to capture in a 'user' var """
    
    user = input("\nEntrez votre nom d'utilisateur courant : ")
    if user in scores.keys():
        print("Je vous ai trouvé(e), {}. Votre score est actuellement de {}. Bonne partie".format\
              (user, scores[user]))
    else:
        print("\nVous n'êtes pas un utilisateur enregistré...")
        choice_loop = True
        while choice_loop:
            user_choice = input("\nVous pouvez taper \"info\" puis Entrée pour \
vérifier dans la liste des joueurs, ou Entrée pous vous logger \
en tant que nouvel utilisateur : ")
            if user_choice.lower() == "info":
                print("Liste des joueurs enregistrés : ")
                for player in scores.keys():
                    print("{}".format(player))
                return get_user(scores)
            else:
                print("\nTrès bien, {}. Vous êtes désormais dans la liste des joueurs, avec 0 points".format(user))
                scores[user] = 0
                break
    return user
                
        




def get_random_word():

    """ function picking a pseudo-random word in the words list
    already imported from data.py """
    
    return choice(words_list)



def lets_play(word):

    # idem que pour la fonction get_user() : sans paramètre, elle ne reconnait
    # pas la variable 'word", qui a reçu le résultat de get_random_word pourtant.
    # lorsque je teste dans le shell lancé depuis le fichier main(), une fois l'erreur
    # levée, la variable word a pourant bien reçu le résultat de get_random_word()

    """ Games's core. Returns the player's remaining strokes, to be
    captured and converted in score right after """

    # this function is handling too many operations... and it might be
    # a little bit odd to have such a big function directly returning a score
    # = > have to decompose it in sub-functions !!!

    found_letters = str()
    remaining_strokes = permitted_strokes
    print("Le mot que vous devez trouver comporte {} lettres\n".format(len(word)))

    while remaining_strokes > 0:
        print("Il vous restes {} chances\n".format(remaining_strokes))
        letter_test = input("Proposez une lettre et appuyez sur Entrée : ")


        try:
            assert letter_test not in found_letters
        except AssertionError:
            print("Vous avez déjà testé et découvert cette lettre...")
            continue

        
        
        
        if letter_test in word:
            print("Bravo ! Vous avez découvert la lettre {}\n".format(letter_test))
            for letter in word:
                if letter == letter_test:
                    found_letters += letter
        else:
            remaining_strokes -= 1
            print("Désolé, la lettre {} ne se trouve pas dans le mot\n".format(letter_test.upper()))
            

                      

        if len(word) == len(found_letters):
            print("Félicitations, vous avez gagné en découvrant le mot {}\n".format(word.upper()))
            break
        else:
            print("Voici ce que vous avez déjà découvert :\n")
            for letter in word:
                if letter not in found_letters:
                    print("*".center(50))
                else:
                    print(letter.upper().center(50))



    if remaining_strokes == 0:
        print("\nDésolé l'ami(e), vous n'avez plus d'essais... Vous n'avez donc marqué aucun point !")
    else:
        print("\nIl vous restait {0} tentatives, vous avez donc marqué {0} points".format(remaining_strokes))

    return remaining_strokes
            




def save_scores(scores):

    # là encore, ne fonctionnait pas sans argument... dans le fichier main, c'était la ligne
    # d'appel de la fonction elle-même qui posait problème, et non comme précédemment l'usage
    # de certaines variables dans le bloc d'instructions de la fonction (variables définies en dehors du
    # bloc.
    # Comment python peut-il affirmer que l'appel save_scores(), dans le fichier main,
    # n'est pas reconnu, alors même
    # que j'ai importé un module comportant cette fonction (bien sûr, j'ai vérifié l'orthorgraphe, là
    # n'était pas le problème) ???
    
    with open(scores_file, "wb") as writter:
        pickler = pickle.Pickler(writter)
        pickler.dump(scores)


	


			


