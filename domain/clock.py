class Clock():

    def __init__(self):
        self.__time = None
        self.__framerate = None

    def getTime(self):
        return self.__time

    def getFramerate(self):
        return self.__framerate

    def setTime(self, value):
        self.__time = value

    def setFramerate(self, value):
        self.__framerate = value
