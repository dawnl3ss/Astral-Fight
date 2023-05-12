from lib.entity.Entity import Entity
from lib.position.Vector2 import Vector2

class Alien(Entity):

    def __init__(self):
        super().__init__(self.ENTITY_TYPE_ALIEN, "src/assets/alien.png")
        self.set_position(Vector2(500, 500))
        self.damage = 20
        self.velocity = 20

    def get_damage(self):
        return self.damage

    def get_velocity(self):
        return self.velocity