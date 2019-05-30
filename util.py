from box import box
def get_neighboord(xCoord, yCoord, matrix):
    test_seperation = [
        [xCoord-1, yCoord+1], [xCoord, yCoord+1], [xCoord+1, yCoord+1],
        [xCoord-1, yCoord], [xCoord+1, yCoord],
        [xCoord-1, yCoord-1], [xCoord, yCoord-1], [xCoord+1, yCoord-1],
    ]
    neighbors = []

    for seperation in test_seperation:
        if(is_valid_seperation(seperation[0], seperation[1], matrix)):
            neighbors.append(seperation)

    return neighbors


def is_valid_seperation(currX, currY, matrix):
    return currX >= 0 and currY >= 0 and currX < len(matrix) and currY < len(matrix[0])

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

def generate_boxes(row,column):
    boxes = []
    for row in range(row):
        rowArray=[]
        for col in range(column):
            rowArray.append(box(row,col))
        boxes.append(rowArray)
    return boxes
