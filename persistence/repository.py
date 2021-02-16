
class ButtonsRepository():

    def __init__(self):
        self.__buttons = []

    def addButton(self, button):
        self.__buttons.append(button)

    def getAllButtons(self):
        return self.__buttons

    def deleteButton(self, button):
        new_data = []
        for btn in self.__buttons:
            if btn.getName() != button.getName():
                new_data.append(btn)

        self.__buttons = new_data
