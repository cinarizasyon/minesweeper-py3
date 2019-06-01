import util
import colorama
from termcolor import colored, cprint

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

# print(colored("test","grey","on_white"))

test2 = [1,2,3,4,5,6,7,8]
split = list(util.split_list(test2,3))
print(split[2][0])
# for a in len(split):
#     for b in len(split[0])
#         print(split[a][b],sep = ' ', end="")
