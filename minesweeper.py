import constants
import random
from box import box
class minesweeper:

    def __init__(self,level_no):
        self.level = self.__get_level(level_no)
        self.set_boxes(self.generate_boxes(self.level.row_count,self.level.column_count))
        self.select_box(0,0)

    def get_boxes(self):
        return self.boxes

    def set_boxes(self,boxes):
        self.boxes = boxes

    def generate_boxes(self,row,column):
        boxes = []
        for row in range(row):
            for col in range(column):
                boxes.append(box(row,col))
        return boxes

    def generate_random_mines(self):
        mines = random.sample(self.boxes,self.level.mine_count)
        for mine in mines:
            mine.set_as_mine()

    def toggle_flag(self,xCoord,yCoord, flag_count):
        box = self.__get_box(xCoord,yCoord)
        result = None
        if box is not None:
            next_flag_state = not(box.get_is_flagged())
            if next_flag_state == True:
                if flag_count < self.level.mine_count:
                    box.set_is_flagged(next_flag_state)
                    result = True
            else:
                box.set_is_flagged(next_flag_state)
                result = False
            self.__set_box(xCoord,yCoord,box)
        return result

    def select_box(self,xCoord,yCoord):
        box = self.__get_box(xCoord,yCoord)
        if box is not None:
            box.set_is_selected(True)
    
    def unselect_box(self,xCoord,yCoord):
        box = self.__get_box(xCoord,yCoord)
        if box is not None:
            box.set_is_selected(False)

    def open_box(self,xCoord,yCoord):
        box = self.__get_box(xCoord,yCoord)

        if box is not None:
            box.set_state(True)
            if box.get_is_mine():
                box.set_tag("M")
            else:
                box.set_tag("O")
            self.__set_box(xCoord,yCoord,box)
        return box.get_state()

    def __get_level(self,no):
        result = None
        for level in constants.levels:
            if level.no == no:
                result = level
        return result

    def __get_box(self,xCoord,yCoord):
        result = None
        for box in self.boxes:
            if box.get_xCoord() == xCoord and box.get_yCoord() == yCoord:
                result = box
        return result

    def __set_box(self,xCoord,yCoord,box):
        for box in self.boxes:
            if box.get_xCoord() == xCoord and box.get_yCoord() == yCoord:
                box = box

