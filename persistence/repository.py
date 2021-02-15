
class ButtonsRepository():

    def __init__(self):
        self.__buttons = []

    def addButton(self, button):
        self.__buttons.append(button)

    def getAllButtons(self):
        return self.__buttons
