from lib.task.ScheduledTask import ScheduledTask
from lib.manager.EntityManager import EntityManager
from src.maths.Calcul import Calcul
from lib.packet.entity.EntityColidePacket import EntityCollidePacket


class EntityCollideTask(ScheduledTask):

    def __init__(self):
        super().__init__(0.001 * 1000)
        self.manager = EntityManager()
        self.calcul = Calcul()

    def journey(self):
        if not self.is_remove(self.id):

            for projectile in list(self.manager.get_projectiles().values()):
                for alien in list(self.manager.get_aliens().values()):
                    if self.calcul.is_in_range(projectile.get_position().get_x(), alien.get_position().get_x() - 50, alien.get_position().get_x() + 50) and self.calcul.is_in_range(projectile.get_position().get_y(), alien.get_position().get_y() - 15, alien.get_position().get_y() + 15):
                        EntityCollidePacket(projectile, alien).__call__()


