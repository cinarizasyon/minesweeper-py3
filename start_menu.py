import os
import sys
from pynput import keyboard
valid_options=["1","2","3","Q"]
def show():
    os.system("cls")
    print("Welcome to Minesweeper Game!")
    print("Please select game level")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    print("Q) Quit")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    
def choice():
    return input("Your select is :")

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        if str.upper(key.char) in valid_options:
            if str.upper(key.char) == "Q":
                sys.exit(0)
            listener.stop()
        else:
            print('Please only select options in menu.')
    except AttributeError:
        print('Please only select options in menu.')

# Collect events until releasead
