from presentation.userInterface import UI
from business.service import ButtonService, WorldService, EnemyService
from persistence.repository import ButtonsRepository, WorldRepository, EnemyRepository

if __name__ == '__main__':
    buttons_repository = ButtonsRepository()
    world_repository = WorldRepository()
    enemy_repository = EnemyRepository()
    button_service = ButtonService(buttons_repository)
    world_service = WorldService(world_repository)
    enemy_service = EnemyService(enemy_repository)
    screen = UI(button_service, world_service, enemy_service)
    screen.main_loop()
