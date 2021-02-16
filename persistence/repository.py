
class WorldRepository():

    def __init__(self):
        self.__world_data = []
        self.__wall = []
        self.__road = []

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
