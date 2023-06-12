from lib.packet.entity.EntityPacket import EntityPacket
from lib.manager.EntityManager import EntityManager
from lib.position.Vector2 import Vector2
from src.maths.Calcul import Calcul
from src.entity.Alien import Alien

class SpawnEntityPacket(EntityPacket):

    def __init__(self):
        super().__init__(Alien(Vector2(Calcul().rand(10, 1410), 30)))

    def __call__(self):
        EntityManager().aliens[self.get_entity().get_id()] = self.get_entity()
        self.get_entity().start_move_task()