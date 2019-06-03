import util
import os
import sys
import game_screen
from minesweeper import minesweeper
from pynput import keyboard

game_level = ""
start_menu_valid_options = ["1","2","3","Q"]
game_valid_options = ["KEY.UP","KEY.DOWN","KEY.RIGHT","KEY.LEFT","ENTER","F"]
game = None
curr_coord = [0,0]

def game_choice(choice):
        global game, curr_coord
        if choice in game_valid_options:
                currX = curr_coord[0]
                currY = curr_coord[1]
                tmpX = currX
                tmpY = currY
                if choice == "KEY.UP": 
                        tmpY = currY - 1
                elif choice == "KEY.DOWN": 
                        tmpY = currY + 1
                elif choice == "KEY.RIGHT": 
                        tmpX = currX + 1
                elif choice == "KEY.LEFT": 
                        tmpX = currX - 1
                elif choice == "ENTER":
                        pass
                elif choice == "F":
                        pass
                
                if util.is_valid_seperation(tmpX,tmpY,game.level.row_count,game.level.column_count):
                        game.unselect_box(currX,currY)
                        currX = tmpX
                        currY = tmpY
                        game.select_box(currX,currY)
                        curr_coord = [currX,currY]
                        game_screen.show(game.get_boxes(),game.level)
                        print("currX {0} currY {1} tmpX {2} tmpY {3}".format(currX,currY,tmpX,tmpY))
                else:
                        print("not valid sep." + choice)

def start_menu_choice(choice):
                global game
                game = minesweeper(int(choice))
                game.generate_random_mines()
                game_screen.show(game.get_boxes(),game.level)
                with keyboard.Listener(on_press=on_game_press) as game_listener:
                        game_listener.join()

def on_start_menu_press(key):
    try:
        if str.upper(key.char) in start_menu_valid_options:
                game_level = str.upper(key.char)
                if game_level == "Q":
                        return False
                # menu_listener.stop()
                start_menu_choice(game_level)
        else:
            print('Please only select options in menu.')
    except AttributeError:
        print('Please only select options in menu.')

def on_game_press(key):
    try:
        game_choice(str.upper(key.char))
    except AttributeError:
        if key == keyboard.Key.up : game_choice("KEY.UP")
        elif key ==  keyboard.Key.down : game_choice("KEY.DOWN")
        elif key == keyboard.Key.right : game_choice("KEY.RIGHT")
        elif key == keyboard.Key.left : game_choice("KEY.LEFT")


os.system("cls")
print("Welcome to Minesweeper Game!")
print("Please select game level")
print("1) Easy")
print("2) Medium")
print("3) Hard")
print("Q) Quit")
with keyboard.Listener(on_press=on_start_menu_press) as menu_listener:
        menu_listener.join()
                        


                
                        







