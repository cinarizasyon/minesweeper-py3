import util
import os
import sys
import game_screen
from minesweeper import minesweeper
from pynput import keyboard

game_over = False
start_menu_valid_options = ["1", "2", "3", "Q"]
game_valid_options = ["KEY.UP", "KEY.DOWN",
                      "KEY.RIGHT", "KEY.LEFT", "KEY.ENTER", "F"]
curr_coord = [0, 0]
flag_count = 0
game_level = ""


def game_choice(choice):
    global game, curr_coord, flag_count, game_over, curr_coord
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
        elif choice == "KEY.ENTER":
            game_over = game.open_box(tmpX, tmpY)
        elif choice == "F":
            toggle_flag = game.toggle_flag(tmpX, tmpY, flag_count)
            if toggle_flag is True:
                flag_count += 1
            elif toggle_flag is False:
                flag_count -= 1

        if util.is_valid_seperation(
                tmpX, tmpY,
                game.level.row_count, game.level.column_count):

            game.unselect_box(currX, currY)
            currX = tmpX
            currY = tmpY
            game.select_box(currX, currY)
            curr_coord = [currX, currY]
            game_screen.show(game.get_boxes(), game.level)
            print("Mines left: {}".format(game.level.mine_count - flag_count))
            # print("currX {0} currY {1} tmpX {2} tmpY {3}".format(
            #                                               currX,currY,tmpX,tmpY))


def start_menu_choice(choice):
    global game
    game = minesweeper(int(choice))
    game.generate_random_mines()
    game_screen.show(game.get_boxes(), game.level)
    with keyboard.Listener(on_press=on_game_press) as game_listener:
        game_listener.join()


def on_start_menu_press(key):
    global game_over
    try:
        if str.upper(key.char) in start_menu_valid_options:
            game_level = str.upper(key.char)
            if game_level == "Q":
                sys.exit(0)
                return False
            start_menu_choice(game_level)
            init()
        else:
            print('Please only select options in menu.')
    except AttributeError:
        print('Please only select options in menu.')


def on_game_press(key):
    global game_over
    if game_over:
        return False
    try:
        game_choice(str.upper(key.char))
    except AttributeError:
        if key == keyboard.Key.up:
            game_choice("KEY.UP")
        elif key == keyboard.Key.down:
            game_choice("KEY.DOWN")
        elif key == keyboard.Key.right:
            game_choice("KEY.RIGHT")
        elif key == keyboard.Key.left:
            game_choice("KEY.LEFT")
        elif key == keyboard.Key.enter:
            game_choice("KEY.ENTER")


def draw_start_menu():
    util.clear()
    print("Welcome to Minesweeper Game!")
    print("Please select game level")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    print("Q) Quit")


def init():
    global game_over, game, curr_coord, flag_count
    game_over = False
    game = None
    curr_coord = [0, 0]
    flag_count = 0
    draw_start_menu()
    with keyboard.Listener(on_press=on_start_menu_press) as menu_listener:
        menu_listener.join()


def main():
    init()


if __name__ == "__main__":
    main()
