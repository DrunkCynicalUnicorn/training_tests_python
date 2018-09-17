
from random import choice
import pickle
import os

from data import *



def get_scores():

    """ function importing the scores_file if exists, or creating an empty
        hash table if not, to attribute a value to 'score' variable """
    
    if os.path.exists(scores_file):
        with open(scores_file, "rb") as binary_reader:
            depickler = pickle.Unpickler(pickle_reader)
            scores = depickler.load()
    else:
        scores = {}
    return scores





def get_user():

    """ function identifying or creating a username in scores hash table.
    Returns a user_name to capture in a 'user' var """
    
    user_name = input("Entrez votre nom d'utilisateur courant : ")
    if user_name in scores.keys():
        print("Je vous ai trouvé(e), {}. Votre score est actuellement de {}".format\
              (user_name, scores[user_name]))
    else:
        print("Vous n'êtes pas un utilisateur enregistré...")
        choice_loop = True
        while choice_loop:
            user_choice = input("Vous pouvez taper \"info\" puis Entrée pour \
vérifier dans la liste des joueurs, ou Entrée pous vous logger \
en tant que nouvel utilisateur : ")
            if user_choice.lower() == "info":
                print("Liste des joueurs enregistrés :\n")
                for player in scores.keys():
                    print("{}".format(player))
                return get_user()
            else:
                print("Très bien, {}. Vous êtes désormais dans la liste des joueurs".format(user_name))
                scores[user_name] = 0
                break
    return user_name
                
        




def get_random_word():

    """ function picking a pseudo-random word in the words list
    already imported from data.py """
    
    return choice(words_list)



def lets_play():

    """ Games's core. Returns the player's remaining strokes, to be
    captured and converted in score right after """

    # this function is handling too many operations... and it might be
    # a little bit odd to have such a big function directly returning a score
    # = > have to decompose it in sub-functions !!!

    found_letters = str()
    remaining_strokes = permitted_strokes

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
        print("Désolé l'ami(e), vous n'avez plus d'essais... Vous n'avez donc marqué aucun point !")
    else:
        print("Il vous restait {} tentatives, vous avez donc marqué {} points".format(remaining_strokes))

    return remaining_strokes
            




def save_score():
    with open(scores_file, "wb") as writter:
        pickler = pickle.Pickler(writter)
        pickler.dump(scores)


	


			


