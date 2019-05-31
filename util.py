from box import box
def get_neighboord(xCoord, yCoord, row_count, col_count):
    test_seperation = [
        [xCoord-1, yCoord+1], [xCoord, yCoord+1], [xCoord+1, yCoord+1],
        [xCoord-1, yCoord], [xCoord+1, yCoord],
        [xCoord-1, yCoord-1], [xCoord, yCoord-1], [xCoord+1, yCoord-1],
    ]
    neighbors = []

    for seperation in test_seperation:
        if(is_valid_seperation(seperation[0], seperation[1], row_count,col_count)):
            neighbors.append(seperation)

    return neighbors


def is_valid_seperation(currX, currY, row_count,col_count):
    return currX >= 0 and currY >= 0 and currX < row_count and currY < col_count

def print_matrix(matrix):
    for row in range(len(matrix[0])):
        for column in range(len(matrix)):
            print(matrix[column][row],sep=' ',end='',flush=True),
        print("")

def print_boxes(boxes):
    for row in range(len(boxes[0])):
        for column in range(len(boxes)):
            print(boxes[column][row].get_coord(),sep=' ',end='',flush=True),
        print("")

def print_table(table):
    for row in range(len(table)):
        for col in range(len(table[0])):
            print("{0}{1}{2}{3}".format("  ",table[row][col],"  ","|"),end='',flush=True),
        print("",flush=True)
        for col in range(len(table[0])):
            print("-----+",sep='',end='',flush=True),
        print("",flush=True)
