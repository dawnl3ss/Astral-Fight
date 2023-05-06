from lib.packet.action.MoveActionPacket import MoveActionPacket
from lib.manager.PacketManager import emit_packet
from lib.position.Vector2 import Vector2
from pygame.sprite import Sprite

class Entity (Sprite):

    ENTITY_TYPE_PLAYER = 0
    ENTITY_TYPE_ALIEN = 1
    ENTITY_TYPE_PROJECTILE = 2

    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def get_position(self):
        return Vector2(self.rect.x, self.rect.y)

    def set_position(self, vec2):
        self.rect.x = vec2.get_x()
        self.rect.y = vec2.get_y()

    def move(self, vector):
        emit_packet(MoveActionPacket(self, vector))