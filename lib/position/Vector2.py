class Vector2():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def add(self, vec2):
        return Vector2(self.x + vec2.x, self.y + vec2.y)