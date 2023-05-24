from src.maths.Calcul import Calcul
from lib.task.Pool import Pool

class Task(Pool):

    task_list = []

    def __init__(self):
        self.id = Calcul().rand(0, 9999999999999)
        self.task_list.append(self.id)
        self.add(self)

    def remove_task(self, id):
        if id in self.task_list:
            self.task_list.remove(id)

    def is_remove(self, id):
        return not id in self.task_list

    def on_run(self):
        pass