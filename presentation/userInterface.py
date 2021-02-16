import pygame
from pygame.locals import *
from pygame import mixer
from domain.valueObject import Button


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
        self.__setPygame()
        self.__setScreen()
        self.__setButtons()

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




    def __setButtons(self):
        #exit button
        exit_image = pygame.image.load("image/exit.png")
        exit_button_x = self.__screen_width - self.__percent(self.__screen_width, 5)
        exit_button_y = 0
        exit_button_width = self.__percent(self.__screen_width, 5)
        exit_button_height = self.__percent(self.__screen_height, 5)
        exit_image = pygame.transform.scale(exit_image, (exit_button_width, exit_button_height))
        exit_button = Button("exit", "common", exit_image, exit_button_x, exit_button_y)
        self.__game_service.addButton(exit_button)

        #minimize button
        minimize_image = pygame.image.load("image/minimize.png")
        minimize_button_x = self.__screen_width - 2 * self.__percent(self.__screen_width, 5) + 1*self.__percent(self.__screen_width, 1)
        minimize_button_y = self.__percent(self.__screen_height, 1)
        minimize_button_width = self.__percent(self.__screen_width, 4)
        minimize_button_height = self.__percent(self.__screen_height, 3)
        minimize_image = pygame.transform.scale(minimize_image, (minimize_button_width, minimize_button_height))
        minimize_button = Button("minimize", "common", minimize_image, minimize_button_x, minimize_button_y)
        self.__game_service.addButton(minimize_button)

    def __set_maximize_button(self):
        #maximize button
        maximize_image = pygame.image.load("image/maximize.png")
        maximize_button_x = 0
        maximize_button_y = 0
        maximize_button_width = self.__screen_width
        maximize_button_height = self.__screen_height
        maximize_image = pygame.transform.scale(maximize_image, (maximize_button_width, maximize_button_height))
        maximize_button = Button("maximize", "special", maximize_image, maximize_button_x, maximize_button_y)
        self.__game_service.addButton(maximize_button)

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
