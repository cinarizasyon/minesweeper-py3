import util
import os
from minesweeper import minesweeper

game_level = ""
valid_options = ["1","2","3"]
while game_level.lower() != 'q':
        os.system("cls")
        print("Welcome to Minesweeper Game!")
        print("Please select game level")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        print("Q) Quit")
        game_level = input("Your select is :")
        if valid_options.index(game_level) != -1:
                os.system("cls")
                print("Game started")
                game = minesweeper(int(game_level))
                game.generate_random_mines()




