
class GameService():

    def __init__(self, buttons_repository, world_repository):
        self.__buttons_repository = buttons_repository
        self.__world_repository = world_repository

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

    def getWorldData(self, level):
        if level > 0:
            return self.__world_repository.getInitWorldData(level)
        else:
            return self.__world_repository.getWorldData()

    def addWall(self, wall):
        self.__world_repository.addWall(wall)

    def addRoad(self, road):
        self.__world_repository.addRoad(road)

    def getAllWalls(self):
        return self.__world_repository.getAllWalls()

    def getAllRoads(self):
        return self.__world_repository.getAllRoads()


