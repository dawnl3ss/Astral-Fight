from lib.packet.Packet import Packet

class EntityPacket(Packet):

    def __init__(self, entity):
        super().__init__(self.PACKET_TYPE_ENTITY)
        self.entity =  entity

    def get_entity(self):
        return self.entity