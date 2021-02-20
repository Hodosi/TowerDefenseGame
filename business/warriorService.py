from domain.entity import Archer

class WarriorService():

    def __init__(self, warrior_repository):
        self.__warrior_repository = warrior_repository

    def getWarriorsCount(self, name):
        """
        determine count of current warriors by name
        :param name: name of warriors
        :return: number of warriors
        """
        if name == "archer":
            return self.__warrior_repository.getArchersCount()

    def getWarriorsInitCount(self, name, level):
        """
        determine count of initial warriors by name
        :param name: name of warriors
        :param level: number of warriors
        :return: number of warriors
        """
        if name == "archer":
            return self.__warrior_repository.getArchersInitCount(level)

    def createWarrior(self, id, name, image, x, y, width, height, power):
        """
        pass
        :param id:
        :param name:
        :param image:
        :param x:
        :param y:
        :param width:
        :param height:
        :param power:
        :return:
        """
        if id == 0:
            up = False
            down = False
            right = False
            left = False
        else:
            pass

        if name == "archer":
            archer = Archer(id, image, x, y, width, height, power, up, down, right, left)
            self.__warrior_repository.addArcher(archer)

    def getAllWarriors(self, name):
        """
        collect warriors by name and transmit it to UI or to other functions in service
        :param name: name of warriors
        :return: list of warrior objects
        """
        if name == "archer":
            return self.__warrior_repository.getAllArchers()

    def changeClickedStatus(self, warriors, warrior_zone, war_zones, value):
        """
        change every warriors, war zone and warrior zone clicked status to value
        :param warriors: list of warrior objects
        :param warrior_zone: object
        :param war_zones: list of war zone objects
        :param value:
        :return:
        """
        for warrior in warriors:
            warrior.setClikcedStatus(value)

        for war_zone in war_zones:
            war_zone.setClickedStatus(value)

        warrior_zone.setClickedStatus(value)

    def updateWarriorZone(self, warrior_zone, name, x, y):
        """
        pass
        :param warrior_zone:
        :param name:
        :param x:
        :param y:
        :return:
        """
        # warrior zone
        zone_x = warrior_zone.getX()
        zone_y = warrior_zone.getY()
        zone_width = warrior_zone.getWidth()
        zone_height = warrior_zone.getHeight()

        if zone_x <= x <= zone_x + zone_width:
            if zone_y <= y <= zone_y + zone_height:
                current_warrior = warrior_zone.getWarrior()
                if current_warrior != None and warrior_zone.getClickedStatus() == False:
                    if current_warrior.getName() == name:
                        if name == "archer":
                            count = self.__warrior_repository.getArchersCount()
                            count += 1
                            self.__warrior_repository.setArchersCount(count)
                            warrior_zone.setImage(None)
                            warrior_zone.setWarrior(None)
                            warrior_zone.setClickedStatus(True)

    def updateWarZone(self, war_zones, warrior_zone, x, y):
        """
        pass
        :param war_zones:
        :param warrior_zone:
        :param x:
        :param y:
        :return:
        """
        # war zone
        for war_zone in war_zones:
            zone_x = war_zone.getX()
            zone_y = war_zone.getY()
            zone_width = war_zone.getWidth()
            zone_height = war_zone.getHeight()

            if zone_x <= x <= zone_x + zone_width:
                if zone_y <= y <= zone_y + zone_height:
                    current_warrior = warrior_zone.getWarrior()
                    war_zone_warrior = war_zone.getWarrior()
                    if war_zone_warrior != None and war_zone.getClickedStatus() == False:
                        if war_zone_warrior.getName() == "archer":
                            count = self.__warrior_repository.getArchersCount()
                            count += 1
                            self.__warrior_repository.setArchersCount(count)
                            war_zone.setImage(None)
                            war_zone.setWarrior(None)

                    if current_warrior != None and war_zone.getClickedStatus() == False:
                        war_zone.setWarrior(current_warrior)
                        war_zone.setImage(warrior_zone.getImage())
                        warrior_zone.setWarrior(None)
                        warrior_zone.setImage(None)
                        war_zone.setClickedStatus(True)

    def updateWarriors(self, warriors, warrior_zone, x, y):
        """
        pass
        :param warriors:
        :param warrior_zone:
        :param x:
        :param y:
        :return:
        """
        # warriors
        for warrior in warriors:
            if warrior.getClikcedStatus() == True:
                continue
            warrior_x = warrior.getX()
            warrior_y = warrior.getY()
            warrior_width = warrior.getWidth()
            warrior_height = warrior.getHeight()
            if warrior_x <= x <= warrior_x + warrior_width:
                if warrior_y <= y <= warrior_y + warrior_height:
                    # main warrior
                    id = warrior.getId()
                    if id == 0:
                        if warrior.getName() == "archer":
                            count = self.__warrior_repository.getArchersCount()
                            if count > 0:
                                current_warrior = warrior_zone.getWarrior()
                                if current_warrior == None:
                                    count -= 1
                                    self.__warrior_repository.setArchersCount(count)
                                    warrior_zone.setImage(warrior.getImage())
                                    warrior_zone.setWarrior(warrior)
                                    warrior.setClikcedStatus(True)
                                    return warrior
                                elif current_warrior.getName() != warrior.getName():
                                    pass
