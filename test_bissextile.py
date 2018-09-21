play = True

while play:

    

    bissextile = False 
    valid_year = False


    
    
    while valid_year != True:
        year = input("Entrez une année : ")
        try:
            year = int(year)
            valid_year = True
        except:
            print("L'année saisie est invalide")
            
        
        

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        bissextile = True
    else:
        bissextile = False

        

        

    if bissextile:
        print("L'année", year, "est bissextile")
    else:
        print("L'année", year, "n'est pas bissextile")

        


    choice = input("Tapez \'q\' pour quitter le programme, ou n'importe quelle \
touche pour continuer, puis Entrée : ")

    if choice.lower() == "q":
        play = False
    else:
        play = True
