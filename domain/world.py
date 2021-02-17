class World():

    def __init__(self):
        self.__object_size = None
        self.__start_y = None
        self.__level = 1

    def getObjectSize(self):
        return self.__object_size

    def getStartY(self):
        return self.__start_y

    def getLevel(self):
        return self.__level

    def setObjectSize(self, value):
        self.__object_size = value

    def setStartY(self, value):
        self.__start_y = value

    def setLevel(self, value):
        self.__level = value