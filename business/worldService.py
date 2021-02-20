from domain.valueObject import Wall, Road, Arrow, WarZone, WarriorZone

class WorldService():

    def __init__(self, world_repository):
        self.__world_repository = world_repository

    def getInitWorldData(self, level):
        """
        load initial world data for a level and transmit it to UI
        :param level: level of game
        :return: matrix of world data
        """
        return self.__world_repository.getInitWorldData(level)

    def getWorldData(self):
        """
        load current world data for a level and transmit it to UI
        :return: matrix of world data
        """
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

    def createWarZone(self, image, x, y, width, height):
        """
        create a war_zone object and transmit it to repository for adding
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        war_zone = WarZone(image, x, y, width, height)
        self.__world_repository.addWarZone(war_zone)

    def createWarriorZone(self, image, x, y, width, height):
        """
        create a warrior_zone object and transmit it to repository for adding
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :return:
        """
        warrior_zone = WarriorZone(image, x, y, width, height)
        self.__world_repository.addWarriorZone(warrior_zone)

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

    def getAllWarZones(self):
        """
        collect all war zone objects and transmit it to UI
        :return: list of road objects
        """
        return self.__world_repository.getAllWarZones()

    def getWarriorZone(self):
        """
        collect warrior zone object and transmit it to UI
        :return: list of road objects
        """
        return self.__world_repository.getWarriorZone()
