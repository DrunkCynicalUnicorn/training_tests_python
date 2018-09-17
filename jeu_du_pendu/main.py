# -*-coding:Utf-8 -*


from random import choice
import pickle
import os

from data import *
from func import *


scores = get_scores()

user = get_user(scores)

play = True

while play:
    input("Bienvenue dans le jeu du pendu. Vous devez deviner un mot en \
proposant des lettres. Vous avez droit à {} tentatives au total. Si la lettre \
se trouve dans le mot, votre coup n'est pas décompté.\nGood Luck !\n".format(permitted_strokes))

    word = get_random_word()

    score = lets_play(word)

    scores[user] += int(score)

    print("Votre score total est désormais de {} pts".format(scores[user]))
    
    save_scores(scores)

    while 1:
        try_again = input("Voulez-vous continuer ? Taper 'y' pour 'oui', 'n' pour 'non' : ")
        if try_again == "y":
            break
        elif try_again == "n":
            play = False
            break
        else:
            continue

input("Merci d'avoir joué avec moi ! ")
exit()

