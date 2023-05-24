from lib.task.Task import Task

class TaskManager():

    def __init__(self):
        self.task = Task()

    def do_tasks(self):
        for task in self.task.pool:
            task.on_run()