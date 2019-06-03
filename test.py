import util
import colorama
from termcolor import colored, cprint
from pynput import keyboard

colorama.init()

test = [
    [" ","1:s","2","3","4","5","6","7","8"],
    ["1"," ","F","F","2"," "," "," "," "],
    ["2","F","F","1"," "," "," "," "," "],
    ["3"," "," "," "," "," "," "," "," "],
    ["4"," ","F","F","2"," "," "," "," "],
    ["5"," ","F","F","2"," "," "," "," "],
    ["6"," ","F","F","2"," "," "," "," "],
    ["7"," ","F","F","2"," "," "," "," "],
    ["8"," ","F","F","2"," "," "," "," "],
]

util.print_table(test)
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

# Collect events until releasead
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

