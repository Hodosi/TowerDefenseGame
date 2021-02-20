class ValueObject():

    def __init__(self, image, x, y, width, height):
        self.__image = image
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

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


class Button(ValueObject):

    def __init__(self, name, type, image, x, y, width, height):
        ValueObject.__init__(self, image, x, y, width, height)
        self.__name = name
        self.__type = type
        self.__clicked = False

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def getClickedStatus(self):
        return self.__clicked

    def setClickedStatus(self, value):
        self.__clicked = value


class Wall(ValueObject):

    def __init__(self, image, x, y, width, height):
        ValueObject.__init__(self, image, x, y, width, height)


class Road(ValueObject):

    def __init__(self, image, x, y, width, height):
        ValueObject.__init__(self, image, x, y, width, height)


class Arrow(ValueObject):

    def __init__(self, image, x, y, width, height, direction):
        ValueObject.__init__(self, image, x, y, width, height)
        self.__direction = direction

    def getDirection(self):
        return self.__direction


class WarZoneObject(ValueObject):
    def __init__(self, image, x, y, width, height):
        ValueObject.__init__(self, image, x, y, width, height)
        self.__zone_image = image
        self.__image = image
        self.__warrior = None
        self.__clicked = False

    def getImage(self):
        return self.__image

    def setImage(self, image):
        if image == None:
            self.__image = self.__zone_image
        else:
            self.__image = image

    def getWarrior(self):
        return self.__warrior

    def setWarrior(self, value):
        self.__warrior = value

    def getClickedStatus(self):
        return self.__clicked

    def setClickedStatus(self, value):
        self.__clicked = value


class WarZone(WarZoneObject):

    def __init__(self, image, x, y, width, height):
        WarZoneObject.__init__(self, image, x, y, width, height)


class WarriorZone(WarZoneObject):

    def __init__(self, image, x, y, width, height):
        WarZoneObject.__init__(self, image, x, y, width, height)


