import util

boxes = util.generate_boxes(8,8)
neighbor_boxes = util.get_neighboord(0,0,boxes)
util.print_boxes(boxes)
util.print_matrix(neighbor_boxes)