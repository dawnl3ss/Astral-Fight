class Packet():

    PACKET_TYPE_ACTION = 0

    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    # decode the packet
    def __call(self):
        pass