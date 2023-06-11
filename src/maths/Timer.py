import time

class Timer:

    def __init__(self, ms):
        self.constructTime = int(round(time.time() * 1000))
        self.ms = ms

    def update_time(self):
        self.constructTime = int(round(time.time() * 1000))

    # Vérifier si le timer est fini
    def is_finished(self):
        return int(round(time.time() * 1000)) >= self.constructTime + self.ms
