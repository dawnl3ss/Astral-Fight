from lib.packet.action.ActionPacket import ActionPacket

class MoveActionPacket(ActionPacket):

    def __init__(self, actor, vector):
        super().__init__(self.ACTION_TYPE_MOVE, actor)
        self.vector = vector
        self.prev_location = actor.get_position()
        self.new_location = actor.get_position().add(vector)

    def get_vector(self):
        return self.vector

    def get_prev_location(self):
        return self.prev_location

    def get_new_location(self):
        return self.new_location

    def __call(self):
        self.actor.set_position(self.get_new_location())