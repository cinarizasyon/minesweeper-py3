import os
import util

def show(boxes, level):
    os.system("cls")
    table=convert_to_table(boxes,level)
    util.print_table(table)

def convert_to_table(boxes,level):
        table = []
        table_header = [" "]
        for x in range(1,level.column_count+1):
                table_header.append(str(x))
        table.append(table_header)
        boxes_matrix = list(util.split_list(boxes,level.row_count))
       
        for row in range(len(boxes_matrix)):
                row_data=[str(row + 1)]
                for col in range(len(boxes_matrix[0])):
                        row_data.append(box_text(boxes_matrix[row][col]))
                table.append(row_data)
        return table

def box_text(box):
        text= " "
        if box.get_is_flagged():
                text = "F"
        if box.get_is_selected():
                text += ":s"
        return text


        

            

