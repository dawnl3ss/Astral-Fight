from lib.entity.Entity import Entity
from lib.position.Vector2 import Vector2
from src.tasks.AlienMoveTask import AlienMoveTask

class Alien(Entity):

    def __init__(self, vec2):
        super().__init__(self.ENTITY_TYPE_ALIEN, "src/assets/alien.png")
        self.set_position(vec2)
        self.damage = 20
        self.velocity = 20

    def get_damage(self):
        return self.damage

    def get_velocity(self):
        return self.velocity

    def start_move_task(self):
        task = AlienMoveTask(self)
        task.on_run()