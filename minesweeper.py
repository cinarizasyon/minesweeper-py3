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

    def toggle_flag(self,xCoord,yCoord):
        box = self.__get_box(xCoord,yCoord)
        if box is not None:
            box.set_is_flagged(not(box.get_is_flagged))

    def select_box(self,xCoord,yCoord):
        box = self.__get_box(xCoord,yCoord)
        if box is not None:
            box.set_is_selected(True)
    
    def unselect_box(self,xCoord,yCoord):
        box = self.__get_box(xCoord,yCoord)
        if box is not None:
            box.set_is_selected(False)

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

