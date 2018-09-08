from random import randrange
from math import ceil

play = True

bank = 1000


while play:



    validation_mise = False
    while validation_mise != True:
        print("Vous disposez d'une somme de", bank, "$")
        mise = input("Combien voulez-vous miser : ")
        try:
            mise = int(mise)
            assert 0 < mise <= bank
            bank -= mise
            print("Très bien. Vous avez paris", mise, "$ : votre banque est désormais de", bank, "$")
            validation_mise = True
        except ValueError:
            print("Vous n'avez pas entré une donnée valide : si ça ne se compte pas, ça ne se parie pas !")
            continue
        except AssertionError:
            print("Vous n'avez pas entré une somme valide : je ne prends pas les paris nuls, encore moins les paris négatifs, ou vous ne pouvez pas parier au-delà de vos moyens !")
            continue



    validation_bet = False
    while validation_bet != True:
        bet = input("Vous pouvez parier sur un numéro allant de 1 à 49. Sur quel numéro misez-vous : ")
        try:
            bet = int(bet)
            assert 0 <= bet <= 49         
            print("Vous avez parié sur le n°", bet)
            validation_bet = True
        except ValueError:
            print("Vous n'avez pas saisi une donnée valide : il faut entrer un nombre entre 0 et 49 inclus !")
            continue
        except AssertionError:
            print("La roulette n'est numérotée que de 0 à 49 inclus... veuillez parier sur un nombre inclus dans cette fourchette !")
            continue


    win_number = randrange(50)
    print("La roulette tourne...tourne...et la bille s'arrête finalement sur le numéro", win_number)

    if bet == win_number:
        bank += ceil(3 * mise)
        print("Félicitations, vous avez gagné. Votre banque est désormais de", bank, "$")
    elif bet % 2 == win_number % 2:
        bank += ceil(1.5 * mise)
        print("Arggggh... vous n'avez pas misé sur le bon numéro... mais sur la bonne couleur : vous récupérer votre mise et la moitié de celle-ci.\nVotre banque est désormais de", bank, "$")
    else:
        print("Désolé, vous n'avez ni le bon numéro, ni la bonne couleur... Votre banque est désormais de", bank)


    user_will = input("Taper n'importe quelle touche pour rejouer, ou \'q\' pour quitter le jeu, puis appuyez sur \'Entrée\' : ")
    if user_will.lower() == "q":
        play = False
    else:
        continue




    
