class WorldRepository():

    def __init__(self):
        self.__world_data = []
        self.__wall = []
        self.__road = []
        self.__start_road = []
        self.__arrow = []
        self.__war_zone = []
        self.__warrior_zone = None

    def __read_all(self, level):
        filename = "levels/level" + str(level) + ".txt"
        with open(filename, "r") as f:
            lines = f.readlines()
            self.__world_data = []
            self.__wall = []
            for line in lines:
                line.strip()
                if line != "":
                    world_data_line = []
                    parts = line.split(" ")
                    for part in parts:
                        world_data_line.append(int(part))
                    self.__world_data.append(world_data_line)

    def getInitWorldData(self, level):
        self.__read_all(level)
        return self.__world_data

    def getWorldData(self):
        return self.__world_data

    def addWall(self, wall):
        self.__wall.append(wall)

    def getAllWalls(self):
        return self.__wall

    def addRoad(self, road):
        self.__road.append(road)

    def getAllRoads(self):
        return self.__road

    def addStartRoad(self, road):
        self.__start_road.append(road)

    def getAllStartRoads(self):
        return self.__start_road

    def addArrow(self, arrow):
        self.__arrow.append(arrow)

    def getAllArrows(self):
        return self.__arrow

    def addWarZone(self, war_zone):
        self.__war_zone.append(war_zone)

    def getAllWarZones(self):
        return self.__war_zone

    def addWarriorZone(self, zone):
        self.__warrior_zone = zone

    def getWarriorZone(self):
        return self.__warrior_zone


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


class EnemyRepository():

    def __init__(self):
        self.__aliens = []
        self.__aliens_count = 0

    def __read_all(self, level):
        filename = "levels/level" + str(level) + "_enemies.txt"
        with open(filename, "r") as f:
            lines = f.readlines()
            self.__aliens_count = 0
            for line in lines:
                line.strip()
                if line != "":
                    parts = line.split(",")
                    if parts[0] == "alien":
                        self.__aliens_count = int(parts[1])

    def getAliensCount(self, level):
        self.__read_all(level)
        return self.__aliens_count

    def getAllAliens(self):
        return self.__aliens

    def addAlien(self, alien):
        self.__aliens.append(alien)

    def deleteAlien(self, alien):
        new_data = []
        for aln in self.__aliens:
            if aln.getId() != alien.getId():
                new_data.append(aln)

        self.__aliens = new_data

    def updateAlien(self, alien):
        new_data = []
        for aln in self.__aliens:
            if aln.getId() == alien.getId():
                new_data.append(alien)
            else:
                new_data.append(aln)

        self.__aliens = new_data


class WarriorRepository():

    def __init__(self):
        self.__archers = []
        self.__archers_count = 0

    def __read_all(self, level):
        filename = "levels/level" + str(level) + "_warriors.txt"
        with open(filename, "r") as f:
            lines = f.readlines()
            self.__archers_count = 0
            for line in lines:
                line.strip()
                if line != "":
                    parts = line.split(",")
                    if parts[0] == "archer":
                        self.__archers_count = int(parts[1])

    def getArchersInitCount(self, level):
        self.__read_all(level)
        return self.__archers_count

    def getArchersCount(self):
        return self.__archers_count

    def setArchersCount(self, value):
        self.__archers_count = value

    def getAllArchers(self):
        return self.__archers

    def addArcher(self, archer):
        self.__archers.append(archer)

    def deleteArcher(self, archers):
        new_data = []
        for arc in self.__archers:
            if arc.getId() != archers.getId():
                new_data.append(arc)

        self.__archers = new_data

    def updateArcher(self, archer):
        new_data = []
        for arc in self.__archers:
            if arc.getId() == archer.getId():
                new_data.append(archer)
            else:
                new_data.append(arc)

        self.__archers = new_data



