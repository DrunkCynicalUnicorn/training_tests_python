import random
from math import ceil, floor


def maze_list2(player, size=15, percent_w=50):

    """ produces a random list-shaped maze with walled-borders, in which you can
        set maze's size and wall's rate (mandatory wall, a.k.a. borders, are excluded
        from the rate, it will set the inner maze walls)
        Returns the maze_structure """

    nb_w_sprites = floor(((size-2) ** 2) * (percent_w / 100))
    nb_empty_sprites = (size-2)**2 - nb_w_sprites
    string_sprites_bank = (nb_w_sprites * "W") + (nb_empty_sprites * ".")

    sprites_list_bank = []
    for sprite in string_sprites_bank:
        sprites_list_bank.append(sprite)

    wall_line = "W" * size
    maze_structure = [wall_line]
    for line in range(size-2):
        chars = str()
        for i_char in range(size - 2):
            chars += sprites_list_bank.pop(random.randrange(len(sprites_list_bank))) 
        line = "W{}W".format(chars)
        maze_structure.append(line)
    maze_structure.append(wall_line)

    return maze_structure



def init_player(maze, player):

    """ initalize the player's position at first "empty" sprite
        Returns position in [x_pos, y_pos] list form """
    
    for line_num, chars in enumerate(maze):
        if "." in chars:
            x_pos = chars.index(".")
            y_pos = line_num
            break
        else:
            continue
    return [x_pos, y_pos]

    
            

def show_maze(maze, player, player_location):

    """ func charged to print the maze at game initialization and after each
        user's move
        Returns None and prints the structure """
    
    for line_num, line_chars in enumerate(maze):
        if player_location[1] == line_num:
            print(line_chars[:player_location[0]] + player + line_chars[player_location[0] +1:])
        else:
            print(line_chars)


def move(maze, player_location):

    """ takes a desired move in input, processes it to check if it's doable/valid, and returns
        the move in coordinates form, to be grabbed by player_pos var """
    
    move_submit = False
    while move_submit != True:
        move = input("Use Z/Q/S/D keys to submit a move, then hit \"Enter\" : ")
        if move.lower() not in ["z", "q", "s", "d"]:
            print("You didn't type a valid command... Getting out from the maze is gonna be long if you can't get a simple instruction...")
        else:
            move_submit = True

    
    if move.lower() == "z":
        if maze[player_location[1] - 1][player_location[0]] == "." :
            verified_move = [player_location[0], player_location[1] - 1]
        else:
            print("Can't you see the f...ing wall ?".upper().center(80))
            return player_location
    elif move.lower() == "s":
        if maze[player_location[1] + 1][player_location[0]] == "." :
            verified_move = [player_location[0], player_location[1] + 1]
        else:
            print("Can't you see the f...ing wall ?".upper().center(80))
            return player_location
    elif move.lower() == "q":
        if maze[player_location[1]][player_location[0] - 1] == ".":
            verified_move = [player_location[0] - 1, player_location[1]]
        else:
            print("Can't you see the f...ing wall ?".upper().center(80))
            return player_location
    elif move.lower() == "d":
        if maze[player_location[1]][player_location[0] + 1] == ".":
            verified_move = [player_location[0] + 1, player_location[1]]
        else:
            print("Can't you see the f...ing wall ?".upper().center(80))
            return player_location
    else:
        lets_play = False
        exit()
        



    return verified_move
            



    
    

def main():
    player = "F"
    maze = maze_list2(player, 30, 10)
    player_location = init_player(maze, player)


    lets_play = True
    while lets_play: 
        show_maze(maze, player, player_location)
        player_location = move(maze, player_location)
    


main()
