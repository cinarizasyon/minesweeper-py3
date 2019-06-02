import util
import os
import sys
import start_menu
import game_screen
import keyboard
from minesweeper import minesweeper

game_level = ""
valid_options = ["1","2","3"]
curr_coord = [0,0]

def change_box(game):
        #control this function
        try:
                currX = curr_coord[0]
                currY = curr_coord[1]
                tmpX = currX
                tmpY = currY
                if keyboard.is_pressed(24): tmpY = currY - 1 # up arrow
                elif keyboard.is_pressed(25): tmpY = currY + 1 #down arrow
                elif keyboard.is_pressed(26): tmpY = currX + 1 #right arrow
                elif keyboard.is_pressed(27): tmpY = currX - 1 #left arrow

                if util.is_valid_seperation(tmpX,tmpY,game.level.row_count,game.level.column_count):
                        game.unselect_box(currX,currY)
                        currX = tmpX
                        currY = tmpY
                        game.select_box(currX,currY)
        except:
                print(sys.exc_info()[0])

while game_level.lower() != 'q':
        start_menu.show()
        game_level = start_menu.choice()
        if valid_options.index(game_level) != -1:
                game = minesweeper(int(game_level))
                game.generate_random_mines()
                does_the_game_continue=True
                while does_the_game_continue:
                        game_screen.show(game.get_boxes(),game.level)
                        change_box(game)
                        


                
                        







