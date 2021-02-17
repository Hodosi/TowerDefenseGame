from presentation.userInterface import UI
from business.service import GameService
from persistence.repository import ButtonsRepository, WorldRepository

if __name__ == '__main__':
    buttons_repository = ButtonsRepository()
    world_repository = WorldRepository()
    game_service = GameService(buttons_repository, world_repository)
    screen = UI(game_service)
    screen.main_loop()
