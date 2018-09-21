import random

def maze(size=10):
    """
    Créer une carte de labyrinthe en console de largeur et de hauteur size
    Le labyrinthe est encadré par des murs et les murs sont disposés aléatoirement dans la carte comme ceci :
    wwwwwww
    w..w..W
    ww..WWW
    WWW.WWW
    W...WWW
    WWW..WW
    WWWWWWW
    (size=7)
    """

    maze_structure = str()
    for line in range(size):
        if line == 0 or line == (size - 1):
            maze_structure += ("W" * size + "\n")
        else:    
            maze_structure += ("W" + ("".join(random.choices("W.", k = size - 2))) + "W\n")
    return maze_structure

def maze_list(size=10):
    """
    Même exercice que pour la fonction maze mais cette fois le labyrinthe doit être renvoyé sous forme
    d'une liste avec une chaine de caractères pour chaque ligne
    """

    wall_line = "W" * size
    maze_structure = [wall_line]
    for line in range(size-2):
        maze_structure.append("W" + ("".join(random.choices("W.", k = size - 2))) + "W")
    maze_structure.append(wall_line)
    return maze_structure

def maze_2(size=10, pourcent_w=50):
    """
    Même exercice que maze mais avec un pourcentage de w à l'intérieur de labyrinthe défini
    par le paramètre pourcent
    """

    nb_w_sprites = floor(((size-2) ** 2) * (percent_w / 100))
    nb_empty_sprites = (size-2)**2 - nb_w_sprites
    string_sprites_bank = (nb_w_sprites * "W") + (nb_empty_sprites * ".")

    sprites_list_bank = []
    for sprite in string_sprites_bank:
        sprites_list_bank.append(sprite)


    maze_structure = str()
    line_breaker = size
    for char in range(size**2):
        if char < size or char > (size*size - size):
            maze_structure += "W"
        elif char == line_breaker - 1 or char == line_breaker - 1 + size:
            maze_structure += "W"
        elif char == line_breaker or char == line_breaker + size:
            maze_structure += "\nW"
            line_breaker = char
        else:
            maze_structure += sprites_list_bank.pop(random.randrange(len(sprites_list_bank)))

    
    return maze_structure

def maze2_list(size=10, pourcent_w=50):
    """
    Même exercice que pour la fonction maze2 mais cette fois le labyrinthe doit être renvoyé sous forme
    d'une liste avec une chaîne de caractères pour chaque ligne
    """
    nb_w_sprites = floor(((size-2) ** 2) * (percent_w / 100))
    nb_empty_sprites = (size-2)**2 - nb_w_sprites
    string_sprites_bank = (nb_w_sprites * "W") + (nb_empty_sprites * ".") # operations' clarity has been prefered here, but it's doable to pack
                                                                          # these three lines into the last one, whithout using the 2 first intermediate
                                                                          # var
    sprites_list_bank = []
    for sprite in string_sprites_bank:     # = kind of hard work here, but join string method doesn't work
        sprites_list_bank.append(sprite)   # if its sep arg = "" 

    wall_line = "W" * size
    maze_structure = [wall_line]
    for line in range(size-2):
        chars = str()
        for i_char in range(size - 2):
            chars += sprites_list_bank.pop(random.randrange(len(sprites_list_bank))) # have to figure out how to fill a random line without calling for 
        line = "W{}W".format(chars)                                                  # the second "for loop", while keeping removing items from bank list
        maze_structure.append(line)                                                      # => TODO : in first place, try in shell to pop multiple objects from list

    maze_structure.append(wall_line)
    return maze_structure



def check_maze(test_maze):
    """
    La fonction renvoie True si le joueur peut se déplacer sur l'intégralité du labyrinthe (hormis les bords)
    """
    """ this edit tests whether it's possible, based on maze's first empty space a player will spot in, to move
        to the bottom right corner (border walls excluded), so for a list-shape maze, we're talking about position
        maze[size-2][size-2]. So while inner mazes here are randomly produced here, if this "out-position" is filled
        with a wall, the test will return False, even if it could be possible from start-position to run through
        the maze to this end-position """
        checked_maze = False
    
    if type(maze) is not list:
        maze = maze.splitlines()

    for line_num, chars in enumerate(maze):
        if "." in chars:
            x_loc = chars.index(".")
            y_loc = line_num
            break
        else:
            continue
    current_point = [y_loc, x_loc]

    tested_coor = []
    tested_coor.append(current_point)
    prev_point = list()
    test_process = True
    while test_process:
        
        y_loc, x_loc = current_point[0], current_point[1]
        
            ### NOT WORKING WHEN TESTING POS COOR whithout "stringing" the 1st test, which often return true because it seems to test the char, not the position itself, even with "is" instead of "==" 
            ### => modif test = put it in str() to test if position expressed in words are the same... = shitty way to do it, but i can't figure it out without a real position object
        if "out_tester[" + str(len(maze)-2) + "][" + str(len(maze)-2) + "]" == "out_tester[" + str(y_loc) + "][" + str(x_loc) + "]":
            checked_maze = True
            test_process = False          
        elif maze[y_loc][x_loc+1] == "." and [y_loc, x_loc+1] not in tested_coor:
            prev_point = current_point
            current_point = [y_loc, x_loc+1]
            tested_coor.append(current_point)
        elif maze[y_loc][x_loc-1] == "." and [y_loc, x_loc-1] not in tested_coor:
            prev_point = current_point
            current_point = [y_loc, x_loc-1]
            tested_coor.append(current_point)
        elif maze[y_loc+1][x_loc] == "." and [y_loc+1, x_loc] not in tested_coor:
            prev_point = current_point
            current_point = [y_loc+1, x_loc]
            tested_coor.append(current_point)
        elif maze[y_loc-1][x_loc] == "." and [y_loc-1, x_loc] not in tested_coor:
            prev_point = current_point
            current_point = [y_loc-1, x_loc]
            tested_coor.append(current_point)
        else :
            if current_point == prev_point:
                test_process = False
                break
            else:
                current_point = prev_point
                continue

    return checked_maze


