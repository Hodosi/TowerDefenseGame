from domain.entity import Alien

class EnemyService():

    def __init__(self, enemy_repository):
        self.__enemy_repository = enemy_repository

    def getEnemiesCount(self, name, level):
        """
        determine count of enemies by name
        :param name: name of enemy
        :param level: level of game
        :return: number of initial enemies
        """
        if name == "alien":
            return self.__enemy_repository.getAliensCount(level)

    def createEnemies(self, name, count, start_road, image, width, height, power, center):
        """
        create enemy objects and transmit every enemy to repository for adding
        :param name: name of enemy
        :param count: number of enemies
        :param start_road: list of starting roads for enemies
        :param image: image of enemies
        :param width: width of enemies
        :param height: height of enemies
        :param power: power of enemies
        :param center:difference between object.x and enemy.x position
        :return:
        """
        number_of_start_roads = len(start_road)
        road_count = 0
        for i in range(1, count + 1):
            if road_count >= number_of_start_roads:
                road_count = 0
            road = start_road[road_count]
            road_count += 1

            if name == "alien":
                x = -width*((i-1)//number_of_start_roads)
                y = road.getY() + center
                alien = Alien(i, image, x, y, width, height, power)
                self.__enemy_repository.addAlien(alien)

    def getAllEnemies(self, name):
        """
        collect enemies by name and transmit it to UI or to other functions in service
        :param name: name of enemies
        :return: list of enemy objects
        """
        if name == "alien":
            return self.__enemy_repository.getAllAliens()

    def updateEnemies(self, enemies, arrows):
        """
        pass
        :param enemies:
        :param arrows:
        :return:
        """
        for enemy in enemies:
            enemy_x = enemy.getX()
            enemy_y = enemy.getY()

            # change direction
            for arrow in arrows:
                arrow_x = arrow.getX()
                arrow_y = arrow.getY()
                arrow_width = arrow.getWidth()
                arrow_height = arrow.getHeight()
                if arrow_x <= enemy_x <= arrow_x + arrow_width // 5:
                    if arrow_y <= enemy_y <= arrow_y + arrow_height // 5:
                        direction = arrow.getDirection()
                        enemy_direction = enemy.getDirection()
                        if enemy_direction == "right":
                            enemy_x += 2
                            enemy.setX(enemy_x)
                        if enemy_direction == "left":
                            enemy_x -= 2
                            enemy.setX(enemy_x)
                        if enemy_direction == "up":
                            enemy_y -= 2
                            enemy.setY(enemy_y)
                        if enemy_direction == "down":
                            enemy_y += 2
                            enemy.setY(enemy_y)
                        enemy.setDirection(direction)

            if enemy.getDirection() == "right":
                enemy.setX(enemy_x + 1)
            elif enemy.getDirection() == "up":
                enemy.setY(enemy_y - 1)
            elif enemy.getDirection() == "down":
                enemy.setY(enemy_y + 1)
