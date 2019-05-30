from box import box
import util

test_matrix = []
for x in range(8):
    for y in range(8):
        test_matrix.append([x, y])

util.print_matrix(util.get_neighboord(5, 5, test_matrix))
