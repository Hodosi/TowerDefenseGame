import pygame
from pygame.locals import *
from pygame import mixer


class Screen():

    def __init__(self, game_service):
        self.__game_service = game_service
        self.__screen = None
        self.__screen_background_image = None
        self.__screen_width = None
        self.__screen_height = None
        self.__screen_color = (0, 0, 0)
        self.__clock = None
        self.__framerate = None
        self.__screen_minimized = False
        self.__object_size = None
        self.__world_start_y = None
        self.__level = 1
        self.__setPygame()
        self.__setScreen()
        self.__setButtons()
        self.__initWorldSize()
        self.__setWorld()

    def __percent(self, size , prc):
        return int(size * prc / 100)


    def __setPygame(self):
        pygame.init()
        mixer.init()
        self.__clock = pygame.time.Clock()
        self.__framerate = 60

    def __setScreen(self):
        self.__resetScreen()
        pygame.display.set_caption("Tower Defense Game")
        background_image = pygame.image.load("image/background.png")
        background_image = pygame.transform.scale(background_image, (self.__screen_width, self.__screen_height))
        self.__screen_background_image = background_image

    def __resetScreen(self):
        monitor = pygame.display.Info()
        self.__screen_width = monitor.current_w
        self.__screen_height = monitor.current_h
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def __initWorldSize(self):
        monitor = pygame.display.Info()
        width = monitor.current_w
        self.__object_size = width // 30
        self.__world_start_y = self.__percent(self.__screen_height, 5)

    def __setWorld(self):
        world_data = self.__game_service.getWorldData(self.__level)

        wall_image = pygame.image.load("image/brick_wall.png")
        road_image = pygame.image.load("image/cracks.png")

        row_count = 0
        for line in world_data:
            col_count = 0
            y = row_count * self.__object_size + self.__world_start_y
            for value in line:
                x = col_count * self.__object_size
                if value == 1:
                    image = pygame.transform.scale(wall_image, (self.__object_size, self.__object_size))
                    self.__game_service.createWall(image, x, y)
                if value == 2:
                    image = pygame.transform.scale(road_image, (self.__object_size, self.__object_size))
                    self.__game_service.createRoad(image, x, y)

                col_count += 1
            row_count += 1

    def __drawWorld(self):
        walls = self.__game_service.getAllWalls()
        for wall in walls:
            self.__screen.blit(wall.getImage(), (wall.getX(), wall.getY()))

        roads = self.__game_service.getAllRoads()
        for road in roads:
            self.__screen.blit(road.getImage(), (road.getX(), road.getY()))



    def __drawGrid(self):
        # for visualization

        #lines
        monitor = pygame.display.Info()
        self.__screen_width = monitor.current_w
        self.__screen_height = monitor.current_h
        for i in range(0, 16):
            start_point = i * self.__object_size + self.__world_start_y
            pygame.draw.line(self.__screen, (255, 255, 255), (0, start_point), (self.__screen_width, start_point))

        #cols
        for i in range(0, 30):
            start_point = i * self.__object_size
            pygame.draw.line(self.__screen, (255, 255, 255), (start_point, self.__world_start_y), (start_point, self.__screen_height))

    def __setButtons(self):
        #exit button
        exit_image = pygame.image.load("image/exit.png")
        exit_button_x = self.__screen_width - self.__percent(self.__screen_width, 5)
        exit_button_y = 0
        exit_button_width = self.__percent(self.__screen_width, 5)
        exit_button_height = self.__percent(self.__screen_height, 5)
        exit_image = pygame.transform.scale(exit_image, (exit_button_width, exit_button_height))
        self.__game_service.createButton("exit", "common", exit_image, exit_button_x, exit_button_y)

        #minimize button
        minimize_image = pygame.image.load("image/minimize.png")
        minimize_button_x = self.__screen_width - 2 * self.__percent(self.__screen_width, 5) + 1*self.__percent(self.__screen_width, 1)
        minimize_button_y = self.__percent(self.__screen_height, 1)
        minimize_button_width = self.__percent(self.__screen_width, 4)
        minimize_button_height = self.__percent(self.__screen_height, 3)
        minimize_image = pygame.transform.scale(minimize_image, (minimize_button_width, minimize_button_height))
        self.__game_service.createButton("minimize", "common", minimize_image, minimize_button_x, minimize_button_y)

    def __set_maximize_button(self):
        #maximize button
        maximize_image = pygame.image.load("image/maximize.png")
        maximize_button_x = 0
        maximize_button_y = 0
        maximize_button_width = self.__screen_width
        maximize_button_height = self.__screen_height
        maximize_image = pygame.transform.scale(maximize_image, (maximize_button_width, maximize_button_height))
        self.__game_service.createButton("maximize", "special", maximize_image, maximize_button_x, maximize_button_y)

    def __buttonClicked(self, button):
        clicked = False

        # get mouse position
        mouse_position = pygame.mouse.get_pos()

        #check mouseover and clicked condition
        button_rectangle = button.getImage().get_rect()
        button_rectangle.x = button.getX()
        button_rectangle.y = button.getY()

        if button_rectangle.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] == 1 and button.getClickedStatus() == False:
                clicked = True
                button.setClickedStatus(True)

        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False
            button.setClickedStatus(False)

        return clicked


    def __drawButtons(self, type):
        clicked_button = None
        buttons = self.__game_service.getButtonsByType(type)
        for button in buttons:
            if self.__buttonClicked(button):
                clicked_button = button

            self.__screen.blit(button.getImage(), (button.getX(), button.getY()))

        return clicked_button


    def __buttonEvent(self, button):
        if button.getName() == "exit":
            return False
        if button.getName() == "maximize":
            self.__resetScreen()
            self.__game_service.deleteButtonByName("maximize")
            self.__screen_minimized = False

        elif button.getName() == "minimize":
            monitor = pygame.display.Info()
            self.__screen_width = self.__percent(monitor.current_w, 10)
            self.__screen_height = self.__percent(monitor.current_h, 10)
            self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
            self.__set_maximize_button()
            self.__screen_minimized = True
            maximize_button = self.__game_service.getButtonByName("maximize")
            maximize_button.setClickedStatus(True)


        return True


    def main_loop(self):
        run = True
        while run:
            self.__clock.tick(self.__framerate)

            #self.__screen.fill(self.__screen_color)

            self.__screen.blit(self.__screen_background_image, (0, 0))

            if self.__screen_minimized == False:
                self.__drawWorld()
                self.__drawGrid()
                button = self.__drawButtons("common")
            else:
                button = self.__drawButtons("special")


            if button != None:
                run = self.__buttonEvent(button)
                if run == False:
                    break


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            pygame.display.update()

        pygame.quit()
