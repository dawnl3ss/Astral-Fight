from lib.task.Task import Task
from src.maths.Timer import Timer

class ScheduledTask(Task):

    def __init__(self, s):
        super().__init__()
        self.timer = Timer(s)

    def get_timer(self):
        return self.timer

    def journey(self):
        pass

    def on_run(self):
        if self.get_timer().is_finished():
            self.journey()
            self.get_timer().update_time()

