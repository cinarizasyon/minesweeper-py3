import os
def show():
    os.system("cls")
    print("Welcome to Minesweeper Game!")
    print("Please select game level")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    print("Q) Quit")
    
def choice():
    return input("Your select is :")