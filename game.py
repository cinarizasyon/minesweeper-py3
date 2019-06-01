import util
import os
import start_menu
import game_screen
from minesweeper import minesweeper

game_level = ""
valid_options = ["1","2","3"]

def does_the_game_continue():
        return True

while game_level.lower() != 'q':
        start_menu.show()
        game_level = start_menu.choice()
        if valid_options.index(game_level) != -1:
                os.system("cls")
                game = minesweeper(int(game_level))
                game.generate_random_mines()
                while does_the_game_continue():
                        game_screen.show(game.get_boxes(),game.level)
                        input("Please select")





