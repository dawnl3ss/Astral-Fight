from lib.position.Vector2 import Vector2
from lib.task.ScheduledTask import ScheduledTask


class AlienMoveTask(ScheduledTask):

    def __init__(self, alien):
        super().__init__(1)
        self.alien = alien

    def journey(self):
        if not self.is_remove(self.id):
            self.alien.set_position(self.alien.get_position().add(Vector2(0, 5)))