from lib.manager.EntityManager import EntityManager
from lib.packet.action.ActionPacket import ActionPacket
from src.entity.Projectile import Projectile
from lib.position.Vector2 import Vector2

class ShootActionPacket(ActionPacket):

    def __init__(self, actor):
        super().__init__(self.ACTION_TYPE_SHOOT, actor)

    def __call__(self):
        projectile = Projectile(self.get_actor().get_position().add(Vector2(23, -20)))
        EntityManager().projectiles.append(projectile)
