
class GameService():

    def __init__(self, buttons_repository):
        self.__buttons_repository = buttons_repository

    def addButton(self, button):
        self.__buttons_repository.addButton(button)

    def getButtonsByType(self, type):
        type_buttons = []
        all_buttons = self.__buttons_repository.getAllButtons()

        for button in all_buttons:
            if button.getType() == type:
                type_buttons.append(button)

        return type_buttons

    def getButtonByName(self, name):
        all_buttons = self.__buttons_repository.getAllButtons()

        for button in all_buttons:
            if button.getName() == name:
                return button


    def deleteButtonByName(self, name):
        all_buttons = self.__buttons_repository.getAllButtons()

        for button in all_buttons:
            if button.getName() == name:
                self.__buttons_repository.deleteButton(button)




