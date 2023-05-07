from lib.entity.Entity import Entity
from lib.position.Vector2 import Vector2

class Player(Entity):

    def __init__(self):
        super().__init__(self.ENTITY_TYPE_PLAYER, "src/assets/player.png")
        self.set_position(Vector2(100, 650))
        self.health = 100
        self.damage = 20
        self.velocity = 20

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_velocity(self):
        return self.velocity