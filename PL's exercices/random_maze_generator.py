import random

def maze(size=15):
    
    """ string random maze generator of size arg*arg """
    
    maze_structure = str()
    line_breaker = size
    for i in range(size*size):
        if i < size or i > (size*size - size):
            maze_structure += "W"
        elif i == line_breaker - 1 or i == line_breaker - 1 + size:
            maze_structure += "W"
        elif i == line_breaker or i == line_breaker + size:
            maze_structure += "\nW"
            line_breaker = i
        else:
            maze_structure += random.choice("W.")
    return maze_structure

    # alternative possible : faire un labyrinthe de taille
    # (size - 2) * (size - 2), puis le remplir avec des "W" en début et fin de
    # ligne, et insérer au début et à la fin de la structure
    # ainsi obtenue deux lignes de W pour obtenir les bords




def maze_list(size=15):
    
    maze_structure = list()
    maze_line = "".center(size, "W") 
    for i in range(size):
        if i == (size - size) or i == (size - 1):
            maze_structure.append(maze_line)
        else:
            random_maze_line = "W" + "".join(random.choices("W.", k = size -2)) + "W"
            maze_structure.append(random_maze_line)
    return maze_structure
    

    """
    Ou encore : 
    line_listed_maze = maze(size)
    return line_listed_maze.splitlines()
    """    


