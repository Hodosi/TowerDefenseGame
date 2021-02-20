from presentation.userInterface import UI
from business.worldService import WorldService
from business.buttonService import ButtonService
from business.enemyService import EnemyService
from business.warriorService import WarriorService
from persistence.repository import ButtonsRepository, WorldRepository, EnemyRepository, WarriorRepository

if __name__ == '__main__':
    buttons_repository = ButtonsRepository()
    world_repository = WorldRepository()
    enemy_repository = EnemyRepository()
    warrior_repository = WarriorRepository()
    button_service = ButtonService(buttons_repository)
    world_service = WorldService(world_repository)
    enemy_service = EnemyService(enemy_repository)
    warrior_service = WarriorService(warrior_repository)
    screen = UI(button_service, world_service, enemy_service, warrior_service)
    screen.main_loop()
