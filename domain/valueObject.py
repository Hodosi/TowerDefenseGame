class Button():

    def __init__(self, name, type, image, x, y):
        self.__name = name
        self.__type = type
        self.__image = image
        self.__x = x
        self.__y = y
        self.__clicked = False

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getImage(self):
        return self.__image

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getClickedStatus(self):
        return self.__clicked

    def setClickedStatus(self, value):
        self.__clicked = value


