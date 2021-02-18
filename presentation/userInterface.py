import pygame
from pygame.locals import *
from pygame import mixer
from domain.screen import Screen
from domain.world import World
from domain.clock import Clock

class UI():

    def __init__(self, button_service, world_service, enemy_service):
        self.__button_service = button_service
        self.__world_service = world_service
        self.__enemy_service = enemy_service
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
        world_data = self.__world_service.getWorldData(level)
        world_object_size = self.__world.getObjectSize()
        world_start_y = self.__world.getStartY()

        #load images
        wall_image = pygame.image.load("image/brick_wall.png") #1
        road_image = pygame.image.load("image/cracks.png") #2
        road_start_image = pygame.image.load("image/cracks_start.png") #3
        left_arrow = pygame.image.load("image/left_arrow.png") #4
        right_arrow = pygame.image.load("image/right_arrow.png") #5
        up_arrow = pygame.image.load("image/up_arrow.png") #6
        down_arrow = pygame.image.load("image/down_arrow.png") #7

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

                col_count += 1
            row_count += 1


    def __drawWorld(self):
        """
        draw world objects on screen
        :return:
        """
        #get screen
        display = self.__screen.getDisplay()

        #draw walls
        walls = self.__world_service.getAllWalls()
        for wall in walls:
            display.blit(wall.getImage(), (wall.getX(), wall.getY()))

        #draw start roads
        roads = self.__world_service.getAllStartRoads()
        for road in roads:
            display.blit(road.getImage(), (road.getX(), road.getY()))

        #draw roads
        roads = self.__world_service.getAllRoads()
        for road in roads:
            display.blit(road.getImage(), (road.getX(), road.getY()))

        #draw arrows
        arrows = self.__world_service.getAllArrows()
        for arrow in arrows:
            display.blit(arrow.getImage(), (arrow.getX(), arrow.getY()))




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
        center = self.__percent(world_object_size, 10)

        #aliens
        # id, image, x, y, width, height, power, life
        aliens_count = self.__enemy_service.getAliensCount(level)
        alien_image = pygame.image.load("image/alien.png")
        alien_image = pygame.transform.scale(alien_image, (enemy_size, enemy_size))
        alien_power = 10
        self.__enemy_service.createAliens(aliens_count, start_road, alien_image, enemy_size, alien_power, center)

    def __updateEnemies(self):
        """
        transmit arrows of game to service to update enemies position
        :return:
        """
        arrows = self.__world_service.getAllArrows()
        self.__enemy_service.updateAliens(arrows)

    def __drawEnemies(self):
        """
        draw enemies of game on screen
        :return:
        """
        #get screen
        display = self.__screen.getDisplay()

        #draw aliens
        aliens = self.__enemy_service.getAllAliens()
        for alien in aliens:
            display.blit(alien.getImage(), (alien.getX(), alien.getY()))

    def __setButtons(self):
        """
        initialize buttons of game
        :return:
        """
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()

        #exit button
        exit_image = pygame.image.load("image/exit.png")
        exit_button_x = width - self.__percent(width, 5)
        exit_button_y = 0
        exit_button_width = self.__percent(width, 5)
        exit_button_height = self.__percent(height, 5)
        exit_image = pygame.transform.scale(exit_image, (exit_button_width, exit_button_height))
        self.__button_service.createButton("exit", "common", exit_image, exit_button_x, exit_button_y, exit_button_width, exit_button_height)

        #minimize button
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

        #maximize button
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

            #self.__screen.fill(self.__screen_color)

            display = self.__screen.getDisplay()
            display.blit(self.__screen.getBackgroundImage(), (0, 0))

            if self.__screen.getMinimizedStatus() == False:
                self.__drawWorld()
                self.__drawGrid()
                self.__updateEnemies()
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
