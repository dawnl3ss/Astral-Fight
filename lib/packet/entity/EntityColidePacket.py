from lib.packet.entity.EntityPacket import EntityPacket
from lib.manager.EntityManager import EntityManager

class EntityCollidePacket(EntityPacket):

    def __init__(self, collider, collided):
        super().__init__(collider)
        self.collided = collided

    def get_collider(self):
        return self.get_entity()

    def get_collided(self):
        return self.collided

    def __call__(self):
        manager = EntityManager()
        manager.projectiles.pop(self.get_collider().get_id())
        manager.aliens.pop(self.get_collided().get_id())