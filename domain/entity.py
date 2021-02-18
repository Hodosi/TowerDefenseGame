class Enemy():

    def __init__(self, id, image, x, y, width, height, power):
        self.__id = id
        self.__image = image
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__power = power
        self.__life = 100
        self.__direction = "right"

    def getId(self):
        return self.__id

    def getImage(self):
        return self.__image

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getPower(self):
        return  self.__power

    def getLife(self):
        return self.__life

    def getDirection(self):
        return self.__direction

    def setX(self, value):
        self.__x = value

    def setY(self, value):
        self.__y = value

    def setLife(self, value):
        self.__life = value

    def setDirection(self, value):
        self.__direction = value



class Alien(Enemy):

    def __init__(self, id, image, x, y, width, height, power):
        Enemy.__init__(self, id,  image, x, y, width, height, power)