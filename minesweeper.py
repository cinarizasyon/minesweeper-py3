import constants
import random
import util
from box import box


class minesweeper:
    def __init__(self, level_no):
        self.level = self.__get_level(level_no)
        self.set_boxes(
            self.generate_boxes(self.level.row_count, self.level.column_count)
        )
        self.select_box(0, 0)
        self.__mines = []

    def get_boxes(self):
        return self.boxes

    def set_boxes(self, boxes):
        self.boxes = boxes

    def generate_boxes(self, row, column):
        boxes = []
        for row in range(row):
            for col in range(column):
                boxes.append(box(row, col))
        return boxes

    def generate_random_mines(self):
        self.__mines = random.sample(self.boxes, self.level.mine_count)
        for mine in self.__mines:
            mine.set_as_mine()

    def toggle_flag(self, xCoord, yCoord, flag_count):
        box = self.__get_box(xCoord, yCoord)
        result = None
        if box is not None and box.get_state() is False:
            next_flag_state = not (box.get_is_flagged())
            if next_flag_state is True:
                if flag_count < self.level.mine_count:
                    box.set_is_flagged(next_flag_state)
                    result = True
            else:
                box.set_is_flagged(next_flag_state)
                result = False
            self.__set_box(xCoord, yCoord, box)
        return result

    def select_box(self, xCoord, yCoord):
        box = self.__get_box(xCoord, yCoord)
        if box is not None:
            box.set_is_selected(True)

    def unselect_box(self, xCoord, yCoord):
        box = self.__get_box(xCoord, yCoord)
        if box is not None:
            box.set_is_selected(False)

    def open_box(self, xCoord, yCoord):
        box = self.__get_box(xCoord, yCoord)
        game_over = False
        if box is not None and box.get_is_flagged() is False:
            if box.get_is_mine():
                self.show_mines()
                self.lock_boxes()
                game_over = True
            else:
                if self.show_box(box) == 0:
                    self.show_neighbors(box.get_xCoord(), box.get_yCoord())
                self.__set_box(xCoord, yCoord, box)
                game_over = False
        return game_over

    def show_mines(self):
        for mine in self.__mines:
            if mine.get_is_flagged() is False:
                mine.set_state(True)
                mine.set_tag("M")
                self.__set_box(mine.get_xCoord(), mine.get_yCoord(), mine)

    def show_neighbors(self, xCoord, yCoord):
        neighbors = util.get_neighboord(
            xCoord, yCoord, self.level.row_count, self.level.column_count
        )
        for neighbor in neighbors:
            box = self.__get_box(neighbor[0], neighbor[1])
            self.show_box(box)
            self.__set_box(xCoord, yCoord, box)

    def show_box(self, box):
        box.set_state(True)
        mine_count = self.get_mine_count_in_neighboord(
            box.get_xCoord(), box.get_yCoord()
        )
        if mine_count > 0:
            box.set_tag(str(mine_count) + ":o")
        else:
            box.set_tag("C:o")
        return mine_count

    def lock_boxes(self):
        for box in self.boxes:
            if (
                box.get_is_mine() is False and
                box.get_is_flagged() is False and
                box.get_tag() == ""
            ):
                box.set_state(True)
                box.set_tag(" :o")
                self.__set_box(box.get_xCoord(), box.get_yCoord(), box)

    def get_mine_count_in_neighboord(self, xCoord, yCoord):
        boxes_matrix = list(util.split_list(
            self.boxes, self.level.column_count))
        neighboord = util.get_neighboord(
            xCoord, yCoord, len(boxes_matrix), len(boxes_matrix[0])
        )
        mine_count = 0
        for neighbor in neighboord:
            box = self.__get_box(neighbor[0], neighbor[1])
            if box is not None and box.get_is_mine():
                mine_count += 1
        return mine_count

    def __get_level(self, no):
        result = None
        for level in constants.levels:
            if level.no == no:
                result = level
        return result

    def __get_box(self, xCoord, yCoord):
        result = None
        for box in self.boxes:
            if box.get_xCoord() == xCoord and box.get_yCoord() == yCoord:
                result = box
        return result

    def __set_box(self, xCoord, yCoord, box):
        for box in self.boxes:
            if box.get_xCoord() == xCoord and box.get_yCoord() == yCoord:
                box = box
