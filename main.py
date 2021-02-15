from presentation.userInterface import Screen
from business.service import GameService
from persistence.repository import ButtonsRepository

if __name__ == '__main__':
    buttons_repository = ButtonsRepository()
    game_service = GameService(buttons_repository)
    screen = Screen(game_service)
    screen.main_loop()
