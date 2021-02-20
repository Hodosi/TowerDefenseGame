import pygame
from pygame.locals import *
from pygame import mixer
from domain.screen import Screen
from domain.world import World
from domain.clock import Clock

class UI():

    def __init__(self, button_service, world_service, enemy_service, warrior_service):
        self.__button_service = button_service
        self.__world_service = world_service
        self.__enemy_service = enemy_service
        self.__warrior_service = warrior_service
        self.__screen = Screen()
        self.__world = World()
        self.__clock = Clock()
        self.__setPygame()
        self.__setClock()
        self.__setScreen()
        self.__setButtons()
        self.__initWorldSize()
        self.__setWorld()
        self.__setEnemies()
        self.__setWarrios()

    def __percent(self, size, percent):
        """
        :param size: size of surface
        :param percent: percent of surface
        :return: percent of size as an integer
        """
        return int(size * percent / 100)

    def __setPygame(self):
        """
        initialize pygame
        :return:
        """
        pygame.init()
        mixer.init()

    def __setClock(self):
        """
        initialize display frame rate
        :return:
        """
        self.__clock.setTime(pygame.time.Clock())
        self.__clock.setFramerate(60)

    def __setScreen(self):
        """
        initialize start screen and background image
        :return:
        """
        self.__resetScreen()
        pygame.display.set_caption("Tower Defense Game")
        background_image = pygame.image.load("image/background.png")
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()
        background_image = pygame.transform.scale(background_image, (width, height))
        self.__screen.setBackgroundImage(background_image)

    def __resetScreen(self):
        """
        reinitialize start screen display mode, width and height
        :return:
        """
        monitor = pygame.display.Info()
        width = monitor.current_w
        height = monitor.current_h
        self.__screen.setWidth(width)
        self.__screen.setHeight(height)
        display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.__screen.setDisplay(display)

    def __initWorldSize(self):
        """
        initialize dimension of objects(squares) in world and start position of world
        :return:
        """
        monitor = pygame.display.Info()
        width = monitor.current_w
        size = width // 30
        self.__world.setObjectSize(size)
        height = self.__screen.getHeight()
        y_position = self.__percent(height, 5)
        self.__world.setStartY(y_position)

    def __setWorld(self):
        """
        initialize world data and create world objects
        :return:
        """
        level = self.__world.getLevel()
        world_data = self.__world_service.getInitWorldData(level)
        world_object_size = self.__world.getObjectSize()
        world_start_y = self.__world.getStartY()

        # load images
        wall_image = pygame.image.load("image/brick_wall.png")  # 1
        road_image = pygame.image.load("image/cracks.png")  # 2
        road_start_image = pygame.image.load("image/cracks_start.png")  # 3
        left_arrow = pygame.image.load("image/left_arrow.png")  # 4
        right_arrow = pygame.image.load("image/right_arrow.png")  # 5
        up_arrow = pygame.image.load("image/up_arrow.png")  # 6
        down_arrow = pygame.image.load("image/down_arrow.png")  # 7
        war_zone_image = pygame.image.load("image/swords.png")  # 8
        warrior_zone = pygame.image.load("image/shield.png")  # 9

        row_count = 0
        for line in world_data:
            col_count = 0
            y = row_count * world_object_size + world_start_y
            for value in line:
                x = col_count * world_object_size
                if value == 1:
                    image = pygame.transform.scale(wall_image, (world_object_size, world_object_size))
                    self.__world_service.createWall(image, x, y, world_object_size, world_object_size)
                if value == 2:
                    image = pygame.transform.scale(road_image, (world_object_size, world_object_size))
                    self.__world_service.createRoad(image, x, y, world_object_size, world_object_size)
                if value == 3:
                    image = pygame.transform.scale(road_start_image, (world_object_size, world_object_size))
                    self.__world_service.createStartRoad(image, x, y, world_object_size, world_object_size)
                if value == 4:
                    direction = "left"
                    image = pygame.transform.scale(left_arrow, (world_object_size, world_object_size))
                    self.__world_service.createArrow(image, x, y, world_object_size, world_object_size, direction)
                if value == 5:
                    direction = "right"
                    image = pygame.transform.scale(right_arrow, (world_object_size, world_object_size))
                    self.__world_service.createArrow(image, x, y, world_object_size, world_object_size, direction)
                if value == 6:
                    direction = "up"
                    image = pygame.transform.scale(up_arrow, (world_object_size, world_object_size))
                    self.__world_service.createArrow(image, x, y, world_object_size, world_object_size, direction)
                if value == 7:
                    direction = "down"
                    image = pygame.transform.scale(down_arrow, (world_object_size, world_object_size))
                    self.__world_service.createArrow(image, x, y, world_object_size, world_object_size, direction)
                if value == 8:
                    image = pygame.transform.scale(war_zone_image, (world_object_size, world_object_size))
                    self.__world_service.createWarZone(image, x, y, world_object_size, world_object_size)
                if value == 9:
                    image = pygame.transform.scale(warrior_zone, (world_object_size, world_object_size))
                    self.__world_service.createWarriorZone(image, x, y, world_object_size, world_object_size)

                col_count += 1
            row_count += 1

    def __drawWorld(self):
        """
        draw world objects on screen
        :return:
        """
        # get screen
        display = self.__screen.getDisplay()

        # draw walls
        walls = self.__world_service.getAllWalls()
        for wall in walls:
            display.blit(wall.getImage(), (wall.getX(), wall.getY()))

        # draw start roads
        roads = self.__world_service.getAllStartRoads()
        for road in roads:
            display.blit(road.getImage(), (road.getX(), road.getY()))

        # draw roads
        roads = self.__world_service.getAllRoads()
        for road in roads:
            display.blit(road.getImage(), (road.getX(), road.getY()))

        # draw arrows
        arrows = self.__world_service.getAllArrows()
        for arrow in arrows:
            display.blit(arrow.getImage(), (arrow.getX(), arrow.getY()))

        # draw war zones
        war_zones = self.__world_service.getAllWarZones()
        for war_zone in war_zones:
            display.blit(war_zone.getImage(), (war_zone.getX(), war_zone.getY()))

        # draw warrior zone
        warrior_zone = self.__world_service.getWarriorZone()
        display.blit(warrior_zone.getImage(), (warrior_zone.getX(), warrior_zone.getY()))
        rectangle = warrior_zone.getImage().get_rect()
        rectangle.x = warrior_zone.getX()
        rectangle.y = warrior_zone.getY()
        pygame.draw.rect(display, (255, 0, 0), rectangle, 5)

    def __drawGrid(self):
        """
        draw squares contour in world for visualization
        :return:
        """
        monitor = pygame.display.Info()
        self.__screen.setWidth(monitor.current_w)
        self.__screen.setHeight(monitor.current_h)

        width = self.__screen.getWidth()
        height = self.__screen.getHeight()
        display = self.__screen.getDisplay()

        world_object_size = self.__world.getObjectSize()
        world_start_y = self.__world.getStartY()

        # lines
        for i in range(0, 16):
            start_point = i * world_object_size + world_start_y
            pygame.draw.line(display, (255, 255, 255), (0, start_point), (width, start_point))

        #cols
        for i in range(0, 30):
            start_point = i * world_object_size
            pygame.draw.line(display, (255, 255, 255), (start_point, world_start_y), (start_point, height))

    def __setEnemies(self):
        """
        initialize enemies of game
        :return:
        """
        level = self.__world.getLevel()
        start_road = self.__world_service.getAllStartRoads()
        world_object_size = self.__world.getObjectSize()
        enemy_size = self.__percent(world_object_size, 80)
        width = enemy_size
        height = enemy_size
        center = self.__percent(world_object_size, 10)

        # aliens
        name = "alien"
        count = self.__enemy_service.getEnemiesCount(name, level)
        image = pygame.image.load("image/" + name + ".png")
        image = pygame.transform.scale(image, (width, height))
        power = 10
        self.__enemy_service.createEnemies(name, count, start_road, image, width, height, power, center)

    def __updateEnemies(self):
        """
        transmit arrows of game to service to update enemies position
        :return:
        """
        arrows = self.__world_service.getAllArrows()

        # aliens
        name = "alien"
        aliens = self.__enemy_service.getAllEnemies(name)
        self.__enemy_service.updateEnemies(aliens, arrows)

    def __drawEnemies(self):
        """
        draw enemies of game on screen
        :return:
        """
        # get screen
        display = self.__screen.getDisplay()

        # draw aliens
        aliens = self.__enemy_service.getAllEnemies("alien")
        for alien in aliens:
            display.blit(alien.getImage(), (alien.getX(), alien.getY()))

    def __setWarrios(self):
        """
        initialize warriors of game
        :return:
        """
        level = self.__world.getLevel()
        world_object_size = self.__world.getObjectSize()
        world_start_y = self.__world.getStartY()

        id = 0
        y = world_start_y
        width = world_object_size
        height = world_object_size

        # archers
        archers_count = self.__warrior_service.getWarriorsInitCount("archer", level)
        archers_image = pygame.image.load("image/archer.png")
        archers_image = pygame.transform.scale(archers_image, (world_object_size, world_object_size))
        x = 0
        archers_power = 4
        self.__warrior_service.createWarrior(id, "archer", archers_image, x, y, width, height, archers_power)

    def __updateWarriors(self):
        """
        update warriors, war zones and warrior zone of game
        :return:
        """
        war_zone = self.__world_service.getAllWarZones()
        warrior_zone = self.__world_service.getWarriorZone()
        archers = self.__warrior_service.getAllWarriors("archer")
        if pygame.mouse.get_pressed()[0] == 1:
            mouse_position = pygame.mouse.get_pos()
            mouse_x = mouse_position[0]
            mouse_y = mouse_position[1]
            # archers
            name = "archer"
            self.__warrior_service.updateWarriorZone(warrior_zone, name, mouse_x, mouse_y)
            self.__warrior_service.updateWarZone(war_zone, warrior_zone, mouse_x, mouse_y)
            self.__warrior_service.updateWarriors(archers, warrior_zone, mouse_x, mouse_y)

        if pygame.mouse.get_pressed()[0] == 0:
            # archers
            self.__warrior_service.changeClickedStatus(archers, warrior_zone, war_zone, False)

    def __drawWarriorsCount(self, count, x, y):
        """
        draw a number on screen
        :param count:
        :param x:
        :param y:
        :return:
        """
        world_object_size = self.__world.getObjectSize()
        size_of_text = self.__percent(world_object_size, 40)
        x += self.__percent(world_object_size, 50)
        y += self.__percent(world_object_size, 60)

        count = str(count)

        # get screen
        display = self.__screen.getDisplay()

        # draw text
        font = pygame.font.SysFont("Bauhaus 93", size_of_text)
        red = (255, 0, 0)
        black = (0, 0, 0)
        image = font.render(count, True, black)

        display.blit(image, (x, y))

    def __drawWarriors(self):
        """
        draw warriors of game
        :return:
        """
        # get screen
        display = self.__screen.getDisplay()

        # draw archers
        archers = self.__warrior_service.getAllWarriors("archer")
        for archer in archers:
            display.blit(archer.getImage(), (archer.getX(), archer.getY()))
            id = archer.getId()
            if id == 0:
                # draw warrior
                rectengle = archer.getImage().get_rect()
                rectengle.x = archer.getX()
                rectengle.y = archer.getY()
                pygame.draw.rect(display, (0, 255, 0), rectengle, 5)

                # draw count
                count = self.__warrior_service.getWarriorsCount("archer")
                self.__drawWarriorsCount(count, archer.getX(), archer.getY())

    def __setButtons(self):
        """
        initialize buttons of game
        :return:
        """
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()

        # exit button
        exit_image = pygame.image.load("image/exit.png")
        exit_button_x = width - self.__percent(width, 5)
        exit_button_y = 0
        exit_button_width = self.__percent(width, 5)
        exit_button_height = self.__percent(height, 5)
        exit_image = pygame.transform.scale(exit_image, (exit_button_width, exit_button_height))
        self.__button_service.createButton("exit", "common", exit_image, exit_button_x, exit_button_y, exit_button_width, exit_button_height)

        # minimize button
        minimize_image = pygame.image.load("image/minimize.png")
        minimize_button_x = width - 2 * self.__percent(width, 5) + 1*self.__percent(width, 1)
        minimize_button_y = self.__percent(height, 1)
        minimize_button_width = self.__percent(width, 4)
        minimize_button_height = self.__percent(height, 3)
        minimize_image = pygame.transform.scale(minimize_image, (minimize_button_width, minimize_button_height))
        self.__button_service.createButton("minimize", "common", minimize_image, minimize_button_x, minimize_button_y, minimize_button_width, minimize_button_height)

    def __set_maximize_button(self):
        """
        initialize maximize button of game
        :return:
        """
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()

        # maximize button
        maximize_image = pygame.image.load("image/maximize.png")
        maximize_button_x = 0
        maximize_button_y = 0
        maximize_button_width = width
        maximize_button_height = height
        maximize_image = pygame.transform.scale(maximize_image, (maximize_button_width, maximize_button_height))
        self.__button_service.createButton("maximize", "special", maximize_image, maximize_button_x, maximize_button_y, maximize_button_width, maximize_button_height)

    def __buttonEvent(self, button):
        """
        execute a button click
        :param button: clicked button
        :return: False if exit button was clicked, True otherwise
        """
        if button.getName() == "exit":
            return False

        if button.getName() == "maximize":
            self.__resetScreen()
            self.__button_service.deleteButtonByName("maximize")
            self.__screen.setMinimizedStatus(False)

        elif button.getName() == "minimize":
            monitor = pygame.display.Info()
            width = self.__percent(monitor.current_w, 10)
            height = self.__percent(monitor.current_h, 10)
            self.__screen.setWidth(width)
            self.__screen.setHeight(height)
            self.__screen.setDisplay(pygame.display.set_mode((width, height)))
            self.__set_maximize_button()
            self.__screen.setMinimizedStatus(True)
            maximize_button = self.__button_service.getButtonByName("maximize")
            maximize_button.setClickedStatus(True)

        return True

    def __checkButtonClickUI(self, type):
        """
        transmit clicked button, if it exists, to button event controller in UI
        :param type: type of buttons needs to check
        :return: False if exit button was clicked, True otherwise
        """
        button = None

        if pygame.mouse.get_pressed()[0] == 1:
            mouse_position = pygame.mouse.get_pos()
            mouse_x = mouse_position[0]
            mouse_y = mouse_position[1]
            button = self.__button_service.buttonCollision(type, mouse_x, mouse_y)
            if button != None:
                button.setClickedStatus(True)

        if pygame.mouse.get_pressed()[0] == 0:
            self.__button_service.changeClickedStatus(type, False)

        if button != None:
            run = self.__buttonEvent(button)
            if run == False:
                return False

    def __drawButtons(self, type):
        """
        draw buttons on screen
        :param type: type of buttons
        :return:
        """
        display = self.__screen.getDisplay()
        buttons = self.__button_service.getButtonsByType(type)

        for button in buttons:
            display.blit(button.getImage(), (button.getX(), button.getY()))

    def main_loop(self):
        """
        display the screen
        :return:
        """
        run = True
        while run:
            time = self.__clock.getTime()
            framerate = self.__clock.getFramerate()
            time.tick(framerate)

            # self.__screen.fill(self.__screen_color)

            display = self.__screen.getDisplay()
            display.blit(self.__screen.getBackgroundImage(), (0, 0))

            if self.__screen.getMinimizedStatus() == False:
                self.__drawWorld()
                self.__drawGrid()
                self.__updateWarriors()
                self.__updateEnemies()
                self.__drawWarriors()
                self.__drawEnemies()
                self.__drawButtons("common")
                if self.__checkButtonClickUI("common") == False:
                    run = False
                    break
            else:
                self.__drawButtons("special")
                self.__checkButtonClickUI("special")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            pygame.display.update()

        pygame.quit()
