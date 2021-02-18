from domain.valueObject import Button, Wall, Road, Arrow
from domain.entity import Alien

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
        :param level: level of game, 0 represent the actual world
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

    def createStartRoad(self, image, x, y, width, height):
        """
        create a start road object and transmit it to repository for adding
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        road = Road(image, x, y, width, height)
        self.__world_repository.addStartRoad(road)

    def createArrow(self, image, x, y, width, height, direction):
        """
        create a arrow object and transmit it to repository for adding
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :param direction:
        :return:
        """
        arrow = Arrow(image, x, y, width, height, direction)
        self.__world_repository.addArrow(arrow)

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

    def getAllStartRoads(self):
        """
        collect all start road objects and transmit it to UI
        :return: list of road objects
        """
        return self.__world_repository.getAllStartRoads()

    def getAllArrows(self):
        """
        collect all arrow objects and transmit it to UI
        :return: list of road objects
        """
        return self.__world_repository.getAllArrows()

class EnemyService():

    def __init__(self, enemy_repository):
        self.__enemy_repository = enemy_repository

    def getAliensCount(self, level):
        """
        :param level: level of game, 0 represent the actual world
        :return: number of initial aliens
        """
        return self.__enemy_repository.getAliensCount(level)

    def createAliens(self, aliens_count, start_road, alien_image, alien_size, alien_power, center):
        """
        create alien objects and transmit every alien to repository for adding
        :param aliens_count:
        :param start_road:
        :param alien_image:
        :param alien_size:
        :param alien_power:
        :param center:
        :return:
        """
        #id, image, x, y, width, height, power, life
        width = alien_size
        height = alien_size
        x = alien_size
        road_count = 0
        for i in range(1, aliens_count + 1):
            if road_count >= len(start_road):
                road_count = 0
            road = start_road[road_count]
            road_count += 1

            alien = Alien(i, alien_image, -alien_size*((i-1)//3), road.getY() + center, width, height, alien_power)
            self.__enemy_repository.addAlien(alien)

    def getAllAliens(self):
        """
        collect aliens and transmit it to UI or to other functions in service
        :return: list of aliens objects
        """
        return self.__enemy_repository.getAllAliens()

    def updateAliens(self, arrows):
        """
        pass
        :param arrows: list of arrow objects
        :return:
        """
        aliens = self.__enemy_repository.getAllAliens()
        for alien in aliens:
            alien_x = alien.getX()
            alien_y = alien.getY()
            alien_size = alien.getWidth()

            #change direction
            pos_changed = False
            for arrow in arrows:
                arrow_x = arrow.getX()
                arrow_y = arrow.getY()
                arrow_width = arrow.getWidth()
                arrow_height = arrow.getHeight()
                #move up
                if arrow_x  <= alien_x  <= arrow_x + arrow_width // 5 :
                    if arrow_y  <= alien_y  <= arrow_y + arrow_height // 5:
                        direction = arrow.getDirection()
                        alien_direction = alien.getDirection()
                        if alien_direction == "right":
                            alien_x += 2
                            alien.setX(alien_x)
                        if alien_direction == "left":
                            alien_x -= 2
                            alien.setX(alien_x)
                        if alien_direction == "up":
                            alien_y -= 2
                            alien.setY(alien_y)
                        if alien_direction == "down":
                            alien_y += 2
                            alien.setY(alien_y)
                        alien.setDirection(direction)

                #move right


            if alien.getDirection() == "right":
                alien.setX(alien_x + 1)
            elif alien.getDirection() == "up":
                alien.setY(alien_y - 1)
            elif alien.getDirection() == "down":
                alien.setY(alien_y + 1)

            #self.__enemy_repository.updateAlien(alien)








