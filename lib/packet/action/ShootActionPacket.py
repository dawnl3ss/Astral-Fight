from lib.packet.action.ActionPacket import ActionPacket

class ShootActionPacket(ActionPacket):

    def __init__(self, actor):
        super().__init__(self.ACTION_TYPE_SHOOT, actor)

    def __call(self):
        pass