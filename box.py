class box:
    def __init__(self, xCoord, yCoord):
        self.__is_flagged = False
        self.__is_mine = False
        self.__xCoord = xCoord
        self.__yCoord = yCoord

    def get_is_flagged(self):
        return self.__is_flagged

    def get_is_mine(self):
        return self.__is_mine

    def get_xCoord(self):
        return self.__xCoord

    def get_yCoord(self):
        return self.__yCoord

    def set_is_flagged(self, flag):
        self.__is_flagged = flag

    def set_as_mine(self):
        self.__is_mine = True

    def set_xCoord(self, xCoord):
        self.__xCoord = xCoord

    def set_yCoord(self, yCoord):
        self.__yCoord = yCoord

    def get_coord(self):
        return "({0},{1})".format(self.get_xCoord(), self.get_yCoord())
