class Pool():

    pool = []

    def add(self, task):
        self.pool.append(task)

    def remove(self, task):
        self.pool.remove(task)