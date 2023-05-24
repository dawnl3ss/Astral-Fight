from lib.position.Vector2 import Vector2
from lib.task.Task import Task


class AlienMoveTask(Task):

    def __init__(self, alien):
        super().__init__()
        self.alien = alien

    def on_run(self):
        if not self.is_remove(self.id):
            self.alien.set_position(self.alien.get_position().add(Vector2(0, 1)))
            print(self.alien.get_position().serialize())