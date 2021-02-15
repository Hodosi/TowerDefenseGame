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
        monitor = pygame.display.Info()
        self.__screen_width = monitor.current_w
        self.__screen_height = monitor.current_h
        self.__screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Tower Defense Game")
        background_image = pygame.image.load("image/background.png")
        background_image = pygame.transform.scale(background_image, (self.__screen_width, self.__screen_height))
        self.__screen_background_image = background_image

    def __setButtons(self):
        exit_image = pygame.image.load("image/exit.png")
        exit_button_x = self.__screen_width - self.__percent(self.__screen_width, 5)
        exit_button_y = 0
        exit_button_width = self.__percent(self.__screen_width, 5)
        exit_button_height = self.__percent(self.__screen_height, 5)
        exit_image = pygame.transform.scale(exit_image, (exit_button_width, exit_button_height))
        exit_button = Button("exit", "common", exit_image, exit_button_x, exit_button_y)
        self.__game_service.addButton(exit_button)

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
            button.setClickedStatus(False)

        return clicked


    def __drawCommonButtons(self):
        clicked_button = None
        common_buttons = self.__game_service.getButtonsByType("common")
        for button in common_buttons:
            if self.__buttonClicked(button):
                clicked_button = button

            self.__screen.blit(button.getImage(), (button.getX(), button.getY()))

        return clicked_button


    def main_loop(self):
        run = True
        while run:
            self.__clock.tick(self.__framerate)

            self.__screen.fill(self.__screen_color)

            self.__screen.blit(self.__screen_background_image, (0, 0))

            button = self.__drawCommonButtons()

            if button != None:
                if button.getName() == "exit":
                    run = False
                    break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            pygame.display.update()

        pygame.quit()
