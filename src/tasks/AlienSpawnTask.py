from lib.packet.entity.SpawnEntityPacket import SpawnEntityPacket
from lib.task.ScheduledTask import ScheduledTask

class AlienSpawnTask(ScheduledTask):

    def __init__(self):
        super().__init__(2 * 1000)

    def journey(self):
        if not self.is_remove(self.id):
            SpawnEntityPacket().__call__()
