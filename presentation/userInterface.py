import pygame
from pygame.locals import *
from pygame import mixer
from domain.screen import Screen
from domain.world import World
from domain.clock import Clock

class UI():

    def __init__(self, game_service):
        self.__game_service = game_service
        self.__screen = Screen()
        self.__world = World()
        self.__clock = Clock()
        self.__setPygame()
        self.__setClock()
        self.__setScreen()
        self.__setButtons()
        self.__initWorldSize()
        self.__setWorld()


    def __percent(self, size, prc):
        return int(size * prc / 100)


    def __setPygame(self):
        pygame.init()
        mixer.init()

    def __setClock(self):
        self.__clock.setTime(pygame.time.Clock())
        self.__clock.setFramerate(60)


    def __setScreen(self):
        self.__resetScreen()
        pygame.display.set_caption("Tower Defense Game")
        background_image = pygame.image.load("image/background.png")
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()
        background_image = pygame.transform.scale(background_image, (width, height))
        self.__screen.setBackgroundImage(background_image)

    def __resetScreen(self):
        monitor = pygame.display.Info()
        width = monitor.current_w
        height = monitor.current_h
        self.__screen.setWidth(width)
        self.__screen.setHeight(height)
        display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.__screen.setDisplay(display)

    def __initWorldSize(self):
        monitor = pygame.display.Info()
        width = monitor.current_w
        size = width // 30
        self.__world.setObjectSize(size)
        height = self.__screen.getHeight()
        y_position = self.__percent(height, 5)
        self.__world.setStartY(y_position)

    def __setWorld(self):
        level = self.__world.getLevel()
        world_data = self.__game_service.getWorldData(level)
        world_object_size = self.__world.getObjectSize()
        world_start_y = self.__world.getStartY()

        wall_image = pygame.image.load("image/brick_wall.png")
        road_image = pygame.image.load("image/cracks.png")

        row_count = 0
        for line in world_data:
            col_count = 0
            y = row_count * world_object_size + world_start_y
            for value in line:
                x = col_count * world_object_size
                if value == 1:
                    image = pygame.transform.scale(wall_image, (world_object_size, world_object_size))
                    self.__game_service.createWall(image, x, y)
                if value == 2:
                    image = pygame.transform.scale(road_image, (world_object_size, world_object_size))
                    self.__game_service.createRoad(image, x, y)

                col_count += 1
            row_count += 1

    def __drawWorld(self):
        display = self.__screen.getDisplay()

        walls = self.__game_service.getAllWalls()
        for wall in walls:
            display.blit(wall.getImage(), (wall.getX(), wall.getY()))

        roads = self.__game_service.getAllRoads()
        for road in roads:
            display.blit(road.getImage(), (road.getX(), road.getY()))



    def __drawGrid(self):
        # for visualization

        #lines
        monitor = pygame.display.Info()
        self.__screen.setWidth(monitor.current_w)
        self.__screen.setHeight(monitor.current_h)

        width = self.__screen.getWidth()
        height = self.__screen.getHeight()
        display = self.__screen.getDisplay()

        world_object_size = self.__world.getObjectSize()
        world_start_y = self.__world.getStartY()

        for i in range(0, 16):
            start_point = i * world_object_size + world_start_y
            pygame.draw.line(display, (255, 255, 255), (0, start_point), (width, start_point))

        #cols
        for i in range(0, 30):
            start_point = i * world_object_size
            pygame.draw.line(display, (255, 255, 255), (start_point, world_start_y), (start_point, height))

    def __setButtons(self):
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()

        #exit button
        exit_image = pygame.image.load("image/exit.png")
        exit_button_x = width - self.__percent(width, 5)
        exit_button_y = 0
        exit_button_width = self.__percent(width, 5)
        exit_button_height = self.__percent(height, 5)
        exit_image = pygame.transform.scale(exit_image, (exit_button_width, exit_button_height))
        self.__game_service.createButton("exit", "common", exit_image, exit_button_x, exit_button_y)

        #minimize button
        minimize_image = pygame.image.load("image/minimize.png")
        minimize_button_x = width - 2 * self.__percent(width, 5) + 1*self.__percent(width, 1)
        minimize_button_y = self.__percent(height, 1)
        minimize_button_width = self.__percent(width, 4)
        minimize_button_height = self.__percent(height, 3)
        minimize_image = pygame.transform.scale(minimize_image, (minimize_button_width, minimize_button_height))
        self.__game_service.createButton("minimize", "common", minimize_image, minimize_button_x, minimize_button_y)

    def __set_maximize_button(self):
        width = self.__screen.getWidth()
        height = self.__screen.getHeight()

        #maximize button
        maximize_image = pygame.image.load("image/maximize.png")
        maximize_button_x = 0
        maximize_button_y = 0
        maximize_button_width = width
        maximize_button_height = height
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
        display = self.__screen.getDisplay()

        clicked_button = None
        buttons = self.__game_service.getButtonsByType(type)
        for button in buttons:
            if self.__buttonClicked(button):
                clicked_button = button

            display.blit(button.getImage(), (button.getX(), button.getY()))

        return clicked_button


    def __buttonEvent(self, button):
        if button.getName() == "exit":
            return False
        if button.getName() == "maximize":
            self.__resetScreen()
            self.__game_service.deleteButtonByName("maximize")
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
            maximize_button = self.__game_service.getButtonByName("maximize")
            maximize_button.setClickedStatus(True)


        return True


    def main_loop(self):
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
