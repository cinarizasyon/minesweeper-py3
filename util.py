from box import box
import colorama
from termcolor import colored, cprint
from os import system, name

colorama.init()


def get_neighboord(xCoord, yCoord, row_count, col_count):
    test_seperation = [
        [xCoord-1, yCoord+1], [xCoord, yCoord+1], [xCoord+1, yCoord+1],
        [xCoord-1, yCoord], [xCoord+1, yCoord],
        [xCoord-1, yCoord-1], [xCoord, yCoord-1], [xCoord+1, yCoord-1],
    ]
    neighbors = []

    for seperation in test_seperation:
        if(is_valid_seperation(
                seperation[0], seperation[1],
                row_count, col_count)):

            neighbors.append(seperation)

    return neighbors


def is_valid_seperation(currX, currY, row_count, col_count):
    return (currX >= 0 and
            currY >= 0 and
            currX < row_count and
            currY < col_count)


def split_list(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def print_array(array):
    for item in array:
        print(item, sep=' ', end='', flush=True)


def print_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            print(matrix[row][column], sep=' ', end='', flush=True),
        print("")


def print_boxes(boxes):
    for row in range(len(boxes[0])):
        for column in range(len(boxes)):
            print(boxes[column][row].get_coord(), sep=' ', end='', flush=True),
        print("")


def print_table(table):
    for row in range(len(table)):
        for col in range(len(table[0])):
            if str(table[col][row]).find(":s") != -1:
                colored_text = colored(
                    "  " + table[col][row].replace(":s", "")
                                          .replace(":o", "") +
                    "  ", "grey", "on_white")
                print("{0}{1}".format(colored_text, "|"), end='', flush=True),
            elif str(table[col][row]).find("F") != -1:
                colored_text = colored(
                    "  " + table[col][row] + "  ", "grey", "on_yellow")
                print("{0}{1}".format(colored_text, "|"), end='', flush=True),
            elif str(table[col][row]).find("M") != -1:
                colored_text = colored(
                    "  " + table[col][row] + "  ", "white", "on_red")
                print("{0}{1}".format(colored_text, "|"), end='', flush=True),
            elif str(table[col][row]).find(":o") != -1:
                colored_text = colored(
                    "  " + table[col][row].replace(":o", "") +
                    "  ", "white", "on_green")
                print("{0}{1}".format(colored_text, "|"), end='', flush=True),
            else:
                print("{0}{1}{2}{3}".format(
                    "  ", table[col][row], "  ", "|"), end='', flush=True),
        print("", flush=True)
        for col in range(len(table[0])):
            print("-----+", sep='', end='', flush=True),
        print("", flush=True)


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
