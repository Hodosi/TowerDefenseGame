class Screen():

    def __init__(self):
        self.__display = None
        self.__background_image = None
        self.__width = None
        self.__height = None
        self.__color = (0, 0, 0)
        self.__minimized = False

    def getDisplay(self):
        return self.__display

    def getBackgroundImage(self):
        return self.__background_image

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getColor(self):
        return self.__color

    def getMinimizedStatus(self):
        return self.__minimized

    def setDisplay(self, value):
        self.__display = value

    def setBackgroundImage(self, value):
        self.__background_image = value

    def setWidth(self, value):
        self.__width = value

    def setHeight(self, value):
        self.__height = value

    def setColor(self, value):
        self.__color = value

    def setMinimizedStatus(self, value):
        self.__minimized = value