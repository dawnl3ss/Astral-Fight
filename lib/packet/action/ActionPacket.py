from lib.packet.Packet import Packet

class ActionPacket(Packet):

    ACTION_TYPE_MOVE = 0
    ACTION_TYPE_SHOOT = 1

    def __init__(self, action, actor):
        super().__init__(self.PACKET_TYPE_ACTION)
        self.action = action
        self.actor = actor

    def get_action_type(self):
        return self.action

    def get_actor(self):
        return self.actor

    def __call__(self):
        pass