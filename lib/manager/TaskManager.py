from lib.task.Task import Task

class TaskManager():

    def do_tasks(self):
        for task in Task().pool:
            task.on_run()