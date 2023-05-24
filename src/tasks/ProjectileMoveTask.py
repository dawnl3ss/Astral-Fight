from lib.position.Vector2 import Vector2
from lib.task.Task import Task


class ProjectileMoveTask(Task):

    def __init__(self, projectile):
        super().__init__()
        self.projectile = projectile

    def on_run(self):
        if not self.is_remove(self.id):
            if self.projectile.get_position().get_y() >= 0:
                self.projectile.set_position(Vector2(self.projectile.get_position().get_x(), self.projectile.get_position().get_y() - 2.5))
            else:
                self.remove(self)
