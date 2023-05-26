import time

class Timer:

    def __init__(self, ms):
        self.constructTime = time.localtime(time.time())[5]
        self.ms = ms

    def update_time(self):
        self.constructTime = time.localtime(time.time())[5]

    # Vérifier si le timer est fini
    def is_finished(self):
        return time.localtime(time.time())[5] == self.constructTime + self.ms
