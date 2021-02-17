from domain.valueObject import Button, Wall, Road

class ButtonService():
    def __init__(self, buttons_repository):
        self.__buttons_repository = buttons_repository

    def createButton(self, name, type, image, x, y, width, height):
        """
        create a button object and transmit to repository for adding
        :param name:
        :param type:
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        button = Button(name, type, image, x, y, width, height)
        self.__buttons_repository.addButton(button)

    def getButtonsByType(self, type):
        """
        collect buttons and transmit it to UI or to other functions in service
        :param type: type of button
        :return: list of button objects which has the type
        """
        type_buttons = []
        all_buttons = self.__buttons_repository.getAllButtons()

        for button in all_buttons:
            if button.getType() == type:
                type_buttons.append(button)

        return type_buttons

    def getButtonByName(self, name):
        """
        collect button and transmit it to UI
        :param name: name of button
        :return: object button which has the name
        """
        all_buttons = self.__buttons_repository.getAllButtons()

        for button in all_buttons:
            if button.getName() == name:
                return button


    def deleteButtonByName(self, name):
        """
        find a button by name and transmit it for repository for deletion
        :param name: name of button
        :return:
        """
        all_buttons = self.__buttons_repository.getAllButtons()

        for button in all_buttons:
            if button.getName() == name:
                self.__buttons_repository.deleteButton(button)


    def buttonCollision(self, type, x, y):
        """
        determines the collision between type buttons and a position (x, y)
        :param type:
        :param x:
        :param y:
        :return: collided button object
        """
        buttons = self.getButtonsByType(type)
        for button in buttons:
            if button.getClickedStatus() == False:
                button_x = button.getX()
                button_y = button.getY()
                button_width = button.getWidth()
                button_height = button.getHeight()
                if button_x <= x <= button_x + button_width:
                    if button_y <= y <= button_y + button_height:
                        button.setClickedStatus(True)
                        return button
        return None

    def changeClickedStatus(self, type, value):
        """
        change every type button clicked status to value
        :param type:
        :param value:
        :return:
        """
        buttons = self.getButtonsByType(type)
        for button in buttons:
            button.setClickedStatus(value)


class WorldService():
    def __init__(self, world_repository):
        self.__world_repository = world_repository

    def getWorldData(self, level):
        """
        load world data for a level and transmit it to UI
        :param level: level of game
        :return: matrix of world data
        """
        if level > 0:
            return self.__world_repository.getInitWorldData(level)
        else:
            return self.__world_repository.getWorldData()

    def createWall(self, image, x, y, width, height):
        """
        create a wall object and transmit it to repository for adding
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        wall = Wall(image, x, y, width, height)
        self.__world_repository.addWall(wall)

    def createRoad(self, image, x, y, width, height):
        """
        create a road object and transmit it to repository for adding
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        road = Road(image, x, y, width, height)
        self.__world_repository.addRoad(road)

    def getAllWalls(self):
        """
        collect all wall objects and transmit it to UI
        :return: list of wall objects
        """
        return self.__world_repository.getAllWalls()

    def getAllRoads(self):
        """
        collect all road objects and transmit it to UI
        :return: list of road objects
        """
        return self.__world_repository.getAllRoads()


