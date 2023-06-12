from lib.manager.EntityManager import EntityManager
from lib.manager.TaskManager import TaskManager
from src.entity.Player import Player
from src.tasks.AlienSpawnTask import AlienSpawnTask
import pygame

from src.tasks.EntityCollideTask import EntityCollideTask


class Game():

    def __init__(self):
        self.entity_manager = EntityManager()
        self.task_manager = TaskManager()
        self.pressed_keys = {}
        self.player = Player()
        self.running = True
        self.create_window()
        self.start_tasks()

    def is_running(self):
        return self.running

    def set_running(self, value):
        self.running = value

    def create_window(self):
        pygame.display.set_caption("Astral-Fight | Shoot the aliens !")
        self.background = pygame.image.load("src/assets/background.jpg")
        self.screen = pygame.display.set_mode((1500, 800))

    def display_screen(self):
        self.screen.blit(self.background, (0, -200))

    def display_player(self):
        self.screen.blit(self.player.image, self.player.rect)

    def display_projectiles(self):
        for projectiles in list(self.entity_manager.get_projectiles().values()):
            if projectiles.get_position().get_y() >= 0:
                print(projectiles.get_position().get_y())
                self.screen.blit(projectiles.image, projectiles.rect)
            else:
                del self.entity_manager.projectiles[projectiles.get_id()]

    def display_aliens(self):
        for aliens in self.entity_manager.get_aliens().values():
            self.screen.blit(aliens.image, aliens.rect)

    def update_screen(self):
        pygame.display.flip()

    def start_tasks(self):
        alien_spawn = AlienSpawnTask()
        entity_collide = EntityCollideTask()
        alien_spawn.on_run()
        entity_collide.on_run()

    def update_tasks(self):
        self.task_manager.do_tasks()

    def update_all(self):
        self.display_screen()
        self.display_player()
        self.display_projectiles()
        self.display_aliens()
        self.update_screen()
        self.update_tasks()