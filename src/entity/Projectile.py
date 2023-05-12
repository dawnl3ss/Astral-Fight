from lib.entity.Entity import Entity
from src.tasks.ProjectileMoveTask import ProjectileMoveTask

class Projectile(Entity):

    def __init__(self, vec2):
        super().__init__(self.ENTITY_TYPE_PROJECTILE, "src/assets/projectile.png")
        self.set_position(vec2)
        self.damage = 20
        self.velocity = 20

    def get_damage(self):
        return self.damage

    def get_velocity(self):
        return self.velocity

    def start_move_task(self):
        task = ProjectileMoveTask(self)
        task.on_run()