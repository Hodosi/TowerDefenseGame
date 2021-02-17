from presentation.userInterface import UI
from business.service import ButtonService, WorldService
from persistence.repository import ButtonsRepository, WorldRepository

if __name__ == '__main__':
    buttons_repository = ButtonsRepository()
    world_repository = WorldRepository()
    button_service = ButtonService(buttons_repository)
    world_service = WorldService(world_repository)
    screen = UI(button_service, world_service)
    screen.main_loop()
