from lib.packet.action.ShootActionPacket import ShootActionPacket
from lib.packet.action.MoveActionPacket import MoveActionPacket
from lib.position.Vector2 import Vector2
from lib.entity.Entity import Entity


class Player(Entity):

    def __init__(self):
        super().__init__(self.ENTITY_TYPE_PLAYER, "src/assets/player.png")
        self.set_position(Vector2(650, 650))
        self.health = 100
        self.damage = 20
        self.velocity = 20

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_velocity(self):
        return self.velocity

    def move(self, movement):
        if movement == '0xF':
            MoveActionPacket(self, Vector2(self.get_velocity(), 0)).__call__();
        elif movement == '0xB':
            MoveActionPacket(self, Vector2(-self.get_velocity(), 0)).__call__();

    def shoot(self):
        ShootActionPacket(self).__call__();